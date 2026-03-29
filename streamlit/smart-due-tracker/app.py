import streamlit as st
import sqlite3
from datetime import datetime

# ------------------ DB CONNECTION ------------------
conn = sqlite3.connect("dues.db", check_same_thread=False)
c = conn.cursor()

# ------------------ CREATE TABLE ------------------
c.execute("""
CREATE TABLE IF NOT EXISTS dues (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    category TEXT,
    amount REAL,
    due_date TEXT,
    status TEXT,
    created_at TEXT,
    updated_at TEXT,
    notes TEXT,
    priority TEXT
)
""")
conn.commit()

# ------------------ FUNCTIONS ------------------

def add_due(title, category, amount, due_date, status, notes, priority):
    now = datetime.now()
    c.execute("""
        INSERT INTO dues (title, category, amount, due_date, status, created_at, updated_at, notes, priority)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (title, category, amount, due_date, status, now, now, notes, priority))
    conn.commit()


def get_dues():
    return c.execute("SELECT * FROM dues ORDER BY due_date ASC").fetchall()


def delete_due(due_id):
    c.execute("DELETE FROM dues WHERE id=?", (due_id,))
    conn.commit()


def mark_paid(due_id):
    now = datetime.now()
    c.execute("UPDATE dues SET status='Paid', updated_at=? WHERE id=?", (now, due_id))
    conn.commit()


def update_due(due_id, title, category, amount, due_date, status, notes, priority):
    now = datetime.now()
    c.execute("""
        UPDATE dues
        SET title=?, category=?, amount=?, due_date=?, status=?, updated_at=?, notes=?, priority=?
        WHERE id=?
    """, (title, category, amount, due_date, status, now, notes, priority, due_id))
    conn.commit()

# ------------------ UI ------------------

st.set_page_config(page_title="Due Tracker", layout="wide")
st.title("Smart Due Tracker")

# ------------------ FILTER ------------------

st.header("Filter")

col1, col2 = st.columns(2)

with col1:
    filter_status = st.selectbox("Filter by Status", ["All", "Pending", "Paid"])

with col2:
    filter_priority = st.selectbox("Filter by Priority", ["All", "High", "Medium", "Low"])

# ------------------ VIEW SECTION ------------------

st.header("All Dues")

dues = get_dues()

# Apply filters
if filter_status != "All":
    dues = [d for d in dues if d[5] == filter_status]

if filter_priority != "All":
    dues = [d for d in dues if d[9] == filter_priority]

if len(dues) == 0:
    st.info("No dues found")
else:
    for d in dues:
        with st.container():
            col1, col2, col3, col4 = st.columns([2, 2, 2, 2])

            with col1:
                st.write(d[1])
                st.caption(f"{d[2]} | {d[9]}")

            with col2:
                st.write(f"Amount: {d[3]}")
                st.write(f"Due Date: {d[4]}")

            with col3:
                st.write(f"Status: {d[5]}")
                st.caption(d[8])

            with col4:
                if st.button("Mark Paid", key=f"paid_{d[0]}"):
                    mark_paid(d[0])
                    st.rerun()

                if st.button("Delete", key=f"del_{d[0]}"):
                    delete_due(d[0])
                    st.rerun()

            # ------------------ UPDATE ------------------
            with st.expander(f"Edit {d[1]}"):
                new_title = st.text_input("Title", d[1], key=f"title_{d[0]}")
                new_category = st.selectbox(
                    "Category",
                    ["Rent", "Bills", "Credit Card", "Personal"],
                    key=f"cat_{d[0]}"
                )
                new_amount = st.number_input("Amount", value=d[3], key=f"amt_{d[0]}")
                new_due_date = st.date_input(
                    "Due Date",
                    value=datetime.strptime(d[4], "%Y-%m-%d"),
                    key=f"date_{d[0]}"
                )
                new_status = st.selectbox(
                    "Status",
                    ["Pending", "Paid"],
                    key=f"status_{d[0]}"
                )
                new_priority = st.selectbox(
                    "Priority",
                    ["High", "Medium", "Low"],
                    key=f"pri_{d[0]}"
                )
                new_notes = st.text_area("Notes", d[8], key=f"notes_{d[0]}")

                if st.button("Update", key=f"update_{d[0]}"):
                    update_due(
                        d[0],
                        new_title,
                        new_category,
                        new_amount,
                        new_due_date,
                        new_status,
                        new_notes,
                        new_priority
                    )
                    st.success("Updated successfully")
                    st.rerun()

            st.divider()

# ------------------ ADD SECTION ------------------

st.header("Add New Due")

col1, col2, col3 = st.columns(3)

with col1:
    title = st.text_input("Title")
    category = st.selectbox("Category", ["Rent", "Bills", "Credit Card", "Personal"])

with col2:
    amount = st.number_input("Amount", min_value=0.0)
    due_date = st.date_input("Due Date")

with col3:
    status = st.selectbox("Status", ["Pending", "Paid"])
    priority = st.selectbox("Priority", ["High", "Medium", "Low"])

notes = st.text_area("Notes")

if st.button("Add Due"):
    if title and amount:
        add_due(title, category, amount, due_date, status, notes, priority)
        st.success("Due Added Successfully")
        st.rerun()
    else:
        st.warning("Please fill required fields")
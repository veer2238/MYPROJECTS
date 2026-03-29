# Smart Due Tracker

A simple and efficient web application to manage and track your daily dues like rent, credit cards, bills, and personal payments.

Built using Streamlit and SQLite.

---

## Features

* Add new dues with title, category, amount, due date, status, and priority
* View all dues in a clean layout
* Filter dues by status (Pending / Paid)
* Filter dues by priority (High / Medium / Low)
* Update existing dues
* Delete dues
* Mark dues as paid
* Notes section for additional information

---

## Tech Stack

* Python
* Streamlit
* SQLite

---

## Project Structure

smart-due-tracker/
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore

---

## Installation

1. Clone the repository

```

2. Navigate to the project folder

```
cd smart-due-tracker
```

3. Install dependencies

```
pip install -r requirements.txt
```

4. Run the application

```
streamlit run app.py
```

---

## Deployment

This app can be deployed easily using Streamlit Community Cloud.

Steps:

* Upload project to GitHub
* Go to Streamlit Cloud
* Connect your repository
* Deploy the app

---

## Notes

* SQLite database is used for local storage
* On cloud deployment, data may reset due to temporary storage

---

## Future Improvements

* Dashboard with charts and analytics
* User authentication (login system)
* Reminder notifications
* Export data to Excel
* Cloud database integration



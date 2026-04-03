import csv
from datetime import datetime, timedelta

start_date = datetime(2020, 1, 1)
end_date = datetime(2025, 12, 31)

current_date = start_date

with open("date_dim.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow([
        "date",
        "day",
        "month",
        "month_name",
        "quarter",
        "year",
        "week_number",
        "day_name"
    ])

    while current_date <= end_date:
        date = current_date.date()
        day = current_date.day
        month = current_date.month
        month_name = current_date.strftime("%B")
        quarter = (current_date.month - 1) // 3 + 1
        year = current_date.year
        week_number = current_date.isocalendar()[1]
        day_name = current_date.strftime("%A")

        writer.writerow([
            date,
            day,
            month,
            month_name,
            quarter,
            year,
            week_number,
            day_name
        ])

        current_date += timedelta(days=1)

print("✅ Date Dimension dataset generated successfully!")
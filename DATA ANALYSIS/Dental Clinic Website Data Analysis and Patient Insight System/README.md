Dental Clinic Website Data Analysis and Patient Insight System

Sheet 1: Overview Dashboard
Purpose: Summary of overall clinic performance
KPIs:
Total Patients
Total Appointments
Total Revenue
Average Rating
No-Show Rate (%)
Average Waiting Time
Charts:
Line Chart: Revenue by Month
Column Chart: Appointments by Month
Pie Chart: Appointment Status (Completed, Cancelled, No-Show)
Filters:
Date
City
Treatment Category
Sheet 2: Patient Insights
Purpose: Analyze patient demographics
KPIs:
Total Patients
New Patients
Returning Patients
Charts:
Column Chart: Patients by Age Group
Pie Chart: Gender Distribution
Column Chart: Patients by City
Donut Chart: Medical Condition Distribution
Filters:
Gender
City
Registration Date
Sheet 3: Appointment Analysis
Purpose: Understand booking patterns
KPIs:
Total Appointments
No-Show Count
Cancellation Rate
Charts:
Line Chart: Appointments by Date
Column Chart: Appointments by Time Slot
Stacked Column: Visit Type (New vs Follow-up)
Pie Chart: Booking Source
Filters:
Dentist
Treatment
Date
Sheet 4: Dentist Performance
Purpose: Evaluate dentist performance
KPIs:
Total Dentists
Average Experience
Charts:
Column Chart: Appointments per Dentist
Column Chart: Revenue per Dentist
Table: Dentist Name, Specialization, Experience, Appointments
Pie Chart: Availability Status
Filters:
Specialization
Availability
Sheet 5: Revenue Analysis
Purpose: Financial performance and trends
KPIs:
Total Revenue
Total Discount
Net Revenue
Pending Payments
Charts:
Line Chart: Revenue by Month
Column Chart: Revenue by Treatment
Pie Chart: Payment Mode
Column Chart: Payment Status
Filters:
Date
Treatment
Payment Mode
Sheet 6: Feedback and Satisfaction
Purpose: Analyze patient reviews
KPIs:
Average Rating
Total Reviews
Positive Review Percentage
Charts:
Pie Chart: Sentiment Distribution
Column Chart: Ratings (1 to 5)
Line Chart: Rating Trend Over Time
Table: Review Text
Filters:
Rating
Sentiment
Date
Data Model Relationships (Very Important)
Patients.Patient_ID → Appointments.Patient_ID
Appointments.Appointment_ID → Billing.Appointment_ID
Appointments.Appointment_ID → Reviews.Appointment_ID
Treatments.Treatment_ID → Appointments.Treatment_ID
Dentists.Dentist_ID → Appointments.Dentist_ID
All relationships should be set as One-to-Many.

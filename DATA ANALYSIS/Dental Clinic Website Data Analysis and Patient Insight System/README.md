# Clinic Performance Dashboard

## Overview
This project provides a comprehensive analytics dashboard for monitoring and improving clinic operations. It covers patient insights, appointment trends, dentist performance, revenue analysis, and patient feedback.

---

## Dashboard Structure

### Sheet 1: Overview Dashboard
Purpose: Summary of overall clinic performance  

Key KPIs:
- Total Patients  
- Total Appointments  
- Total Revenue  
- Average Rating  
- No-Show Rate (%)  
- Average Waiting Time  

Visualizations:
- Line Chart: Revenue by Month  
- Column Chart: Appointments by Month  
- Pie Chart: Appointment Status (Completed, Cancelled, No-Show)  

Filters:
- Date  
- City  
- Treatment Category  

---

### Sheet 2: Patient Insights
Purpose: Analyze patient demographics  

Key KPIs:
- Total Patients  
- New Patients  
- Returning Patients  

Visualizations:
- Column Chart: Patients by Age Group  
- Pie Chart: Gender Distribution  
- Column Chart: Patients by City  
- Donut Chart: Medical Condition Distribution  

Filters:
- Gender  
- City  
- Registration Date  

---

### Sheet 3: Appointment Analysis
Purpose: Understand booking patterns  

Key KPIs:
- Total Appointments  
- No-Show Count  
- Cancellation Rate  

Visualizations:
- Line Chart: Appointments by Date  
- Column Chart: Appointments by Time Slot  
- Stacked Column Chart: Visit Type (New vs Follow-up)  
- Pie Chart: Booking Source  

Filters:
- Dentist  
- Treatment  
- Date  

---

### Sheet 4: Dentist Performance
Purpose: Evaluate dentist performance  

Key KPIs:
- Total Dentists  
- Average Experience  

Visualizations:
- Column Chart: Appointments per Dentist  
- Column Chart: Revenue per Dentist  
- Table: Dentist Name, Specialization, Experience, Appointments  
- Pie Chart: Availability Status  

Filters:
- Specialization  
- Availability  

---

### Sheet 5: Revenue Analysis
Purpose: Financial performance and trends  

Key KPIs:
- Total Revenue  
- Total Discount  
- Net Revenue  
- Pending Payments  

Visualizations:
- Line Chart: Revenue by Month  
- Column Chart: Revenue by Treatment  
- Pie Chart: Payment Mode  
- Column Chart: Payment Status  

Filters:
- Date  
- Treatment  
- Payment Mode  

---

### Sheet 6: Feedback and Satisfaction
Purpose: Analyze patient reviews  

Key KPIs:
- Average Rating  
- Total Reviews  
- Positive Review Percentage  

Visualizations:
- Pie Chart: Sentiment Distribution  
- Column Chart: Ratings (1 to 5)  
- Line Chart: Rating Trend Over Time  
- Table: Review Text  

Filters:
- Rating  
- Sentiment  
- Date  

---

## Data Model Relationships (Critical)

Ensure the following relationships are properly configured:

- Patients.Patient_ID → Appointments.Patient_ID  
- Appointments.Appointment_ID → Billing.Appointment_ID  
- Appointments.Appointment_ID → Reviews.Appointment_ID  
- Treatments.Treatment_ID → Appointments.Treatment_ID  
- Dentists.Dentist_ID → Appointments.Dentist_ID  

Relationship Type: One-to-Many (1:N)

---

## Tools and Technologies
- Power BI / Tableau / Excel  
- Data Modeling  
- Data Visualization Techniques  

---

## Usage
1. Load the dataset into your BI tool  
2. Establish the defined relationships  
3. Create visuals as per each sheet  
4. Apply filters for interactive analysis  

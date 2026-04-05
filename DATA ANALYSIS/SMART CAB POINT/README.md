Smart Cab Point – Ride Booking Data Analysis and Demand Prediction


# Ride Booking Business Dashboard

## Overview
This project provides a comprehensive analytics dashboard for monitoring and optimizing ride booking business performance. It includes demand patterns, revenue insights, driver performance, customer behavior, and operational efficiency.

---

## Dashboard Structure

### Sheet 1: Overview Dashboard
Purpose: Summary of overall business performance  

Key KPIs:
- Total Rides  
- Total Bookings  
- Total Revenue  
- Average Ride Distance  
- Average Customer Rating  
- Cancellation Rate (%)  

Visualizations:
- Line Chart: Revenue by Month  
- Column Chart: Rides by Month  
- Pie Chart: Ride Status (Completed, Cancelled, No-Show)  
- Area Chart: Bookings Trend  

Filters:
- Date  
- City  
- Vehicle Type  

---

### Sheet 2: Demand Analysis
Purpose: Analyze demand patterns across time and location  

Key KPIs:
- Peak Booking Hour  
- Total Bookings  
- Average Bookings per Day  
- Highest Demand Location  

Visualizations:
- Heatmap: Bookings by Hour vs Day  
- Column Chart: Bookings by City  
- Bar Chart: Top Pickup Locations  
- Line Chart: Daily Booking Trend  

Filters:
- City  
- Ride Type  

---

### Sheet 3: Revenue Analysis
Purpose: Analyze revenue trends and pricing  

Key KPIs:
- Total Revenue  
- Average Fare per Ride  
- Total Surge Amount  
- Total Discount Amount  

Visualizations:
- Line Chart: Revenue Trend (Monthly/Daily)  
- Stacked Column Chart: Fare vs Surge vs Discount  
- Pie Chart: Payment Method Distribution  
- Bar Chart: Revenue by City  

Filters:
- Payment Method  
- City  
- Date  

---

### Sheet 4: Driver Performance
Purpose: Evaluate driver efficiency and performance  

Key KPIs:
- Total Drivers  
- Average Driver Rating  
- Total Rides Completed  
- Driver Cancellation Rate  

Visualizations:
- Bar Chart: Top Drivers by Rides  
- Scatter Plot: Driver Rating vs Rides Completed  
- Column Chart: Driver Availability Status  
- Table: Driver Details  

Filters:
- City  
- Availability Status  

---

### Sheet 5: Customer Insights
Purpose: Analyze customer behavior and segmentation  

Key KPIs:
- Total Customers  
- New Customers  
- Returning Customers  
- Average Customer Rating  

Visualizations:
- Pie Chart: Loyalty Status  
- Column Chart: Customers by City  
- Bar Chart: Payment Preference  
- Histogram: Age Distribution  

Filters:
- City  
- Loyalty Status  

---

### Sheet 6: Operations and Efficiency
Purpose: Improve operational performance and service quality  

Key KPIs:
- Average Ride Duration  
- Average Waiting Time  
- Cancellation Rate  
- Completion Rate  

Visualizations:
- Line Chart: Average Ride Duration Trend  
- Bar Chart: Cancellation Reasons  
- Column Chart: Ride Status Trend  
- Map: Pickup and Drop Locations  

Filters:
- City  
- Date  
- Vehicle Type  

---

## Data Model Relationships (Suggested)

Ensure the following relationships are properly configured:

- Customers.Customer_ID → Bookings.Customer_ID  
- Bookings.Booking_ID → Rides.Booking_ID  
- Drivers.Driver_ID → Rides.Driver_ID  
- Rides.Ride_ID → Payments.Ride_ID  
- Vehicles.Vehicle_ID → Rides.Vehicle_ID  

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

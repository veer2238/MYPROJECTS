Smile Café Point – Food Booking Data Analysis and Sales Optimization

# Café Performance Dashboard

## Overview
This project provides a comprehensive analytics dashboard for monitoring and improving café operations. It covers customer insights, booking trends, order analysis, sales performance, and payment behavior.

---

## Dashboard Structure

### Sheet 1: Overview Dashboard
Purpose: Summary of overall café performance  

Key KPIs:
- Total Customers  
- Total Orders  
- Total Revenue  
- Average Order Value  
- Total Bookings  

Visualizations:
- Line Chart: Revenue by Month  
- Column Chart: Orders by Month  
- Pie Chart: Order Status (Completed, Pending, Cancelled)  
- Donut Chart: Order Type (Dine-in vs Takeaway)  

Filters:
- Date  
- Order Type  
- Payment Method  
- Category  

---

### Sheet 2: Customer Insights
Purpose: Analyze customer demographics and behavior  

Key KPIs:
- Total Customers  
- New Customers  
- Returning Customers  

Visualizations:
- Column Chart: Customers by Age Group  
- Pie Chart: Gender Distribution  
- Column Chart: Customers by Visit Type (Walk-in, Regular, Member)  
- Line Chart: Customer Registration Trend  

Filters:
- Gender  
- Visit Type  
- Registration Date  

---

### Sheet 3: Booking Analysis
Purpose: Understand table reservation patterns  

Key KPIs:
- Total Bookings  
- Completed Bookings  
- Cancelled Bookings  

Visualizations:
- Line Chart: Bookings by Date  
- Column Chart: Bookings by Time Slot  
- Column Chart: Number of People per Booking  
- Pie Chart: Booking Status  

Filters:
- Booking Date  
- Table Number  
- Booking Status  

---

### Sheet 4: Order Analysis
Purpose: Analyze ordering behavior  

Key KPIs:
- Total Orders  
- Dine-in Orders  
- Takeaway Orders  

Visualizations:
- Line Chart: Orders by Date  
- Column Chart: Orders by Time Slot  
- Stacked Column Chart: Orders by Type (Dine-in vs Takeaway)  
- Pie Chart: Orders with Booking vs Walk-in  

Filters:
- Order Type  
- Order Status  
- Date  

---

### Sheet 5: Sales and Menu Analysis
Purpose: Analyze item performance and revenue  

Key KPIs:
- Total Revenue  
- Total Quantity Sold  
- Average Item Price  

Visualizations:
- Column Chart: Revenue by Category  
- Column Chart: Top Selling Items (by Quantity)  
- Column Chart: Item-wise Revenue  
- Pie Chart: Category Distribution  

Filters:
- Category  
- Item Name  
- Availability Status  

---

### Sheet 6: Payment Analysis
Purpose: Analyze payment trends and behavior  

Key KPIs:
- Total Payments  
- Successful Payments  
- Pending Payments  
- Failed Payments  

Visualizations:
- Pie Chart: Payment Method (Cash, UPI, Card)  
- Column Chart: Payment Status  
- Line Chart: Payment Trend Over Time  
- Column Chart: Revenue by Payment Method  

Filters:
- Payment Method  
- Payment Status  
- Date  

---

## Data Model Relationships (Critical)

Ensure the following relationships are properly configured:

- Customers.Customer_ID → Orders.Customer_ID  
- Customers.Customer_ID → Bookings.Customer_ID  
- Bookings.Booking_ID → Orders.Booking_ID  
- Orders.Order_ID → Order_Items.Order_ID  
- Menu.Item_ID → Order_Items.Item_ID  
- Orders.Order_ID → Payments.Order_ID  

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

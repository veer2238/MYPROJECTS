Zypher Women – Premium Clothing Sales Data Analysis and Customer Insights


SHEET 1: Executive Overview
Purpose: Overall business summary
KPIs:
* Total Revenue = SUM(Final_Amount)
* Total Orders = COUNT(Order_ID)
* Total Customers = DISTINCTCOUNT(Customer_ID)
* Average Order Value = Total Revenue / Total Orders
Visuals:
* Line chart: Revenue by Month-Year (Order_Date)
* Pie chart: Order Status (Completed, Cancelled, Returned)
* Bar chart: Revenue by Category
* Map: Revenue by State
Slicers:
* Order Date
* Category
* Customer Segment

SHEET 2: Customer Insights
Purpose: Understand customer demographics and behavior
KPIs:
* Total Customers
* New Customers (based on Signup_Date)
* Average Age
Visuals:
* Bar chart: Customers by State
* Pie chart: Customer Segment (New, Regular, VIP)
* Column chart: Age Distribution
* Line chart: Customers added over time (Signup_Date)
Additional:
* Table: Top Cities by number of customers

SHEET 3: Product Performance
Purpose: Analyze product sales and performance
KPIs:
* Total Products
* Average Product Price
* Top Category (by revenue)
Visuals:
* Bar chart: Revenue by Category
* Bar chart: Top 10 Products (by Total Sales)
* Column chart: Sales by Brand
* Treemap: Category and Subcategory
Calculated Metric:
* Profit = Price - Cost_Price

SHEET 4: Sales Analysis
Purpose: Detailed sales and revenue analysis
KPIs:
* Total Revenue
* Total Discount
* Final Revenue (after discount)
* Average Order Value
Visuals:
* Line chart: Monthly Revenue Trend
* Bar chart: Payment Method distribution
* Column chart: Orders by Shipping Type
* Stacked bar chart: Total Amount vs Discount Amount
Insight Focus:
* Monthly trends
* Impact of discounts

SHEET 5: Shipping Performance
Purpose: Evaluate delivery and logistics
KPIs:
* On-Time Delivery Percentage
* Average Delivery Time
* Return Rate
Visuals:
* Pie chart: Delivery Status (On-Time, Delayed, Failed)
* Bar chart: Courier Partner performance
* Column chart: Average Delivery Time by Courier
* Bar chart: Returns (Yes vs No)
Calculated Metric:
* Delivery Time = Delivery_Date - Shipping_Date

SHEET 6: Reviews and Sentiment Analysis
Purpose: Measure customer satisfaction
KPIs:
* Average Rating
* Total Reviews
* Positive Review Percentage
Visuals:
* Pie chart: Sentiment (Positive, Neutral, Negative)
* Bar chart: Rating distribution (1 to 5)
* Column chart: Average Rating by Category
* Bar chart: Top Reviewed Products
Additional:
* Table: Products with lowest ratings

FINAL STRUCTURE (VERY IMPORTANT)
Relationships to use:
* Customers → Orders → Order_Details
* Products → Order_Details
* Orders → Shipping
* Customers → Reviews
* Products → Reviews



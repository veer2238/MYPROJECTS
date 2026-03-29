E-COMMERCE POWER BI DASHBOARD PROJECT (MEN’S CLOTHING)

---

PROJECT OBJECTIVE:
Build a complete Power BI dashboard to analyze sales, customers, products, payments, returns, and inventory for an e-commerce business.

---

DATA TABLES USED:

1. Customers
2. Products
3. Orders
4. Order_Items
5. Payments
6. Returns
7. Inventory

---

PAGE 1: SALES OVERVIEW

KPIs:

* Total Revenue → SUM(total_amount)
* Total Orders → COUNT(order_id)
* Avg Order Value → SUM(total_amount) / COUNT(order_id)
* Total Customers → DISTINCTCOUNT(customer_id)

CHARTS:

1. Revenue Trend (Line Chart)

   * Axis: order_date
   * Values: SUM(total_amount)

2. Orders by Status (Donut Chart)

   * Legend: order_status
   * Values: COUNT(order_id)

3. Payment Mode Distribution (Pie Chart)

   * Legend: payment_mode
   * Values: COUNT(payment_id)

FILTERS:

* order_date
* payment_mode
* order_status

---

PAGE 2: PRODUCT PERFORMANCE

KPIs:

* Total Products Sold → SUM(quantity)
* Total Revenue → SUM(total_price)

CHARTS:

1. Top Products (Bar Chart)

   * Axis: product_name
   * Values: SUM(total_price)

2. Category-wise Sales

   * Axis: category
   * Values: SUM(total_price)

3. Brand Performance

   * Axis: brand
   * Values: SUM(total_price)

4. Size-wise Sales

   * Axis: size
   * Values: SUM(quantity)

FILTERS:

* category
* brand
* size

---

PAGE 3: CUSTOMER ANALYSIS

KPIs:

* Total Customers
* Repeat Customers (use DAX later)

CHARTS:

1. Customers by Country

   * Axis: country
   * Values: COUNT(customer_id)

2. New Customers Trend

   * Axis: signup_date
   * Values: COUNT(customer_id)

3. Top Customers (Table)

   * Columns: customer_id, SUM(total_amount)

FILTERS:

* country
* gender

---

PAGE 4: PAYMENT ANALYSIS

KPIs:

* Total Payments
* Failed Payments
* Success Rate

CHARTS:

1. Payment Status (Donut)

   * Legend: payment_status
   * Values: COUNT(payment_id)

2. Payment Method Revenue

   * Axis: payment_method
   * Values: SUM(amount)

3. Daily Payments Trend

   * Axis: payment_date
   * Values: SUM(amount)

FILTERS:

* payment_method
* payment_status

---

PAGE 5: RETURNS ANALYSIS

KPIs:

* Total Returns
* Total Refund Amount
* Return Rate

CHARTS:

1. Return Reasons (Bar Chart)

   * Axis: return_reason
   * Values: COUNT(return_id)

2. Refund Amount by Reason

   * Axis: return_reason
   * Values: SUM(refund_amount)

3. Return Rate by Product

   * Axis: product_id
   * Values: COUNT(return_id)

FILTERS:

* return_reason
* date

---

PAGE 6: INVENTORY DASHBOARD

KPIs:

* Total Stock → SUM(current_stock)
* Low Stock Count (filter < 20)

CHARTS:

1. Current Stock by Product

   * Axis: product_id
   * Values: SUM(current_stock)

2. Warehouse Stock

   * Axis: warehouse_location
   * Values: SUM(current_stock)

3. Low Stock Table

   * Columns: product_id, current_stock
   * Filter: current_stock < 20

FILTERS:

* warehouse_location

---

DATA MODEL RELATIONSHIPS:

* Customers → Orders (customer_id)
* Orders → Order_Items (order_id)
* Products → Order_Items (product_id)
* Orders → Payments (order_id)
* Order_Items → Returns (order_id + product_id)
* Products → Inventory (product_id)

---

FINAL QUESTIONS (FOR ANALYSIS):

1. Which product category generates highest revenue?
2. What is the return rate?
3. Which payment method is most successful?
4. Which warehouse has lowest stock?

---

## END OF PROJECT

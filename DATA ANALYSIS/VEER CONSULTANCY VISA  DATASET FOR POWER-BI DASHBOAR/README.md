#  Visa Application Dashboard (Data Analytics Project)

---

##  Project Overview

This project is a **complete data analytics solution** for a Visa Consultancy system.
It simulates real-world visa application workflows and builds a **Power BI dashboard** to analyze:

* Applications
* Approvals & Rejections
* Revenue (Payments)
* Document Verification
* Processing Time
* Country-wise trends

---

##  Objective

To design a **data-driven dashboard** that helps visa consultants:

* Track application status
* Monitor approval rates
* Analyze revenue streams
* Identify delays in processing
* Optimize decision-making

---

##  Data Architecture

This project uses a **relational data model** with multiple connected tables.

### Tables Used:

1. **Applicants**
2. **Visa Applications**
3. **Documents**
4. **Payments**
5. **Status History**
6. **Visa Rules (Countries)**

---

##  Data Model (Relationships)

* Applicants → Visa Applications (applicant_id)
* Visa Applications → Documents (application_id)
* Visa Applications → Payments (application_id)
* Visa Applications → Status History (application_id)
* Visa Applications → Visa Rules (country + visa_type)

---

##  Dataset Details

### 1. Applicants Table

Stores user details

* applicant_id
* full_name
* gender
* date_of_birth
* nationality
* passport_number
* email
* phone
* city
* country

---

### 2. Visa Applications Table

Tracks each visa request

* application_id
* applicant_id
* visa_type (Tourist, Work, Student, etc.)
* destination_country
* application_date
* travel_date
* duration_days
* application_status

---

### 3. Documents Table

Tracks document uploads

* document_id
* application_id
* document_type
* uploaded_date
* verification_status

---

### 4. Payments Table

Tracks revenue

* payment_id
* application_id
* amount
* payment_date
* payment_method
* payment_status

---

### 5. Status History Table

Tracks application lifecycle

* status_id
* application_id
* status (Submitted → Review → Approved/Rejected)
* updated_at

---

### 6. Visa Rules Table

Defines country-level logic

* country
* visa_type
* processing_time_days
* fee
* success_rate

---

##  Power BI Dashboard (6 Pages)

---

##  Page 1: Overview Dashboard

### KPIs:

* Total Applications
* Approved Applications
* Rejected Applications
* Approval Rate (%)
* Total Revenue

### Charts:

* Applications Over Time (Line Chart)
* Status Distribution (Donut Chart)
* Country-wise Applications (Bar Chart)

### Filters:

* Visa Type
* Country
* Date

---

##  Page 2: Application Analysis

### Charts:

* Applications by Visa Type
* Country-wise Approval Rate
* Monthly Trends

### Insights:

* Most popular visa type
* High demand countries

---

##  Page 3: Revenue Dashboard

### KPIs:

* Total Revenue
* Avg Payment per Application

### Charts:

* Revenue Trend
* Payment Method Distribution
* Revenue by Country

---

##  Page 4: Document Verification

### Charts:

* Document Status (Verified / Pending / Rejected)
* Document Type Distribution

### Insights:

* Bottlenecks in verification
* Most rejected documents

---

##  Page 5: Processing Time Analysis

### Charts:

* Avg Processing Time by Country
* Status Timeline

### Insights:

* Delay detection
* Country performance

---

##  Page 6: Approval vs Rejection

### Charts:

* Approval Rate by Country
* Approval Rate by Visa Type

### Insights:

* Best countries for visa success
* Risk analysis

---

##  Tools & Technologies

* Python (Data Generation)
* CSV (Dataset Storage)
* Power BI (Dashboard & Visualization)
* GitHub (Project Hosting)

---

##  How to Use

1. Download CSV files from folder
2. Open Power BI Desktop
3. Load all datasets
4. Create relationships (as defined above)
5. Build dashboard pages

---

##  Key Insights You Can Derive

* Which country has highest approval rate
* Which visa type has highest rejection
* Revenue trends over time
* Processing delays
* Document verification issues

---

##  Learning Outcomes

* Data Modeling (Relational Design)
* Data Cleaning & Structuring
* Dashboard Design (Power BI)
* Business KPI Analysis
* Real-world Project Simulation


---

##  Conclusion

This project demonstrates a **complete end-to-end data analytics workflow**:

👉 Data Generation → Data Modeling → Dashboard → Insights

It simulates a **real visa consultancy business system** and provides actionable insights for decision-making.

---



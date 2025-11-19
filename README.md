# 🛒 Customer Shopping Behavior Analysis  
**A complete end-to-end Data Analytics project using Python, SQL, and Power BI**

![Status](https://img.shields.io/badge/Project-Completed-brightgreen)
![Python](https://img.shields.io/badge/Python-3.10+-blue)
![PowerBI](https://img.shields.io/badge/PowerBI-Dashboard-yellow)
![SQL](https://img.shields.io/badge/PostgreSQL-Analysis-lightgrey)
![License](https://img.shields.io/badge/License-MIT-black)

---

## 📌 **Project Overview**

This project dives deep into the **shopping patterns of 3,900 customers** across various demographics, preferences, and product categories.  

The goal is to uncover insights that help businesses:  
✔ Understand what customers buy  
✔ Identify high-value segments  
✔ Evaluate discount effectiveness  
✔ Improve subscription strategies  
✔ Optimize product & marketing decisions  

The workflow is fully end-to-end:  
**Python → PostgreSQL (SQL Analysis) → Power BI Dashboard → Business Insights**

---

## 📂 **Dataset Summary**

**Total Records:** 3,900  
**Total Columns:** 18  

### **Key Features**
- **Customer Info:** Age, Gender, Location, Age Group, Subscription Status  
- **Shopping Behavior:** Frequency, Previous Purchases, Review Rating  
- **Purchase Info:** Category, Item Purchased, Price, Discount Applied, Season  
- **Operational Data:** Shipping Type, Promo Codes  

### **Data Quality**
- Missing Values: *37 in Review Rating*  
- Issues such as inconsistent formatting and redundant columns were resolved during cleaning.

---

## 🧹 **Data Preparation (Python)**

Performed using **Pandas, NumPy, Matplotlib, Seaborn**.

### ✔ Key Steps
- Imported and explored raw data (`df.info()`, `df.describe()`)
- Converted to readable formats (snake_case)
- Treated missing values using **median imputation by category**
- Engineered:
  - `age_group`  
  - `purchase_frequency_days`
- Removed redundant features (e.g., promo_code_used if discount_applied already exists)
- Loaded the cleaned dataset into **PostgreSQL** for further analysis

---

## 🗄️ **SQL Analysis (PostgreSQL)**

A total of **10+ business queries** were executed to generate meaningful insights.  
Here are the major analyses:

### 🔍 **Key Insights Extracted**
- **Revenue by Gender** — Identified top-spending segments  
- **High-Spending Discount Users** — Found discount users spending above average  
- **Top Rated Products** — Extracted highest-performing products  
- **Shipping Type Comparison** — Spending difference between Standard vs Express  
- **Subscription Impact** — Subscribers vs Non-Subscribers: spend & frequency  
- **Discount-Dependent Products** — Items frequently purchased with discounts  
- **Customer Segmentation** — Classified customers into:
  - *New*
  - *Returning*
  - *Loyal*
- **Top 3 Products per Category**  
- **Correlation between Repeat Buying & Subscriptions**  
- **Revenue by Age Group**

Each SQL query directly answers a real business question.

---

## 📊 **Power BI Dashboard**

An interactive dashboard was created to visualize key metrics:

### 🔸 Dashboard Includes:
- Revenue Breakdown  
- Customer Segments  
- Subscription Insights  
- Best-selling Products  
- Discount vs Non-discount Purchases  
- Age Group Revenue  
- Category & Seasonal Trends  

The dashboard simplifies decision-making and highlights impactful patterns.

---

## 🧠 **Business Recommendations**

Based on the insights:

1. **Boost Subscriptions**  
   Promote exclusive subscriber benefits to increase recurring revenue.

2. **Strengthen Loyalty Programs**  
   Reward returning customers to shift them into the *Loyal* category.

3. **Optimize Discount Strategy**  
   Avoid unnecessary discounts on products that sell well without them.

4. **Promote High-Rated Products**  
   Feature top-rated items in marketing campaigns.

5. **Target High-Revenue Age Groups**  
   Personalize campaigns for the most profitable segments.

6. **Leverage Express Shipping Users**  
   They often show higher purchase amounts—ideal for premium offers.

---

## 🧪 **Tech Stack**

| Area | Technologies Used |
|------|------------------|
| **Data Cleaning** | Python (Pandas, NumPy) |
| **Visualization** | Matplotlib, Seaborn, Power BI |
| **Database** | PostgreSQL |
| **Reporting** | Power BI Interactive Dashboard |
| **Version Control** | Git & GitHub |

---

## 📁 **Project Structure**
📦 customer-shopping-behavior-analysis
┣ 📂 data
┣ 📂 notebooks
┣ 📂 sql_queries
┣ 📂 powerbi_dashboard
┣ 📄 README.md
┣ 📄 requirements.txt
┗ 📄 main.py


---

## 🚀 How to Run This Project

```bash
# Clone the repository
git clone https://github.com/yourusername/yourrepo.git

# Navigate inside project
cd yourrepo

# Install dependencies
pip install -r requirements.txt

# Run analysis script
python main.py




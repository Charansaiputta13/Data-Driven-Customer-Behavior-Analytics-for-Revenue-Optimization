# 🛒 Data-Driven Customer Behavior Analytics for Revenue Optimization 
**A complete end-to-end Data Analytics project using Python, SQL, Streamlit, and Machine Learning**

![Status](https://img.shields.io/badge/Project-Upgraded-brightgreen)
![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red)
![SQL](https://img.shields.io/badge/PostgreSQL-Analysis-lightgrey)
![License](https://img.shields.io/badge/License-MIT-black)

---

## 📌 **Project Overview**

This project dives deep into the **shopping patterns of 3,900 customers** across various demographics, preferences, and product categories.  
It has been upgraded to an **Industry-Level Standard** with a modular code structure, a live interactive web dashboard, and machine learning capabilities.

### 🚀 **New Features**
- **Interactive Web Dashboard**: Built with Streamlit for real-time data exploration.
- **Machine Learning**: Customer segmentation using K-Means clustering.
- **Modular Codebase**: Clean, reusable Python modules in `src/`.

---

## 📂 **Project Structure**

```
customer-shopping-behavior-analysis
┣ 📂 data/                  # Raw data files
┃ ┗ 📄 customer_shopping_behavior.csv
┣ 📂 notebooks/             # Jupyter notebooks for experimentation
┃ ┗ 📄 Shopping_Behaviour_Analysis.ipynb
┣ 📂 sql/                   # SQL scripts
┃ ┗ 📄 customer_analysis.sql
┣ 📂 src/                   # Source code modules
┃ ┣ 📄 data_loader.py       # Data loading & cleaning
┃ ┣ 📄 analytics.py         # KPI calculations
┃ ┗ 📄 ml_models.py         # Machine Learning models
┣ 📄 app.py                 # Streamlit Dashboard Entry Point
┣ 📄 requirements.txt       # Project dependencies
┗ 📄 README.md              # Project Documentation
```

---

## 🚀 **How to Run This Project**

1.  **Clone the repository**
    ```bash
    git clone https://github.com/yourusername/yourrepo.git
    cd yourrepo
    ```

2.  **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the Dashboard**
    ```bash
    streamlit run app.py
    ```
    The app will open in your browser at `http://localhost:8501`.

---

## 📊 **Dashboard Features**

### 1. **Executive Overview**
- Real-time KPIs (Revenue, Avg Spend, Total Customers).
- Interactive charts for Revenue by Category and Gender.

### 2. **Deep Dive Analytics**
- Filter data by Gender and Category.
- Analyze Subscription impact on spending.
- View Customer Age distribution.

### 3. **ML Insights (Clustering)**
- **K-Means Clustering** to identify distinct customer segments.
- 3D Visualization of clusters based on Spend, Frequency, and Rating.

---

## 🧠 **Business Recommendations**

Based on the insights:

1. **Boost Subscriptions**: Promote exclusive subscriber benefits to increase recurring revenue.
2. **Strengthen Loyalty Programs**: Reward returning customers to shift them into the *Loyal* category.
3. **Optimize Discount Strategy**: Avoid unnecessary discounts on products that sell well without them.
4. **Target High-Revenue Age Groups**: Personalize campaigns for the most profitable segments.

---

## 🧪 **Tech Stack**

| Area | Technologies Used |
|------|------------------|
| **App Framework** | Streamlit |
| **Data Processing** | Pandas, NumPy |
| **Visualization** | Plotly, Matplotlib, Seaborn |
| **Machine Learning** | Scikit-Learn (K-Means) |
| **Database** | PostgreSQL (SQL Scripts included) |


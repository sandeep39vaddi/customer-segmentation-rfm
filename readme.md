# 📊 Customer Segmentation using RFM Analysis

## 📌 Overview

This project performs customer segmentation using RFM (Recency, Frequency, Monetary) analysis to identify high-value, loyal, and at-risk customers for targeted business strategies.

---

## 🎯 Objectives

* Segment customers based on purchasing behavior
* Identify high-value and loyal customers
* Detect at-risk customers for retention strategies
* Provide actionable business insights

---

## 🛠️ Tools Used

* Python (Pandas, Matplotlib)
* Data Cleaning & Feature Engineering
* RFM Analysis

---

## 📂 Dataset

* Superstore Sales Dataset (~10K records)
* Includes customer transactions, sales, and order details

---

## ⚙️ Methodology

* Calculated:

  * **Recency** → Days since last purchase
  * **Frequency** → Number of purchases
  * **Monetary** → Total spending

* Assigned RFM scores using quartiles

* Combined scores to create customer segments

---

## 🔍 Customer Segments

* 🏆 Champions → High value, frequent buyers
* 🔁 Loyal Customers → Regular repeat customers
* 📈 Potential Loyalists → Can become loyal
* ⚠️ At Risk → Customers likely to churn
* Others → Average customers

---

## 📊 Visualizations

### Customer Segment Distribution

![Segments](images/customer_segments.png)

### Revenue by Segment

![Revenue](images/revenue_by_segment.png)

### Frequency vs Monetary

![Scatter](images/frequency_vs_monetary.png)

---

## 🔥 Key Insights

* Champions contribute the highest revenue
* Loyal customers show consistent purchase behavior
* At-risk customers have low recency (inactive recently)
* Potential loyalists can be targeted for conversion

---

## 💡 Business Recommendations

* Focus marketing campaigns on potential loyalists
* Retarget at-risk customers with offers
* Reward champions with loyalty programs
* Improve engagement strategies for low-frequency users

---

## ▶️ How to Run

1. Install libraries:
   pip install pandas matplotlib

2. Run:
   python notebook/rfm_analysis.py

---

## 📁 Project Structure

P2_CUSTOMER_SEGMENTATION/
│── data/
│── notebook/
│── images/
│── README.md

---

## 📌 Conclusion

This project demonstrates how customer segmentation can help businesses improve retention, optimize marketing strategies, and increase revenue.

---

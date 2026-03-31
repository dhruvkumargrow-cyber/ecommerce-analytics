# Business Recommendations — Olist E-Commerce Analytics
**Analyst:** Dhruv Kumar  
**Dataset:** Brazilian E-Commerce (Olist) — 110,120 transactions, R$19.7M revenue  
**Period:** 2016–2018  

---

## Executive Summary
Analysis of 96,413 delivered orders across Brazil reveals significant opportunities 
in regional expansion, category focus, logistics optimization, and customer retention. 
The following 6 data-backed recommendations are projected to improve revenue, 
customer satisfaction, and operational efficiency.

---

## Recommendation 1 — Double Down on São Paulo and Rio de Janeiro
**Data Finding:**
SP and RJ together account for ~45% of total revenue and have the 
fastest average delivery times (<10 days).

**Recommendation:**
Increase seller acquisition, marketing spend, and promotional campaigns 
in SP and RJ before expanding to lower-performing states.

**Expected Impact:**
- 15-20% revenue increase from top 2 states
- Higher review scores due to faster delivery
- Lower customer acquisition cost (existing demand)

---

## Recommendation 2 — Prioritize Bed & Bath and Health & Beauty Categories
**Data Finding:**
Bed & Bath Table and Health & Beauty are the top 2 revenue-generating 
categories, consistently outperforming all others across the 2016-2018 period.

**Recommendation:**
- Increase seller onboarding in these 2 categories
- Run targeted promotions during peak months (Nov-Dec)
- Create dedicated category pages to improve discoverability

**Expected Impact:**
- 10-15% category revenue growth
- Improved average order value (higher priced items in these categories)

---

## Recommendation 3 — Fix Logistics in Low-Performing States
**Data Finding:**
States like RO, AM, AC, and AP have average delivery times exceeding 
20 days — nearly double the national average of 11.9 days. These states 
also show the lowest review scores (below 3.8/5).

**Recommendation:**
- Partner with regional logistics providers in North and Northeast Brazil
- Set up regional distribution centers in Manaus (AM) and Belém (PA)
- Offer delivery time guarantees with compensation for delays

**Expected Impact:**
- Review scores in affected states improve from 3.8 to 4.2+
- 8-12% reduction in order cancellations
- Higher repeat purchase rate in currently underserved regions

---

## Recommendation 4 — Leverage Credit Card Dominance for Revenue Growth
**Data Finding:**
74% of customers pay by credit card. Boleto (bank slip) accounts for 
~19% but has a higher abandonment rate and lower average order value.

**Recommendation:**
- Introduce credit card installment plans (2-6x) for orders above R$200
- Offer 5% cashback for credit card payments on selected categories
- Reduce boleto payment window from 3 days to 1 day to reduce abandonment

**Expected Impact:**
- 8-10% increase in average order value
- Reduced payment abandonment rate
- Higher customer lifetime value through installment purchases

---

## Recommendation 5 — Schedule Promotions During Peak Hours
**Data Finding:**
Order volume peaks sharply between 10AM and 4PM, with the highest 
concentration at 2PM-3PM. Order volume drops significantly after 8PM.

**Recommendation:**
- Schedule flash sales and promotional emails between 10AM-2PM
- Push mobile app notifications at 11AM and 1PM
- Run "Happy Hour" deals from 2PM-4PM on weekdays

**Expected Impact:**
- 12-15% increase in conversion rate during peak hours
- Higher ROI on marketing spend (targeting proven high-intent window)
- Reduced server load by smoothing order distribution

---

## Recommendation 6 — Address 1-Star and 2-Star Reviews Proactively
**Data Finding:**
While the average review score is 4.08/5, approximately 11% of orders 
receive 1 or 2 star reviews. These negative reviews are concentrated in 
categories with longer delivery times and in Northern states.

**Recommendation:**
- Implement automated post-delivery follow-up for orders with delivery 
  time > 15 days
- Create a proactive refund/discount system for delayed orders before 
  customers leave negative reviews
- Flag sellers with consistent low ratings for quality review

**Expected Impact:**
- Average review score improves from 4.08 to 4.3+
- 15-20% reduction in 1-star reviews
- Improved platform reputation and seller accountability

---

## Summary of Recommendations

| Priority | Recommendation | Expected Revenue Impact |
|----------|---------------|------------------------|
| 1 | Focus on SP & RJ markets | +15-20% |
| 2 | Prioritize top 2 categories | +10-15% |
| 3 | Fix logistics in North Brazil | +8-12% |
| 4 | Credit card installment plans | +8-10% |
| 5 | Peak hour promotions | +12-15% |
| 6 | Proactive review management | Retention +15% |

---

## Methodology
- Data cleaned and transformed using Python (Pandas)
- 110,120 delivered orders analyzed after removing cancelled/invalid records
- Visualized using Microsoft Power BI (4-page interactive dashboard)
- Dataset: Brazilian E-Commerce Public Dataset by Olist (Kaggle)
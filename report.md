# Trader Performance vs Market Sentiment Report

## 1. Objective
To study how trader performance varies with market sentiment and identify behavioral patterns.

---

## 2. Data Preparation
- Loaded historical trading data and sentiment data  
- Removed duplicates  
- Converted timestamps  
- Handled missing values  
- Merged datasets using date  

---

## 3. Feature Engineering
- Daily PnL  
- Trades per day  
- Win rate  
- Leverage segments  
- Trader consistency  

---

## 4. Segmentation
- High vs Low Leverage Traders  
- Frequent vs Infrequent Traders  
- Consistent vs Inconsistent Traders  

---

## 5. Clustering
KMeans clustering grouped traders into 3 behavior clusters.

---

## 6. Key Insights
1. High leverage traders show higher volatility and losses.  
2. Consistent traders achieve higher average PnL.  
3. Fear days reduce profitability for aggressive traders.  

---

## 7. Actionable Strategies
- Reduce leverage during Fear sentiment.  
- Increase trades only for consistent profitable traders.

---

## 8. Conclusion
Market sentiment significantly impacts trader behavior and profitability.

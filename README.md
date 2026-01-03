# 🚀 Cryptocurrency Volatility Prediction

This project is an end-to-end Machine Learning application that predicts short-term cryptocurrency market volatility using historical price and market data.  
The model is trained using Random Forest and deployed as a live web application using Streamlit Cloud.

---

## 📌 Project Overview

Cryptocurrency markets are highly volatile, making risk assessment difficult for traders and investors.  
This project aims to predict volatility based on historical OHLC prices, trading volume, and market capitalization.

The complete pipeline includes:
- Data preprocessing
- Feature engineering
- Model training and evaluation
- Feature importance analysis
- Cloud deployment

---

## 🧠 Machine Learning Approach

### Models Used
- **Linear Regression** (Baseline)
- **Random Forest Regressor** (Final Model)

Random Forest was selected due to its superior performance in capturing non-linear patterns in volatile financial data.

### Evaluation Metrics
- RMSE (Root Mean Squared Error)
- MAE (Mean Absolute Error)
- R² Score

---

## 🧪 Feature Engineering

The following features were engineered to improve model performance:
- High–Low price spread
- Close–Open price spread
- Liquidity ratio (Volume / Market Capitalization)
- Rolling volatility measures

Feature importance analysis showed that price range and liquidity-based features were the most influential.

---

## 🌐 Live Deployment

The trained model has been deployed online using **Streamlit Cloud**.

🔗 **Live App URL:**  
👉 https://crypto-volatility-app-kryudkex96jkjgr6egvgxp.streamlit.app/

Users can input market parameters and instantly receive predicted volatility values.

---

## 🛠️ Tech Stack

- Python
- Pandas, NumPy
- Scikit-learn
- Joblib
- Streamlit
- GitHub
- Streamlit Cloud


## 📁 Repository Structure


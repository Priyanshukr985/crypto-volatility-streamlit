
![GitHub repo size](https://img.shields.io/github/repo-size/Priyanshukr985/crypto-volatility-streamlit)
![GitHub stars](https://img.shields.io/github/stars/Priyanshukr985/crypto-volatility-streamlit?style=social)
![GitHub forks](https://img.shields.io/github/forks/Priyanshukr985/crypto-volatility-streamlit?style=social)


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

<img width="922" height="876" alt="image" src="https://github.com/user-attachments/assets/49481a1c-0577-4f2d-832e-b9327d3823dd" />


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

## crypto-volatility-streamlit

Cryptocurrency-Volatility-Prediction-using-Machine-Learning.pdf #ppt

Final_Report_Cryptocurrency_Volatility_Prediction.pdf # final report

HLD_LLD_and_Pipeline_Architecture.pdf # HLD + LLD + Pipeline

ML_Project_crypto.ipynb # Source code

app.py # streamlit application

requirements.txt # Project dependencies

rf_volatility_model.pkl # # Trained ML model

README.md # Project documentation





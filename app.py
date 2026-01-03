import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("rf_volatility_model.pkl")

st.title("Cryptocurrency Volatility Prediction")

st.write("Enter market details to predict volatility")

open_price = st.number_input("Open Price", min_value=0.0)
high_price = st.number_input("High Price", min_value=0.0)
low_price = st.number_input("Low Price", min_value=0.0)
close_price = st.number_input("Close Price", min_value=0.0)
volume = st.number_input("Volume", min_value=0.0)
market_cap = st.number_input("Market Capitalization", min_value=0.0)

# Feature engineering
hl_spread = high_price - low_price
co_spread = close_price - open_price
liquidity_ratio = volume / (market_cap + 1)

# Create input dataframe
input_data = pd.DataFrame([[
    open_price, high_price, low_price, close_price,
    volume, market_cap,
    hl_spread, co_spread, liquidity_ratio
]], columns=[
    'open','high','low','close',
    'volume','marketCap',
    'hl_spread','co_spread','liquidity_ratio'
])

if st.button("Predict Volatility"):
    prediction = model.predict(input_data)[0]
    st.success(f"Predicted Volatility: {prediction:.4f}")

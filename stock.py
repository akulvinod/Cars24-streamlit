import streamlit as st
import yfinance as yf
import datetime

st.title("Stock Price Analyzer!")
st.subheader("Get the latest stock price for your favorite company!")


company = st.text_input("Enter the stock ticker symbol (e.g., AAPL, MSFT):", "MSFT")
ticker = yf.Ticker(company)

col1, col2= st.columns(2)
with col1:
    sd = st.date_input("Start date", datetime.date(2025, 1, 1))
with col2:
    ed = st.date_input("End date", datetime.date(2026, 3, 31))


ticker_data = ticker.history(start = sd, end = ed) # historical price.

st.write(f"Here is the historical price data for {ticker.ticker}:")
st.dataframe(ticker_data.head())

st.subheader("Price movement over time:")
st.line_chart(ticker_data["Close"])

st.subheader("Volume traded over time:")
st.bar_chart(ticker_data["Volume"])
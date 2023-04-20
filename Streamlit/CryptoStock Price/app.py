import streamlit as st
import pandas as pd
import numpy as np 
import yfinance as yf
from datetime import date

st.write('''
# Simple Stock Price App
This is simple webapp to shows **closing price** and ***volume*** of Google (API)!
''')

#define symbols:

symbls = ("GOOGL", "BTC-USD", "ADA-USD", "SAND-USD", "ETH-USD")

option = st.selectbox(
    'pls select on of your coins', symbls
    )

tricker = yf.Ticker(option)

trickerDF = tricker.history(period="1d", start = '2012-01-01', end = date.today())

# you can choose on of: Open, High, Low, Close✅, Volume✅, Dividends, Stock Splits

st.write("""
## Highest Price
""")
st.line_chart(trickerDF.High)

st.write("the last price is:", trickerDF.sort_values(by='Date', ascending=False))

# st.text("the last price for now is:", trickerDF.sort_values(by='Date', ascending=False))

# trickerDF['Date'] = pd.to_datetime(trickerDF['Date'])
last_price = trickerDF['High'].iloc[-1]
st.info(f"The last (High) price for today is: {last_price} $")
#st.text("the last price for now is:", trickerDF.iloc[-1].price)

st.write("""
## Volume Price
""")
st.line_chart(trickerDF.Volume)


import streamlit as st
import config
from utils.data_loader import fetch_historical  # <-- fixed import

st.set_page_config(page_title="Nifty Strategy Backtest", layout="wide")

# Always render this
st.title("📊 Nifty Strategy Backtest")
st.write("This is a test to confirm Streamlit UI is working.")

symbol = config.NIFTY_SYMBOL

try:
    df = fetch_historical(symbol, config.FROM_DATE, config.TO_DATE, config.TIMEFRAME)
    st.success(f"Fetched {len(df)} rows for {symbol}")
    st.dataframe(df.head())
    st.line_chart(df["close"])
except Exception as e:
    st.error(f"Error fetching data: {e}")

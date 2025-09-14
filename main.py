import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

from utils.data_loader import fetch_historical
from utils.inidcators import calculate_atr, calculate_adx
from strategies.long_entry import check_entry
from strategies.exit_rules import simulate_exit
from strategies.position_sizing import get_lots
import config


# Load Data via Zerodha API

st.title("📊 Nifty Strategy Backtest (Zerodha API)")

with st.spinner("Fetching data from Zerodha..."):
    nifty = fetch_historical(config.NIFTY_SYMBOL, config.FROM_DATE, config.TO_DATE, config.TIMEFRAME)
    banknifty = fetch_historical(config.BANKNIFTY_SYMBOL, config.FROM_DATE, config.TO_DATE, config.TIMEFRAME)
    vix = fetch_historical(config.VIX_SYMBOL, config.FROM_DATE, config.TO_DATE, "day")["close"]

# Indicators
nifty['ATR'] = calculate_atr(nifty)
nifty['ADX'] = calculate_adx(nifty)


# Backtest

trades = []
for i in range(len(nifty)):
    if check_entry(nifty, banknifty, vix, i):
        atr = nifty['ATR'].iloc[i]
        lots = get_lots(atr)
        entry_price = nifty['close'].iloc[i]
        entry_time = nifty.index[i]

        exit_trade = simulate_exit(entry_price, atr, nifty, i, lots * config.LOT_SIZE)

        trades.append({
            "entry_time": entry_time,
            "entry_price": entry_price,
            "lots": lots,
            "exit_time": exit_trade["exit_time"],
            "exit_price": exit_trade["exit_price"],
            "reason": exit_trade["reason"],
            "pnl": (exit_trade["exit_price"] - entry_price) * exit_trade["lots"]
        })

df_trades = pd.DataFrame(trades)


# Dashboard

if not df_trades.empty:
    total_pnl = df_trades['pnl'].sum()
    win_rate = (df_trades['pnl'] > 0).mean() * 100
    avg_pnl = df_trades['pnl'].mean()

    st.metric("Total PnL", f"{total_pnl:.2f}")
    st.metric("Win Rate", f"{win_rate:.2f}%")
    st.metric("Average Trade PnL", f"{avg_pnl:.2f}")

    st.subheader("📋 Trade Log")
    st.dataframe(df_trades)

    st.subheader("📈 Equity Curve")
    df_trades['cum_pnl'] = df_trades['pnl'].cumsum()
    fig, ax = plt.subplots(figsize=(10,4))
    ax.plot(df_trades['exit_time'], df_trades['cum_pnl'], marker='o')
    ax.set_title("Cumulative PnL Over Time")
    ax.set_ylabel("PnL")
    ax.grid(True)
    st.pyplot(fig)
else:
    st.warning("⚠️ No trades triggered in the dataset.")

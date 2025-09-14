def simulate_exit(entry_price, atr, df, i, lots):
    partial_target = entry_price + 1.5 * atr
    trailing_sl = entry_price - 0.75 * atr

    for j in range(i+1, len(df)):
        high = df['high'].iloc[j]
        low = df['low'].iloc[j]
        dt = df.index[j]

        if high >= partial_target:
            return {
                "exit_price": partial_target,
                "exit_time": dt,
                "lots": lots // 2,
                "reason": "Target"
            }

        if low <= trailing_sl:
            return {
                "exit_price": trailing_sl,
                "exit_time": dt,
                "lots": lots,
                "reason": "SL"
            }

    return {
        "exit_price": df['close'].iloc[-1],
        "exit_time": df.index[-1],
        "lots": lots,
        "reason": "EOD"
    }

def check_entry(nifty_df, bank_df, vix_series, i):
    if i < 2:
        return False

    nifty_curr, nifty_prev = nifty_df.iloc[i], nifty_df.iloc[i-1]
    bank_curr, bank_prev = bank_df.iloc[i], bank_df.iloc[i-1]

    if (
        nifty_curr['high'] > nifty_prev['high']
        and bank_curr['high'] > bank_prev['high']
        and nifty_curr['volume'] > 1.5 * nifty_df['volume'].iloc[i-5:i].mean()
        and nifty_df['ADX'].iloc[i] > 25
        and vix_series.loc[nifty_curr.name.date()] > 18
    ):
        return True
    return False

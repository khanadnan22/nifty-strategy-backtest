# ==========================
# Zerodha Configurations
# ==========================

import datetime

API_KEY = "itxixp0mulvuarbv"
API_SECRET = "o0nz5mttuwdzpg77oavfivrr39n2io96"

# Do NOT keep access token here (it expires daily).
# It will be stored in access_token.txt after you run generate_access_token.py

# Correct Zerodha tradingsymbols
NIFTY_SYMBOL = "NIFTY 50"
BANKNIFTY_SYMBOL = "NIFTY BANK"
VIX_SYMBOL = "INDIA VIX"

# Lot size for options
LOT_SIZE = 50

# Historical data timeframe
TIMEFRAME = "15minute"
FROM_DATE = datetime.date(2025, 8, 1)
TO_DATE = datetime.date(2025, 9, 9)

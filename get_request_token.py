from kiteconnect import KiteConnect

# Your API key and secret from Zerodha developer console
api_key = "itxixp0mulvuarbv"

kite = KiteConnect(api_key=api_key)

# Print login URL
print("Login to your Zerodha account using this URL:")
print(kite.login_url())

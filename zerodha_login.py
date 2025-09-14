from kiteconnect import KiteConnect

# Your API key and secret
api_key = "itxixp0mulvuarbv"
api_secret = "o0nz5mttuwdzpg77oavfivrr39n2io96"

kite = KiteConnect(api_key=api_key)

# 🔹 Replace this request_token with the one you get after login
request_token = "1h3CepyoatQgpCzw7Np7Wu0wzoLoX82H"

# Generate access token
try:
    data = kite.generate_session(request_token, api_secret=api_secret)
    access_token = data["access_token"]

    # Save access token in a file
    with open("access_token.txt", "w") as f:
        f.write(access_token)

    print("Access Token generated and saved successfully:", access_token)

except Exception as e:
    print("Error generating access token:", e)

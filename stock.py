import yfinance as yf

stocks = ["AAPL", "NVDA", "MSFT", "TSLA"]

for s in stocks:
    data = yf.download(s, period="5d")
    print(s, data["Close"].iloc[-1])
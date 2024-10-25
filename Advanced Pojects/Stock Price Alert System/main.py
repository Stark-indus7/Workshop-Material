# This project tracks stock prices and sends alerts when certain thresholds are met.
# Implement the code here

import yfinance as yf
import smtplib

def check_stock_price(stock_symbol, alert_price):
    stock = yf.Ticker(stock_symbol)
    current_price = stock.history(period='1d')['Close'][0]
    
    if current_price > alert_price:
        send_alert_email(stock_symbol, current_price)

def send_alert_email(stock_symbol, current_price):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('your_email@gmail.com', 'your_password')
    
    subject = f"Stock Price Alert: {stock_symbol}"
    body = f"The price of {stock_symbol} is now {current_price}"
    message = f"Subject: {subject}\n\n{body}"
    
    server.sendmail('your_email@gmail.com', 'recipient_email@gmail.com', message)
    server.quit()

# Example usage
check_stock_price('AAPL', 150)

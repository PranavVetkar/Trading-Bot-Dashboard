import streamlit as st
import pandas as pd
import sqlite3
import time

st.set_page_config(page_title="Crypto Bot Dashboard", layout="wide")
st.title("📈 Live BTC/USDT Trading Dashboard")

def get_data():
    conn = sqlite3.connect("crypto_trading.db")
    df = pd.read_sql_query("SELECT * FROM price_history ORDER BY id DESC LIMIT 50", conn)
    conn.close()
    return df

placeholder = st.empty()

while True:
    df = get_data()
    
    with placeholder.container():
        col1, col2 = st.columns(2)
        current_price = df['price'].iloc[0]
        avg_price = df['price'].mean()
        
        col1.metric("Current Price", f"${current_price:,.2f}")
        col2.metric("Avg (Last 50 Ticks)", f"${avg_price:,.2f}")
        
        st.line_chart(df.set_index('timestamp')['price'].iloc[::-1])
        
        st.write("Recent Ticks", df.head(10))
        
    time.sleep(1)
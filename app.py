#STREAMLIT APP
import streamlit as st
import pandas as pd

df = pd.read_csv("processed_data.csv")

st.title("Trader Performance vs Market Sentiment")

st.subheader("Average PnL")
st.bar_chart(df.groupby("classification")["Closed PnL"].mean())

st.subheader("Trades per Day")
st.bar_chart(df.groupby("classification")["trades_per_day"].mean())

st.subheader("Win Rate")
st.bar_chart(df.groupby("classification")["win"].mean())

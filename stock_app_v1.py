import pandas as pd
import streamlit as st
import yfinance as yf

st.title("Finance dashboard")

tickers=('TSLA','AAPL')

dropdown=st.multiselect("Pick your asset",tickers)

start=st.date_input('Start',value=pd.to_datetime('2022-01-01'))
end=st.date_input('End',value=pd.to_datetime('today'))

if len(dropdown)>0:
    df=yf.download(dropdown,start,end)['Adj Close']
    st.line_chart(df)
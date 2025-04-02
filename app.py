import matplotlib.pyplot as plt 
import yfinance as yf   
import streamlit as st

start = '2010-01-01'
end = '2025-03-03'

st.title('Stock Trend Prediction')

user_input = st.text_input(
    'Enter Stock Ticker',
    placeholder='e.g., AAPL, GOOGL, MSFT',
    help='Enter the stock symbol/ticker of the company you want to analyze'
)

if user_input:  # Only fetch data if user has entered ticker
    try:
        # Show data fetch details
        st.sidebar.subheader("Data Fetch Details")
        st.sidebar.write(f"Requesting data for: {user_input}")
        st.sidebar.write(f"Start date: {start}")
        st.sidebar.write(f"End date: {end}")
        
        # Get data from yfinance
        df = yf.download(user_input, start=start, end=end)
        
        # Show response details
        st.sidebar.subheader("Data Details")
        st.sidebar.write("Data Shape:", df.shape)
        st.sidebar.write("Latest Data Point:", df.head(1))
        
    except Exception as e:
        st.error(f"Error fetching data: {e}")
    else:
        if df.empty:
            st.error('No data found for ticker symbol. Please check the symbol and try again.')
        else:
            # Continue with processing the data
            st.subheader('Data from 2010-2022')
            st.write(df.describe())

            #Visualization
            st.subheader('Closing Price vs Time Chart')
            fig = plt.figure(figsize = (12,6))
            plt.plot(df.Close)
            st.pyplot(fig)

            st.subheader('Closing Price vs Time Chart with 100MA')
            ma100 = df.Close.rolling(100).mean()
            fig = plt.figure(figsize = (12,6))
            plt.plot(ma100)
            plt.plot(df.Close)
            plt.legend()
            st.pyplot(fig)

            st.subheader('Closing Price vs Time Chart with 100MA & 200MA')
            ma100 = df.Close.rolling(100).mean()
            ma200 = df.Close.rolling(200).mean()
            fig = plt.figure(figsize = (12,6))
            plt.plot(ma100, 'r', label = 'MA100')
            plt.plot(ma200, 'g', label = 'MA200')
            plt.plot(df.Close, 'b', label = 'Original Price')

            plt.legend()
            st.pyplot(fig)

            
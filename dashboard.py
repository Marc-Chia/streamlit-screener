import streamlit as st
import time
from screener import ross_cameron_screener

# Title
st.title("Small-Cap High Momentum Screener")

# Refresh interval (in seconds)
refresh_interval = 60  # Adjust the interval as needed

# Fetch data
results = ross_cameron_screener(use_simulated=False)

# Display results
st.write("High Momentum Stocks:")
st.table(results)

# Automatic refresh
time.sleep(refresh_interval)
st.experimental_rerun()

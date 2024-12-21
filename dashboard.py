import streamlit as st
from screener import ross_cameron_screener

# Title
st.title("Small-Cap High Momentum Screener")

# Screener Button
if st.button("Run Screener"):
    st.write("Fetching data... This may take a few seconds.")
    results = ross_cameron_screener(use_simulated=True)

    if results:
        st.write("High Momentum Stocks:")
        st.table(results)  # Display as a table

        # Visualization: Line Chart for Example Stock
        example_stock = results[0] if results else None
        if example_stock:
            st.write(f"Price trend for {example_stock['Ticker']}:")
            # Simulated chart data for visualization
            chart_data = {
                "Price": [example_stock["Price"] - i * 0.5 for i in range(10)],
                "Volume": [example_stock["Volume"] + i * 1000 for i in range(10)],
            }
            st.line_chart(chart_data)
    else:
        st.write("No momentum stocks found.")

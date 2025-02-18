import streamlit as st
import pandas as pd
import numpy as np


# st.write("Line chart for random data")
# chart_data = pd.DataFrame(
   # np.random.randn(20, 2),
   # columns=['a', 'b','c'])

#st.line_chart(chart_data)

st.write("Map for random data")
map_data = pd.DataFrame(
               np.random.randn(1000,1) / [50, 50] + [37.76, -122.4],
               columns=['lat', 'lon'])

st.map(map_data)

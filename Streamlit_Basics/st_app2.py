import streamlit as st
import numpy as np
import pandas as pd

#st.write("Dataframe for random numbers with Highlighted Values")
st.write("Generated Table for Random Numbers")
dataframe = pd.DataFrame(
               np.random.rand(10,20),
               columns=('col%d' % i for i in range(20))
      )  

#st.dataframe(dataframe.style.highlight_max(axis=0))
st.table(dataframe)
# jupyter nbconvert --to script Streamlit.ipynb
# pip install streamlit

import streamlit as st
import pandas as pd
import numpy as np

if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    chart_data

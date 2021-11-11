# jupyter nbconvert --to script Streamlit.ipynb
# pip install streamlit

import streamlit as st
import pandas as pd
import numpy as np

left_column, right_column = st.columns(2)
# You can use a column just like st.sidebar:
left_column.button('Press me!')

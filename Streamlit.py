# jupyter nbconvert --to script Streamlit.ipynb
# pip install streamlit

import streamlit as st
import pandas as pd
import numpy as np

x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)

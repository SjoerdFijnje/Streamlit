# jupyter nbconvert --to script Streamlit.ipynb
# pip install streamlit

import streamlit as st
import pandas as pd
import numpy as np

st.text_input("Your name", key="name")

# You can access the value at any point with:
st.session_state.name

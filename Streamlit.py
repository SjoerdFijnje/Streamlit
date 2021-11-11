#!/usr/bin/env python
# coding: utf-8

# jupyter nbconvert --to script Streamlit.ipynb
# pip install streamlit

import streamlit as st
import pandas as pd
import numpy as np

'Dit is een stukje tekst :)'

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)

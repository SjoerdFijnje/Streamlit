#!/usr/bin/env python
# coding: utf-8

# In[31]:


# jupyter nbconvert --to script Streamlit.ipynb


# In[32]:


# pip install streamlit


# In[2]:


import streamlit as st
import pandas as pd
import numpy as np


# In[3]:


chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)


# In[ ]:





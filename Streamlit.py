#!/usr/bin/env python
# coding: utf-8

# In[31]:


# jupyter nbconvert --to script Streamlit.ipynb


# In[32]:


# pip install streamlit


# In[33]:


import streamlit as st


# In[34]:


import pandas as pd

st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))


# In[ ]:





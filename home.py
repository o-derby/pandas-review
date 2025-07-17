import streamlit as st
import pandas as pd

st.header('Welcome to the Pandas Review')
st.subheader('Select What To Review:')

if st.button('Table Manipulation'):
    st.switch_page('pages/table-home.py')
if st.button('Data Visualization'):
    st.switch_page('pages/visualization-visualization-home')
if st.button('Regression Models'):
    st.switch_page('pages/regression/regression-home')

# table = pd.DataFrame({'Greeting': ['hi', 'yo', 'hello', 'hey'], 'Place': ['home', 'park', 'class', 'there']})
# table.set_index('Place', inplace=True)
# table
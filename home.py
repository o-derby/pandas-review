import streamlit as st
import pandas as pd

if 'page' not in st.session_state:
    st.session_state.page = 'home'

if 'last' not in st.session_state:
    st.session_state.last = 'home'

def go_to(name):
    st.session_state.last = st.session_state.page
    st.session_state.page = name
    st.rerun()

def back_home():
    col1, col2 = st.columns([1, 1])

    with col1:
        if st.button('Back'):
            go_to(st.session_state.last)
    with col2:
        if st.button('Home'):
            go_to('home')


def home():
    st.header('Welcome to the Pandas Review')
    st.subheader('Select What To Review:')

    if st.button('Table Manipulation'):
        go_to('tbl_home')
    if st.button('Data Visualization'):
        go_to('vis_home')
    if st.button('Regression Models'):
        go_to('reg_home')

def tbl_home():
    back_home()
    st.header('Review Table Manipulation')
    st.subheader('Select What To Review:')

def vis_home():
    back_home()
    st.header('Review Data Visualization')
    st.subheader('Select What To Review:')

def reg_home():
    back_home()
    st.header('Review Regression Models')
    st.subheader('Select What To Review:')

if st.session_state.page == 'home':
    home()
elif st.session_state.page == 'tbl_home':
    tbl_home()
elif st.session_state.page == 'vis_home':
    tbl_home()
elif st.session_state.page == 'reg_home':
    tbl_home()

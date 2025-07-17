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
    st.subheader('Select What Level To Review:')

    if st.button('Level 1: Basic Selection'):
        go_to('tbl_level1')

def vis_home():
    back_home()
    st.header('Review Data Visualization')
    st.subheader('Select What Level To Review:')

def reg_home():
    back_home()
    st.header('Review Regression Models')
    st.subheader('Select What Level To Review:')

def tbl_level1():
    back_home()
    st.header('Level 1: Basic Selection')
    st.markdown('You are given the following DataFrame (df):')

    sample_df = pd.DataFrame({'Name': ['Oski', 'Cal', 'Bear'], 'Score': [99, 93, 95]})
    st.dataframe(sample_df)

    st.markdown('How do you get the score of the second row?')

    options = {
        'A': "df.loc[1, 'Score']",
        'B': "df.iloc[1, 'Score']",
        'C': "df.iloc[2, 'Score']",
        'D': "df.loc[2]['Score']"
    }

    answer = st.radio('Select the answer below:', list(options.keys()), format_func=lambda x: options[x], index=None, key='tbl_level1_answer')

    if answer != None:
        if st.button('Submit Answer'):
            if answer == 'A':
                st.success("Correct! '.loc' uses label indexing, and index 1 refers to the second row.")
                if st.button('Next Level'):
                    go_to('tbl_level2')

            else:
                st.error("Not quite... Remember that '.loc' uses labels while '.iloc' uses indexs (positions)")
        

if st.session_state.page == 'home':
    home()
elif st.session_state.page == 'tbl_home':
    tbl_home()
elif st.session_state.page == 'vis_home':
    vis_home()
elif st.session_state.page == 'reg_home':
    reg_home()
elif st.session_state.page == 'tbl_level1':
    tbl_level1()

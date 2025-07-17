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
    if st.button('Level 2: Filtering with `.loc[]`'):
        go_to('tbl_level2')
    if st.button('Level 3: Aggregations with `.groupby()`'):
        go_to('tbl_level3')
    if st.button('Level 4: `.apply()` Function'):
        go_to('tbl_level4')
    if st.button('Level 5: Sorting and Ordering'):
        go_to('tbl_level5')
    if st.button('Level 6: Finding Unique Values'):
        go_to('tbl_level6')
    if st.button('Level 7: Changing the Index'):
        go_to('tbl_level7')
    if st.button('Level 8: Pivoting Columns'):
        go_to('tbl_level8')
    if st.button('Level 9: Grouping and Counting'):
        go_to('tbl_level9')

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

    answer = st.radio(
        'Select the answer below:', 
        list(options.keys()), 
        format_func=lambda x: options[x], 
        index=None, 
        key='tbl_level1_answer')

    submitted = st.button('Submit Answer', key='submit_lvl1')

    if submitted:
        if answer is None:
            st.warning("Please select an answer before submitting.")
        elif answer == 'A':
            st.success("Correct! `.loc` uses label indexing, and index 1 refers to the second row. Order is row, column.")
            st.session_state['level1_correct'] = True
        else:
            st.error("Not quite... Remember that `.loc` uses labels while `.iloc` uses indexes (positions).")

    if st.session_state.get('level1_correct', False):
        if st.button('Next Level', key='next_lvl1'):
            go_to('tbl_level2')

def tbl_level2():
    back_home()
    st.header('Level 2: Filtering with `.loc[]`')
    st.markdown('You are given the following DataFrame (df):')

    sample_df = pd.DataFrame({
        'Name': ['Oski', 'Cal', 'Bear', 'Oski'],
        'Score': [99, 93, 95, 91]
    })
    st.dataframe(sample_df)

    st.markdown("Which line of code returns **only rows where the name is 'Oski'**?")

    options = {
        'A': "df.iloc[df['Name'] == 'Oski']",
        'B': "df['Name'] = 'Oski'",
        'C': "df.loc['Name' == 'Oski']",
        'D': "df.loc[df['Name'] == 'Oski']"
    }

    answer = st.radio(
        'Select the answer below:',
        list(options.keys()),
        format_func=lambda x: options[x],
        index=None,
        key='tbl_level2_answer'
    )

    submitted = st.button('Submit Answer', key='submit_lvl2')

    if submitted:
        if answer is None:
            st.warning("Please select an answer before submitting.")
        elif answer == 'D':
            st.success("Correct! You're using a Boolean mask with `.loc[]` — solid work.")
            st.session_state['level2_correct'] = True
        else:
            st.error("Nope! Review how Boolean masking works inside `.loc[]`.")

    if st.session_state.get('level2_correct', False):
        if st.button('Next Level', key='next_lvl2'):
            go_to('tbl_level3')

def tbl_level3():
    back_home()
    st.header('Level 3: Selecting Columns')
    st.markdown('Here is your DataFrame:')

    sample_df = pd.DataFrame({
        'Name': ['Oski', 'Cal', 'Bear'],
        'Score': [99, 93, 95],
        'Major': ['Data', 'History', 'CS']
    })
    st.dataframe(sample_df)

    st.markdown('How do you return only the `Name` and `Score` columns?')

    options = {
        'A': "df['Name', 'Score']",
        'B': "df[['Name', 'Score']]",
        'C': "df.loc[:, ['Name', 'Score']]",
        'D': "Both B and C"
    }

    answer = st.radio(
        'Select the answer below:',
        list(options.keys()),
        format_func=lambda x: options[x],
        index=None,
        key='tbl_level3_answer'
    )

    submitted = st.button('Submit Answer', key='submit_lvl3')

    if submitted:
        if answer is None:
            st.warning("Please select an answer before submitting.")
        elif answer == 'D':
            st.success("Correct! Both options return a DataFrame with those two columns.")
            st.session_state['level3_correct'] = True
        else:
            st.error("Not quite. Remember: `df[['col1', 'col2']]` is a valid way to get multiple columns.")

    if st.session_state.get('level3_correct', False):
        if st.button('Next Level', key='next_lvl3'):
            go_to('tbl_level4')

def tbl_level4():
    back_home()
    st.header('Level 4: Boolean Masking')
    st.markdown('DataFrame time:')

    sample_df = pd.DataFrame({
        'Name': ['Oski', 'Cal', 'Bear', 'Oski'],
        'Score': [99, 93, 95, 91],
        'Major': ['Data', 'CS', 'History', 'Data']
    })
    st.dataframe(sample_df)

    st.markdown("How do you return rows where the name is `'Oski'` **and** the major is `'Data'`?")

    options = {
        'A': "df[(df['Name'] == 'Oski') & (df['Major'] == 'Data')]",
        'B': "df['Name'] == 'Oski' and df['Major'] == 'Data'",
        'C': "df.loc[df['Name'] & df['Major'] == 'Data']",
        'D': "df[df['Name'] = 'Oski' & df['Major'] = 'Data']"
    }

    answer = st.radio(
        'Select the answer below:',
        list(options.keys()),
        format_func=lambda x: options[x],
        index=None,
        key='tbl_level4_answer'
    )

    submitted = st.button('Submit Answer', key='submit_lvl4')

    if submitted:
        if answer is None:
            st.warning("Please select an answer before submitting.")
        elif answer == 'A':
            st.success("Correct! The `&` operator works elementwise for boolean arrays. Make sure conditions are wrapped in parentheses.")
            st.session_state['level4_correct'] = True
        else:
            st.error("Nope. `and` doesn't work elementwise in pandas. Also, watch out for assignment (`=`) vs comparison (`==`).")

    if st.session_state.get('level4_correct', False):
        if st.button('Next Level', key='next_lvl4'):
            go_to('tbl_level5')

def tbl_level5():
    back_home()
    st.header("Level 5: Using `.isin()`")
    st.markdown("You're given the following DataFrame (df):")

    sample_df = pd.DataFrame({
        'Name': ['Oski', 'Cal', 'Bear', 'Oski', 'Goldie'],
        'Score': [99, 93, 95, 91, 88]
    })
    st.dataframe(sample_df)

    st.markdown("Which line of code returns all rows where the name is either `'Oski'` or `'Bear'`?")

    options = {
        'A': "df[df['Name'] == ['Oski', 'Bear']]",
        'B': "df.loc[df['Name'].isin(['Oski', 'Bear'])]",
        'C': "df.loc[df['Name'] == 'Oski' or df['Name'] == 'Bear']",
        'D': "df.iloc[df['Name'].isin(['Oski', 'Bear'])]"
    }

    answer = st.radio(
        'Select the answer below:',
        list(options.keys()),
        format_func=lambda x: options[x],
        index=None,
        key='tbl_level5_answer'
    )

    submitted = st.button('Submit Answer')

    if submitted:
        if answer == 'B':
            st.success("Correct! `.isin()` is perfect for checking membership in a list.")
            st.session_state['level5_correct'] = True
        else:
            st.error("Nope! Try reviewing how `.isin()` works and how it's used inside a filter.")

    if st.session_state.get('level5_correct', False):
        if st.button('Next Level'):
            go_to('tbl_level6')

def tbl_level6():
    back_home()
    st.header("Level 6: Finding Unique Values")
    st.markdown("You are given this DataFrame (df):")

    sample_df = pd.DataFrame({
        'Name': ['Oski', 'Cal', 'Bear', 'Oski', 'Goldie'],
        'Score': [99, 93, 95, 91, 88]
    })
    st.dataframe(sample_df)

    st.markdown("Which line gets all the unique names from the 'Name' column?")

    options = {
        'A': "df['Name'].value_counts()",
        'B': "df['Name'].drop_duplicates()",
        'C': "df['Name'].unique()",
        'D': "df['Name'].nunique()"
    }

    answer = st.radio(
        'Select the answer below:',
        list(options.keys()),
        format_func=lambda x: options[x],
        index=None,
        key='tbl_level6_answer'
    )

    submitted = st.button('Submit Answer')

    if submitted:
        if answer == 'C':
            st.success("Correct! `.unique()` returns a NumPy array of the unique values.")
            st.session_state['level6_correct'] = True
        else:
            st.error("Almost! Some of these are close, but only `.unique()` gives you exactly that result.")

    if st.session_state.get('level6_correct', False):
        if st.button('Next Level'):
            go_to('tbl_level7')

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
elif st.session_state.page == 'tbl_level2':
    tbl_level2()
elif st.session_state.page == 'tbl_level3':
    tbl_level3()
elif st.session_state.page == 'tbl_level4':
    tbl_level4()
elif st.session_state.page == 'tbl_level5':
    tbl_level5()
elif st.session_state.page == 'tbl_level6':
    tbl_level6()
elif st.session_state.page == 'tbl_level7':
    tbl_level7()
elif st.session_state.page == 'tbl_level8':
    tbl_level8()
elif st.session_state.page == 'tbl_level9':
    tbl_level9()

#elif st.session_state.page == 'vis_level1':
#    vis_level1()
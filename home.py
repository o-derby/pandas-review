import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

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
    if st.button('Level 3: Selecting Columns'):
        go_to('tbl_level3')
    if st.button('Level 4: Boolean Masking'):
        go_to('tbl_level4')
    if st.button('Level 5: Using `.isin()`'):
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

    if st.button('Level 1: Basic Histogram'):
        go_to('vis_level1')
    if st.button('Level 2: Basic Scatterplot'):
        go_to('vis_level2')
    if st.button('Level 3: Boxplot'):
        go_to('vis_level3')
    if st.button('Level 4: Lineplot'):
        go_to('vis_level4')
    if st.button('Level 5: KDE Plot'):
        go_to('vis_level5')
    # Add more levels as needed...

def reg_home():
    back_home()
    st.header('Review Regression Models')
    st.subheader('Coming Soon!')

# Helper for asking questions
def ask_question(options_dict, question_prompt="Select the correct code:", key="question"):
    return st.radio(
        question_prompt,
        list(options_dict.keys()),
        format_func=lambda x: options_dict[x],
        index=None,
        key=key
    )

# Helper for checking answers with custom comments
def check_answer(selected, correct_answer_key, right_msg, wrong_msg, session_key='correct'):
    submitted = st.button('Submit Answer')
    if submitted:
        if selected == correct_answer_key:
            st.success(right_msg)
            st.session_state[session_key] = True
        else:
            st.error(wrong_msg)
    return st.session_state.get(session_key, False)


# Table Levels
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

    answer = ask_question(options, key='tbl_level1_answer')

    correct = check_answer(
        answer,
        'A',
        "Correct! `.loc` uses label indexing, so index 1 means the second row, specifying row then column.",
        "Not quite. `.loc` uses labels, and here the second row is at index 1."
        ,
        'level1_correct'
    )

    if correct:
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

    answer = ask_question(options, key='tbl_level2_answer')

    correct = check_answer(
        answer,
        'D',
        "Correct! Using a Boolean mask inside `.loc[]` filters rows where the condition is True.",
        "Wrong. `.loc[]` expects a boolean mask for filtering. Review Boolean masking with `.loc[]`.",
        'level2_correct'
    )

    if correct:
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

    answer = ask_question(options, key='tbl_level3_answer')

    correct = check_answer(
        answer,
        'D',
        "Correct! Both `df[['Name', 'Score']]` and `.loc` with all rows and those columns work.",
        "Not quite. `df[['col1', 'col2']]` and `.loc` slicing are both valid ways.",
        'level3_correct'
    )

    if correct:
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

    answer = ask_question(options, key='tbl_level4_answer')

    correct = check_answer(
        answer,
        'A',
        "Correct! The `&` operator works elementwise for boolean arrays, with conditions in parentheses.",
        "Nope. `and` doesn't work elementwise in pandas, and watch out for `=` vs `==`.",
        'level4_correct'
    )

    if correct:
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

    answer = ask_question(options, key='tbl_level5_answer')

    correct = check_answer(
        answer,
        'B',
        "Correct! `.isin()` is perfect for checking membership in a list.",
        "Nope! `.isin()` lets you filter for multiple values inside a list.",
        'level5_correct'
    )

    if correct:
        if st.button('Next Level', key='next_lvl5'):
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

    answer = ask_question(options, key='tbl_level6_answer')

    correct = check_answer(
        answer,
        'C',
        "Correct! `.unique()` returns a NumPy array of the unique values.",
        "Almost! `.unique()` specifically returns unique values as an array.",
        'level6_correct'
    )

    if correct:
        if st.button('Next Level', key='next_lvl6'):
            go_to('tbl_level7')

def tbl_level7():
    back_home()
    st.header("Level 7: Changing the Index")
    st.markdown("You are given this DataFrame (df):")

    sample_df = pd.DataFrame({
        'ID': [101, 102, 103],
        'Name': ['Oski', 'Cal', 'Bear'],
        'Score': [99, 93, 95]
    })
    st.dataframe(sample_df)

    st.markdown("Which line sets the 'ID' column as the index?")

    options = {
        'A': "df.index = df['ID']",
        'B': "df.set_index('ID')",
        'C': "df.set_index('ID', inplace=False)",
        'D': "df.set_index('ID', inplace=True)"
    }

    answer = ask_question(options, key='tbl_level7_answer')

    correct = check_answer(
        answer,
        'D',
        "Correct! `inplace=True` sets the index on the original DataFrame.",
        "Not quite. You need to set the index inplace or assign the result.",
        'level7_correct'
    )

    if correct:
        if st.button('Next Level', key='next_lvl7'):
            go_to('tbl_level8')

def tbl_level8():
    back_home()
    st.header("Level 8: Pivoting Columns")
    st.markdown("You are given this DataFrame (df):")

    sample_df = pd.DataFrame({
        'Date': ['2024-01-01', '2024-01-01', '2024-01-02'],
        'Name': ['Oski', 'Cal', 'Oski'],
        'Score': [99, 88, 95]
    })
    st.dataframe(sample_df)

    st.markdown("Which line transforms the DataFrame to have one row per date and names as columns?")

    options = {
        'A': "df.pivot(index='Name', columns='Date', values='Score')",
        'B': "df.pivot(index='Date', columns='Name', values='Score')",
        'C': "df.pivot_table(index='Date', columns='Score', values='Name')",
        'D': "df.groupby('Date')['Score'].mean()"
    }

    answer = ask_question(options, key='tbl_level8_answer')

    correct = check_answer(
        answer,
        'B',
        "Nice! `pivot` reshapes with `Date` as index and `Name` as columns.",
        "Not quite. You want to pivot by `Date` as index and `Name` as columns.",
        'level8_correct'
    )

    if correct:
        if st.button('Next Level', key='next_lvl8'):
            go_to('tbl_level9')

def tbl_level9():
    back_home()
    st.header("Level 9: Grouping and Counting")
    st.markdown("You are given this DataFrame (df):")

    sample_df = pd.DataFrame({
        'Name': ['Oski', 'Cal', 'Bear', 'Oski', 'Oski'],
        'Passed': [True, False, True, True, False]
    })
    st.dataframe(sample_df)

    st.markdown("Which line gives a count of how many times each name appears?")

    options = {
        'A': "df.groupby('Name').count()",
        'B': "df.groupby('Name').size()",
        'C': "df['Name'].value_counts()",
        'D': "B and C"
    }

    answer = ask_question(options, key='tbl_level9_answer')

    correct = check_answer(
        answer,
        'D',
        "Nice! Both `groupby().size()` and `value_counts()` count occurrences.",
        "Not quite. `groupby().count()` counts non-null entries per column, which might differ.",
        'level9_correct'
    )

    if correct:
        if st.button('Back to Table Home'):
            go_to('tbl_home')


# Visualization Levels
def vis_level1():
    back_home()
    st.header('Level 1: Creating a Histogram')
    st.markdown("You're given the following DataFrame:")

    tips = pd.DataFrame({
        'total_bill': [16.99, 10.34, 21.01, 23.68, 24.59],
        'tip': [1.01, 1.66, 3.50, 3.31, 3.61],
        'sex': ['Female', 'Male', 'Male', 'Male', 'Female'],
        'smoker': ['No', 'No', 'No', 'No', 'No'],
        'day': ['Sun', 'Sun', 'Sun', 'Sun', 'Sun'],
        'time': ['Dinner', 'Dinner', 'Dinner', 'Dinner', 'Dinner'],
        'size': [2, 3, 3, 2, 4]
    })

    st.dataframe(tips)

    st.markdown("Here's the histogram plot:")
    fig, ax = plt.subplots()
    sns.histplot(data=tips, x='total_bill', ax=ax)
    st.pyplot(fig)

    st.markdown("Which line of code would generate this plot?")
    
    options = {
        'A': "sns.histplot(data=tips, x='tip')",
        'B': "sns.histplot(data=tips, x='total_bill')",
        'C': "sns.barplot(data=tips, x='total_bill')",
        'D': "sns.lineplot(data=tips, x='total_bill')"
    }

    answer = ask_question(options, key='vis_level1_answer')

    correct = check_answer(
        answer,
        'B',
        "Correct! Histogram of `total_bill` matches this plot.",
        "Nope. The plot shows a histogram of `total_bill`, not `tip` or bar/line plots.",
        'vis_level1_correct'
    )

    if correct:
        if st.button('Next Level'):
            go_to('vis_level2')

def vis_level2():
    back_home()
    st.header("Level 2: Creating a Scatterplot")
    st.markdown("Given this DataFrame:")

    tips = pd.DataFrame({
        'total_bill': [16.99, 10.34, 21.01, 23.68, 24.59],
        'tip': [1.01, 1.66, 3.50, 3.31, 3.61],
        'sex': ['Female', 'Male', 'Male', 'Male', 'Female'],
        'smoker': ['No', 'No', 'No', 'No', 'No'],
        'day': ['Sun', 'Sun', 'Sun', 'Sun', 'Sun'],
        'time': ['Dinner', 'Dinner', 'Dinner', 'Dinner', 'Dinner'],
        'size': [2, 3, 3, 2, 4]
    })

    st.dataframe(tips)

    st.markdown("Here's the scatterplot:")
    fig, ax = plt.subplots()
    sns.scatterplot(data=tips, x='total_bill', y='tip', ax=ax)
    st.pyplot(fig)

    st.markdown("Which line of code would create this plot?")

    options = {
        'A': "sns.scatterplot(data=tips, x='tip', y='total_bill')",
        'B': "sns.scatterplot(data=tips, x='total_bill', y='tip')",
        'C': "sns.lineplot(data=tips, x='total_bill', y='tip')",
        'D': "sns.barplot(data=tips, x='total_bill', y='tip')"
    }

    answer = ask_question(options, key='vis_level2_answer')

    correct = check_answer(
        answer,
        'B',
        "Correct! Scatterplot with `total_bill` on x and `tip` on y matches.",
        "Wrong. Check the axis order and plot type.",
        'vis_level2_correct'
    )

    if correct:
        if st.button('Next Level'):
            go_to('vis_level3')

def vis_level3():
    back_home()
    st.header("Level 3: Boxplot")
    st.markdown("Here's the DataFrame:")

    tips = pd.DataFrame({
        'day': ['Sun', 'Sun', 'Sun', 'Sun', 'Sun'],
        'total_bill': [16.99, 10.34, 21.01, 23.68, 24.59],
        'tip': [1.01, 1.66, 3.50, 3.31, 3.61]
    })

    st.dataframe(tips)

    st.markdown("Here's the boxplot:")

    fig, ax = plt.subplots()
    sns.boxplot(data=tips, x='day', y='total_bill', ax=ax)
    st.pyplot(fig)

    st.markdown("Which line of code would create this boxplot?")

    options = {
        'A': "sns.boxplot(data=tips, x='day', y='tip')",
        'B': "sns.boxplot(data=tips, x='day', y='total_bill')",
        'C': "sns.barplot(data=tips, x='day', y='total_bill')",
        'D': "sns.boxplot(data=tips, x='total_bill', y='day')"
    }

    answer = ask_question(options, key='vis_level3_answer')

    correct = check_answer(
        answer,
        'B',
        "Correct! Boxplot shows `total_bill` by `day`.",
        "Wrong. Axis assignment matters here for the boxplot.",
        'vis_level3_correct'
    )

    if correct:
        if st.button('Next Level'):
            go_to('vis_level4')

def vis_level4():
    back_home()
    st.header("Level 4: Lineplot")
    st.markdown("DataFrame:")

    df = pd.DataFrame({
        'day': [1, 2, 3, 4, 5],
        'sales': [5, 10, 7, 12, 9]
    })

    st.dataframe(df)

    st.markdown("Lineplot:")

    fig, ax = plt.subplots()
    sns.lineplot(data=df, x='day', y='sales', ax=ax)
    st.pyplot(fig)

    st.markdown("Which line creates this lineplot?")

    options = {
        'A': "sns.lineplot(data=df, x='day', y='sales')",
        'B': "sns.scatterplot(data=df, x='day', y='sales')",
        'C': "sns.histplot(data=df, x='day')",
        'D': "sns.barplot(data=df, x='day', y='sales')"
    }

    answer = ask_question(options, key='vis_level4_answer')

    correct = check_answer(
        answer,
        'A',
        "Right! `lineplot` for sales over days.",
        "Nope. This plot is a line plot, not scatter or bar.",
        'vis_level4_correct'
    )

    if correct:
        if st.button('Next Level'):
            go_to('vis_level5')

def vis_level5():
    back_home()
    st.header("Level 5: KDE Plot")
    st.markdown("DataFrame:")

    df = pd.DataFrame({
        'value': [1, 2, 2, 3, 3, 3, 4, 4, 5]
    })

    st.dataframe(df)

    st.markdown("KDE plot:")

    fig, ax = plt.subplots()
    sns.kdeplot(data=df, x='value', ax=ax)
    st.pyplot(fig)

    st.markdown("Which line creates this KDE plot?")

    options = {
        'A': "sns.kdeplot(data=df, x='value')",
        'B': "sns.histplot(data=df, x='value')",
        'C': "sns.lineplot(data=df, x='value')",
        'D': "sns.boxplot(data=df, x='value')"
    }

    answer = ask_question(options, key='vis_level5_answer')

    correct = check_answer(
        answer,
        'A',
        "Correct! `kdeplot` creates the smooth density estimate.",
        "Nope. This plot is a KDE, not histogram or boxplot.",
        'vis_level5_correct'
    )

    if correct:
        if st.button('Back to Visualization Home'):
            go_to('vis_home')

# Main app routing
def main():
    page = st.session_state.page

    if page == 'home':
        home()
    elif page == 'tbl_home':
        tbl_home()
    elif page == 'tbl_level1':
        tbl_level1()
    elif page == 'tbl_level2':
        tbl_level2()
    elif page == 'tbl_level3':
        tbl_level3()
    elif page == 'tbl_level4':
        tbl_level4()
    elif page == 'tbl_level5':
        tbl_level5()
    elif page == 'tbl_level6':
        tbl_level6()
    elif page == 'tbl_level7':
        tbl_level7()
    elif page == 'tbl_level8':
        tbl_level8()
    elif page == 'tbl_level9':
        tbl_level9()
    elif page == 'vis_home':
        vis_home()
    elif page == 'vis_level1':
        vis_level1()
    elif page == 'vis_level2':
        vis_level2()
    elif page == 'vis_level3':
        vis_level3()
    elif page == 'vis_level4':
        vis_level4()
    elif page == 'vis_level5':
        vis_level5()
    elif page == 'reg_home':
        reg_home()
    else:
        st.write("Unknown page, returning home.")
        go_to('home')

if __name__ == '__main__':
    main()

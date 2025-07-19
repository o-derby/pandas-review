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
    if st.button('Level 6: Barplot'):
        go_to('vis_level6')
    if st.button('Level 7: Boxplot'):
        go_to('vis_level7')
    if st.button('Level 8: KDE Plot'):
        go_to('vis_level8')
    if st.button('Level 9: Color and Size Mapping'):
        go_to('vis_level9')

def reg_home():
    back_home()
    st.header('Review Regression Models')
    st.subheader('Select What level to Review:')

    if st.button('Level 1: Simple Regression with lmplot'):
        go_to('reg_level1')
    if st.button('Level 2: Regression with Hue'):
        go_to('reg_level2')
    if st.button('Level 3: Multiple Regression with Scikit-learn'):
        go_to('reg_level3')
    if st.button('Level 4: Train Test Split'):
        go_to('reg_level4')
    if st.button('Level 5: R² Score'):
        go_to('reg_level5')
    if st.button('Level 6: MAE'):
        go_to('reg_level6')
    if st.button('Level 7: Applying Log Transformation'):
        go_to('reg_level7')
    if st.button('Level 8: Minimizing Residual Error'):
        go_to('reg_level8')
    if st.button('Level 9: Visualizing Regression Fit'):
        go_to('reg_level9')

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
        'B': "sns.barplot(data=tips, x='total_bill', y='tip')",
        'C': "sns.lineplot(data=tips, x='total_bill', y='tip')",
        'D': "sns.scatterplot(data=tips, x='total_bill', y='tip')"
    }

    answer = ask_question(options, key='vis_level2_answer')

    correct = check_answer(
        answer,
        'D',
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
        if st.button('Next Level'):
            go_to('vis_level6')

def vis_level6():
    back_home()
    st.header("Level 6: Barplot with Filtering and Color Grouping")
    st.markdown("Given this DataFrame:")

    tips = pd.DataFrame({
        'total_bill': [16.99, 10.34, 21.01, 23.68, 24.59, 30.14, 12.34],
        'tip': [1.01, 1.66, 3.50, 3.31, 3.61, 5.00, 1.20],
        'sex': ['Female', 'Male', 'Male', 'Male', 'Female', 'Male', 'Female'],
        'smoker': ['No', 'No', 'No', 'No', 'No', 'Yes', 'Yes'],
        'day': ['Sun', 'Sun', 'Sun', 'Sun', 'Sun', 'Sat', 'Sat'],
        'time': ['Dinner', 'Dinner', 'Dinner', 'Dinner', 'Dinner', 'Dinner', 'Lunch'],
        'size': [2, 3, 3, 2, 4, 4, 2]
    })

    st.dataframe(tips)

    st.markdown(
        "Here's the barplot showing average tip by day, grouped by smoker status, "
        "but only for Dinner time:"
    )

    filtered = tips[tips['time'] == 'Dinner']
    fig, ax = plt.subplots()
    sns.barplot(data=filtered, x='day', y='tip', hue='smoker', ax=ax)
    st.pyplot(fig)

    st.markdown("Which of the following lines generates this plot?")

    options = {
        'A': "sns.barplot(data=tips, x='day', y='tip', hue='smoker')",
        'B': "sns.barplot(data=tips, x='day', y='tip')",
        'C': "sns.barplot(data=tips[tips['time']=='Dinner'], x='day', y='tip', hue='smoker')",
        'D': "sns.barplot(data=tips[tips['smoker']=='No'], x='day', y='tip', hue='time')"
    }

    answer = ask_question(options, key='vis_level6_answer')
    submitted = st.button('Submit Answer')
    if submitted:
        if answer == 'C':
            st.success("Correct! Filtering first with `[tips['time']=='Dinner']` then grouping with `hue='smoker'` is exactly right.")
            st.session_state['vis_level6_correct'] = True
        else:
            st.error("Close but no. Remember, the data was filtered by Dinner only before plotting.")

    if st.session_state.get('vis_level6_correct', False):
        if st.button('Next Level'):
            go_to('vis_level7')

def vis_level7():
    back_home()
    st.header("Level 7: Boxplot with Hue and Row Filtering")
    st.markdown("Given this DataFrame:")

    tips = pd.DataFrame({
        'total_bill': [16.99, 10.34, 21.01, 23.68, 24.59, 30.14, 12.34, 15.20],
        'tip': [1.01, 1.66, 3.50, 3.31, 3.61, 5.00, 1.20, 2.00],
        'sex': ['Female', 'Male', 'Male', 'Male', 'Female', 'Male', 'Female', 'Female'],
        'smoker': ['No', 'No', 'No', 'No', 'No', 'Yes', 'Yes', 'No'],
        'day': ['Sun', 'Sun', 'Sun', 'Sun', 'Sun', 'Sat', 'Sat', 'Fri'],
        'time': ['Dinner', 'Dinner', 'Dinner', 'Dinner', 'Dinner', 'Dinner', 'Lunch', 'Lunch'],
        'size': [2, 3, 3, 2, 4, 4, 2, 2]
    })

    st.dataframe(tips)

    st.markdown(
        "Here's the boxplot showing total bills by day, grouped by smoker, "
        "but only for days that are not Sunday:"
    )

    filtered = tips[tips['day'] != 'Sun']
    fig, ax = plt.subplots()
    sns.boxplot(data=filtered, x='day', y='total_bill', hue='smoker', ax=ax)
    st.pyplot(fig)

    st.markdown("Which line of code would generate this plot?")

    options = {
        'A': "sns.boxplot(data=tips, x='day', y='total_bill', hue='smoker')",
        'B': "sns.boxplot(data=tips[tips['day']!='Sun'], x='day', y='total_bill', hue='smoker')",
        'C': "sns.violinplot(data=tips[tips['day']=='Sun'], x='day', y='total_bill', hue='smoker')",
        'D': "sns.boxplot(data=tips[tips['smoker']=='No'], x='day', y='total_bill')"
    }

    answer = ask_question(options, key='vis_level7_answer')
    submitted = st.button('Submit Answer')
    if submitted:
        if answer == 'B':
            st.success("Good job! Filtering out Sundays and grouping by smoker status is exactly the trick.")
            st.session_state['vis_level7_correct'] = True
        else:
            st.error("Not quite. Remember the plot excludes Sundays and uses `hue='smoker'`.")

    if st.session_state.get('vis_level7_correct', False):
        if st.button('Next Level'):
            go_to('vis_level8')

def vis_level8():
    back_home()
    st.header("Level 8: Heatmap from Pivoted Data")
    st.markdown("Given this DataFrame:")

    flights = pd.DataFrame({
        'year': [1950, 1950, 1951, 1951, 1952, 1952],
        'month': [1, 2, 1, 2, 1, 2],
        'passengers': [112, 118, 132, 129, 144, 140]
    })

    st.dataframe(flights)

    st.markdown("Here's the heatmap showing passengers by year and month:")

    pivot = flights.pivot(index='year', columns='month', values='passengers')

    fig, ax = plt.subplots()
    sns.heatmap(pivot, annot=True, fmt="d", cmap="YlGnBu", ax=ax)
    st.pyplot(fig)

    st.markdown("Which line creates this heatmap?")

    options = {
        'A': "sns.heatmap(flights, annot=True, fmt='d')",
        'B': "sns.heatmap(flights.pivot(index='year', columns='month', values='passengers'), annot=True, fmt='d', cmap='YlGnBu')",
        'C': "sns.heatmap(flights.pivot(index='month', columns='year', values='passengers'), annot=True)",
        'D': "sns.heatmap(flights.pivot_table(index='year', columns='month', values='passengers'), cmap='viridis')"
    }

    answer = ask_question(options, key='vis_level8_answer')
    submitted = st.button('Submit Answer')
    if submitted:
        if answer == 'B':
            st.success("Exactly! Pivot the data by year and month, then plot with YlGnBu colormap.")
            st.session_state['vis_level8_correct'] = True
        else:
            st.error("Nope. Remember to pivot correctly for index=year and columns=month with passengers as values.")

    if st.session_state.get('vis_level8_correct', False):
        if st.button('Next Level'):
            go_to('vis_level9')

def vis_level9():
    back_home()
    st.header("Level 9: Scatterplot with Color and Size Mapping")
    st.markdown("Given this DataFrame:")

    tips = pd.DataFrame({
        'total_bill': [16.99, 10.34, 21.01, 23.68, 24.59, 30.14, 12.34, 15.20, 20.50],
        'tip': [1.01, 1.66, 3.50, 3.31, 3.61, 5.00, 1.20, 2.00, 3.00],
        'sex': ['Female', 'Male', 'Male', 'Male', 'Female', 'Male', 'Female', 'Female', 'Male'],
        'smoker': ['No', 'No', 'No', 'No', 'No', 'Yes', 'Yes', 'No', 'No'],
        'day': ['Sun', 'Sun', 'Sun', 'Sun', 'Sun', 'Sat', 'Sat', 'Fri', 'Fri'],
        'time': ['Dinner', 'Dinner', 'Dinner', 'Dinner', 'Dinner', 'Dinner', 'Lunch', 'Lunch', 'Lunch'],
        'size': [2, 3, 3, 2, 4, 4, 2, 2, 3]
    })

    st.dataframe(tips)

    st.markdown(
        "Here's the scatterplot where:\n"
        "- X is total_bill\n"
        "- Y is tip\n"
        "- Color (hue) shows smoker status\n"
        "- Size of points is the party size\n"
        "Only Dinner time rows are shown."
    )

    filtered = tips[tips['time'] == 'Dinner']

    fig, ax = plt.subplots()
    sns.scatterplot(data=filtered, x='total_bill', y='tip', hue='smoker', size='size', ax=ax)
    st.pyplot(fig)

    st.markdown("Which line of code generates this plot?")

    options = {
        'A': "sns.scatterplot(data=tips, x='total_bill', y='tip', hue='smoker', size='size')",
        'B': "sns.scatterplot(data=tips[tips['time']=='Lunch'], x='total_bill', y='tip', hue='smoker', size='size')",
        'C': "sns.scatterplot(data=tips, x='total_bill', y='tip')",
        'D': "sns.scatterplot(data=tips[tips['time']=='Dinner'], x='total_bill', y='tip', hue='smoker', size='size')"
    }

    answer = ask_question(options, key='vis_level9_answer')
    submitted = st.button('Submit Answer')
    if submitted:
        if answer == 'D':
            st.success("Correct! You filtered for Dinner, and mapped color and size accordingly.")
            st.session_state['vis_level9_correct'] = True
        else:
            st.error("Not quite. Don't forget to filter by Dinner time before plotting.")

    if st.session_state.get('vis_level9_correct', False):
        if st.button('Back to Visualization Home'):
            go_to('vis_home')

def reg_level1():
    back_home()
    st.header('Level 1: Linear Regression with lmplot')

    st.markdown("You're given this dataset:")

    df = pd.read_csv('data/tips.csv')
    st.dataframe(df[['total_bill', 'tip']].head())

    st.markdown("Here’s a regression plot:")

    fig = sns.lmplot(data=df, x='total_bill', y='tip')
    st.pyplot(fig)

    st.markdown("Which code generates this plot?")

    options = {
        'A': "sns.lmplot(data=df, x='tip', y='total_bill')",
        'B': "sns.lineplot(data=df, x='total_bill', y='tip')",
        'C': "sns.lmplot(data=df, x='total_bill', y='tip')",
        'D': "sns.histplot(data=df, x='total_bill', y='tip')"
    }

    answer = st.radio("Select the correct code:", list(options.keys()),
                      format_func=lambda x: options[x], index=None, key="reg1_ans")
    
    if st.button("Submit"):
        if answer == 'C':
            st.success("Correct! `lmplot` fits a regression line for `x='total_bill'`, `y='tip'`.")
            st.session_state['reg1_correct'] = True
        else:
            st.error("Not quite — look for the plot type and the right variable order.")
    
    if st.session_state.get('reg1_correct', False):
        if st.button("Next Level"):
            go_to('reg_level2')

def reg_level2():
    back_home()
    st.header('Level 2: Regression with Hue')

    df = pd.read_csv('data/tips.csv')
    st.dataframe(df[['total_bill', 'tip', 'sex']].head())

    fig = sns.lmplot(data=df, x='total_bill', y='tip', hue='sex')
    st.pyplot(fig)

    st.markdown("Which code adds color based on sex?")

    options = {
        'A': "sns.lmplot(data=df, x='total_bill', y='tip')",
        'B': "sns.lmplot(data=df, x='total_bill', y='tip', color='sex')",
        'C': "sns.lmplot(data=df, x='total_bill', y='tip', hue='sex')",
        'D': "sns.lmplot(data=df, x='tip', y='total_bill', hue='sex')"
    }

    answer = st.radio("Select the correct code:", list(options.keys()),
                      format_func=lambda x: options[x], index=None, key="reg2_ans")
    
    if st.button("Submit"):
        if answer == 'C':
            st.success("Yep! `hue='sex'` splits the regression by color.")
            st.session_state['reg2_correct'] = True
        else:
            st.error("Nope — watch out for `color` vs `hue`, and variable order.")

    if st.session_state.get('reg2_correct', False):
        if st.button("Next Level"):
            go_to('reg_level3')

def reg_level3():
    back_home()
    st.header('Level 3: Multiple Regression with Scikit-learn')

    st.markdown("You fit a model using scikit-learn:")
    st.code("LinearRegression().fit(X[['total_bill', 'size']], y)", language='python')

    st.markdown("What are `X` and `y` in this case?")

    options = {
        'A': "X = df[['tip']], y = df['total_bill']",
        'B': "X = df[['total_bill', 'size']], y = df['tip']",
        'C': "X = df['tip'], y = df[['total_bill', 'size']]",
        'D': "X = df[['size']], y = df['tip']"
    }

    answer = st.radio("Select the correct definition:", list(options.keys()),
                      format_func=lambda x: options[x], index=None, key="reg3_ans")
    
    if st.button("Submit"):
        if answer == 'B':
            st.success("Nice! That's multiple regression with two features predicting `tip`.")
            st.session_state['reg3_correct'] = True
        else:
            st.error("Not quite — pay attention to which columns go in `X` vs `y`.")

    if st.session_state.get('reg3_correct', False):
        if st.button("Next Level"):
            go_to('reg_level4')

def reg_level4():
    back_home()
    st.header('Level 4: Train-Test Split')

    st.markdown("What's the purpose of using `train_test_split(X, y, test_size=0.2)`?")

    options = {
        'A': "It trains your model 20 times.",
        'B': "It keeps 20% of the data for testing.",
        'C': "It balances class labels.",
        'D': "It ensures your data is sorted."
    }

    answer = st.radio("Choose the best explanation:", list(options.keys()),
                      format_func=lambda x: options[x], index=None, key="reg4_ans")
    
    if st.button("Submit"):
        if answer == 'B':
            st.success("Exactly — 20% held out for evaluation!")
            st.session_state['reg4_correct'] = True
        else:
            st.error("Try again — this is a core part of testing model generalization.")

    if st.session_state.get('reg4_correct', False):
        if st.button("Next Level"):
            go_to('reg_level5')

def reg_level5():
    back_home()
    st.header('Level 5: R² Score')

    st.markdown("You train a model and evaluate it with `r2_score(y_test, y_pred)`.")

    st.markdown("If your model gets an R² of 0.82, what does that mean?")

    options = {
        'A': "82% of variance in the target is explained by the model.",
        'B': "The model is 82% accurate.",
        'C': "82% of predictions are correct.",
        'D': "The model made 82 predictions correctly."
    }

    answer = st.radio("Pick the most accurate interpretation:", list(options.keys()),
                      format_func=lambda x: options[x], index=None, key="reg5_ans")
    
    if st.button("Submit"):
        if answer == 'A':
            st.success("Correct — R² measures explained variance.")
            st.session_state['reg5_correct'] = True
        else:
            st.error("R² is not accuracy — it's about variance explained.")

    if st.session_state.get('reg5_correct', False):
        if st.button("Next Level"):
            go_to('reg_level6')

def reg_level6():
    back_home()
    st.header('Level 6: MAE (Mean Absolute Error)')

    st.markdown("You evaluate a regression model and get a **MAE of 3.2**.")

    st.markdown("What does this tell you?")

    options = {
        'A': "The model is 3.2% off on average.",
        'B': "The average prediction is off by 3.2 units.",
        'C': "The model correctly predicts 3.2 values.",
        'D': "The R² score is 3.2."
    }

    answer = st.radio("Pick the best interpretation:", list(options.keys()),
                      format_func=lambda x: options[x], index=None, key="reg6_ans")
    
    if st.button("Submit"):
        if answer == 'B':
            st.success("Correct — MAE measures average absolute error in the same units as the target.")
            st.session_state['reg6_correct'] = True
        else:
            st.error("MAE isn’t a percentage or accuracy score. It tells how far off predictions are on average.")

    if st.session_state.get('reg6_correct', False):
        if st.button("Next Level"):
            go_to('reg_level7')

def reg_level7():
    back_home()
    st.header('Level 7: Log Transforming to Linearize')

    st.markdown("You plot a scatterplot of income vs. home price and see a strong curve, not a line.")

    st.markdown("You apply a log transformation to `home_price` and the result becomes linear.")

    options = {
        'A': "The relationship is exponential, and log transformation made it linear.",
        'B': "The data was originally linear, and log reversed it.",
        'C': "Log transformation is only for normalizing features.",
        'D': "This means `income` is the log of `home_price`."
    }

    answer = st.radio("Which is the best explanation?", list(options.keys()),
                      format_func=lambda x: options[x], index=None, key="reg7_ans")
    
    if st.button("Submit"):
        if answer == 'A':
            st.success("Yep! Exponential relationships can be made linear with a log transformation.")
            st.session_state['reg7_correct'] = True
        else:
            st.error("Remember: log is often used to linearize curved patterns in data.")

    if st.session_state.get('reg7_correct', False):
        if st.button("Next Level"):
            go_to('reg_level8')

def reg_level8():
    back_home()
    st.header('Level 8: Minimizing Error Curve')

    st.markdown("You're fitting a model and plotting the loss (error) over iterations.")

    st.markdown("What does the point at the bottom of the loss curve represent?")

    options = {
        'A': "Where the model is overfitting.",
        'B': "Where the model generalizes perfectly.",
        'C': "Where training error equals testing error.",
        'D': "The point of minimum training loss (error)."
    }

    answer = st.radio("Pick the best interpretation:", list(options.keys()),
                      format_func=lambda x: options[x], index=None, key="reg8_ans")
    
    if st.button("Submit"):
        if answer == 'D':
            st.success("Correct — the minimum of the loss curve is where training loss is lowest.")
            st.session_state['reg8_correct'] = True
        else:
            st.error("Loss curves show error values — this is about minimizing them, not perfect prediction.")

    if st.session_state.get('reg8_correct', False):
        if st.button("Next Level"):
            go_to('reg_level9')

def reg_level9():
    back_home()
    st.header('Level 9: Multiple Regression w/ Interaction')

    st.markdown("You train a multiple regression model with features `age`, `income`, and their interaction (`age * income`).")

    st.markdown("Why might including the interaction term improve the model?")

    options = {
        'A': "It adds nonlinearity by default.",
        'B': "It captures how age modifies the effect of income (and vice versa).",
        'C': "Interaction terms help models train faster.",
        'D': "It's always better to add all possible feature combinations."
    }

    answer = st.radio("Pick the best explanation:", list(options.keys()),
                      format_func=lambda x: options[x], index=None, key="reg9_ans")
    
    if st.button("Submit"):
        if answer == 'B':
            st.success("Correct — interaction terms help capture feature interdependence.")
            st.session_state['reg9_correct'] = True
        else:
            st.error("Interaction terms are for modeling combined effects, not training speed or nonlinearity by default.")

    if st.session_state.get('reg9_correct', False):
        if st.button("Back to Regression Home"):
            go_to('reg_home')

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
elif page == 'vis_level6':
    vis_level6()
elif page == 'vis_level7':
    vis_level7()
elif page == 'vis_level8':
    vis_level8()
elif page == 'vis_level9':
    vis_level9()
elif page == 'reg_home':
    reg_home()
elif page == 'reg_level1':
    reg_level1()
elif page == 'reg_level2':
    reg_level2()
elif page == 'reg_level3':
    reg_level3()
elif page == 'reg_level4':
    reg_level4()
elif page == 'reg_level5':
    reg_level5()
elif page == 'reg_level6':
    reg_level6()
elif page == 'reg_level7':
    reg_level7()
elif page == 'reg_level8':
    reg_level8()
elif page == 'reg_level9':
    reg_level9()
else:
    st.write("Unknown page, returning home.")
    go_to('home')

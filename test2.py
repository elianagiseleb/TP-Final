import streamlit as st


titanic = sns.load_dataset('titanic')

st.write(titanic)


selected_columns = ['survived','pclass','sex','age','sibsp','parch','fare','embarked']


st.write(selected_columns)


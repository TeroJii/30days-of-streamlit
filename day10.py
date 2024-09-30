import streamlit as st

st.header('st.selectbox')

option = st.selectbox(
     'What is your favorite color?',
     ('Blue', 'Red', 'Green'))

shade = st.radio("I like this shade of " + option, ('Dark', 'Medium', 'Light'))

st.write('Your favorite color is ', shade + ' ' + option)
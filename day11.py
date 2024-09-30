import streamlit as st

st.header('st.multiselect')

options = st.multiselect(
     'What are your favorite colors',
     ['Green', 'Yellow', 'Red', 'Blue', 'Gray'],
     ['Yellow', 'Red']
)

options2 = ', '.join(options)

st.write('You selected:', options)

st.write('You selected:', options2)
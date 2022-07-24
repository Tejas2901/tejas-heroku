import streamlit as st

st.set_page_config(page_title = "tejas's streamlit app")

st.subheader('Hi, I am Tejas')
st.title('App to calculate sum of two numbers')

D = st.number_input('Enter a number')
B = st.number_input('Enter one more number')
sum = A + B
C = st.write('Sum of the given two number is ',sum)

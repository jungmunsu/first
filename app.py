import streamlit as st

st.subheader('1. Checkbox test')
a = st.checkbox('1번')
b = st.checkbox('2번')
c = st.checkbox('3번')

if a:
    st.write('1번을 선택하셨습니다.')
if b:
    st.write('2번을 선택하셨습니다.')
if c:
    st.write('3번을 선택하셨습니다.')




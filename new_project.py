import streamlit as st

st.header('백분위 계산기')
a = st.number_input('인원수를 입력하세요.',min_value=0,step=1)
b = st.number_input('당신의 석차를 입력하세요.',min_value=1,step=1)
sbtn = st.button('확인')
if sbtn:
    st.success('당신의 백분위는'+str(round((b/a)*100,1))+'%입니다.')


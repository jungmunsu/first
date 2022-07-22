import streamlit as st

menu = st.sidebar.selectbox('MENU', options=['평균 칼로리 섭취량','평균 칼로리 소모량'])

if menu == '평균 칼로리 섭취량':
 st.header('오늘 당신이 먹은 칼로리')

 a = st.checkbox('아이스크림')
 b = st.checkbox('과자')
 c = st.checkbox('배추김치')
 d = st.checkbox('라면')
 e = st.checkbox('짜장면')
 f = st.checkbox('보쌈')
 g = st.checkbox('닭발')
 h = st.checkbox('떠먹는 요거트')
 i = st.checkbox('고구마')
 j = st.checkbox('마라탕')
 k = st.checkbox('떡볶이')
 l = st.checkbox('치킨')
 sum=0

 if a:
     sum+=230
 if b:
     sum+=580
 if c:
     sum+=29
 if d:
     sum+=400
 if e:
     sum+=700
 if f:
     sum+=800
 if g:
     sum+=1161
 if h:
     sum+=75
 if i:
     sum+=268
 if j:
     sum+=1845
 if k:
     sum+=304
 if l:
     sum+=2233
 ybtn = st.button('입력')
 if ybtn:
     st.success('당신이 드신 kcal는 '+str(sum)+'kcal입니다.')
if menu == '평균 칼로리 소모량':
    st.header('오늘 당신이 소비한 칼로리')

    A = st.checkbox('걷기')
    B = st.checkbox('조깅')
    C = st.checkbox('수면')
    D = st.checkbox('공부')
    E = st.checkbox('자전거 타기')
    F = st.checkbox('수영')
    G = st.checkbox('테니스')
    H = st.checkbox('농구')
    I = st.checkbox('청소')
    J = st.checkbox('배드민턴')
    sum1 = 0

    if A:
        sum1 += 300
    if B:
        sum1 += 480
    if C:
        sum1 += 270
    if D:
        sum1 += 90
    if E:
        sum1 += 780
    if F:
        sum1 += 430
    if G:
        sum1 += 420
    if H:
        sum1 += 240
    if I:
        sum1 += 90
    if J:
        sum1 += 210
    kbtn = st.button('입력')
    if kbtn:
     st.success('당신이 소비한 kcal는'+str(sum1)+'kcal 입니다.')
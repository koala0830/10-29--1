import streamlit as st
st.title("이서영의 첫번째 앱!")
st.subheader("이윤서처럼 수학 잘해지기")
st.write("윤서의 뇌를 내 뇌랑 바꿔치기하자!")
st.link_button("네이버 바로가기",'https://naver.com')

name = st.text_input("이름을 입력해주세요:")
if st.button('환영 인사'):
    st.write(name+"님 안녕하세요!")
    st.balloons()
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSRvvlIKUdJpeiM3NMKZ_3OhhpQ3yTBub3FUw&s")
    
st.success('코알라 안아보기!')
st.warning("코알라 많이 만져주셔야해요!")
st.error("코알라 안아주세요!")
st.info("코알라 사랑하기!")

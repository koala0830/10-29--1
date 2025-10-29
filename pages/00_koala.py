import streamlit as st
import random

st.set_page_config(page_title="코알라 꾸미기 🐨", page_icon="🐨", layout="centered")

st.title("🐨 코알라 꾸미기 놀이터 (이모티콘 버전)")
st.write("이모티콘으로 코알라를 꾸며보세요! 💖")

# 🎨 기본 코알라
koala_base = "🐨"

# 🎽 상의
tops = {
    "없음": "",
    "분홍 셔츠": "👚",
    "파란 셔츠": "👕",
    "후드티": "🧥",
    "정장": "🤵",
    "가죽 재킷": "🧥🕶️",
}

# 👖 하의
bottoms = {
    "없음": "",
    "청바지": "👖",
    "반바지": "🩳",
    "치마": "👗",
    "한복 하의": "🎎",
}

# 🎩 소품
accessories = {
    "없음": "",
    "모자": "🎩",
    "왕관": "👑",
    "리본": "🎀",
    "선글라스": "🕶️",
    "안경": "👓",
    "목걸이": "📿",
    "가방": "👜",
    "꽃": "🌸",
}

# 🌈 배경
backgrounds = {
    "없음": "",
    "숲": "🌳🌿🌲",
    "바다": "🌊🏖️🐚",
    "하늘": "☁️🌈✨",
    "도시": "🏙️🚗🌆",
    "무지개": "🌈💫⭐",
    "파티": "🎉🎊🎈",
}

# 🔧 사이드바 옵션
st.sidebar.header("🎨 꾸미기 옵션")
selected_top = st.sidebar.selectbox("상의 선택", list(tops.keys()))
selected_bottom = st.sidebar.selectbox("하의 선택", list(bottoms.keys()))
selected_acc = st.sidebar.multiselect("소품 선택 (복수 선택 가능)", list(accessories.keys()))
selected_bg = st.sidebar.selectbox("배경 선택", list(backgrounds.keys()))

# 🎲 랜덤 꾸미기
if st.sidebar.button("랜덤 코알라 🎲"):
    selected_top = random.choice(list(tops.keys()))
    selected_bottom = random.choice(list(bottoms.keys()))
    selected_acc = random.sample(list(accessories.keys()), k=random.randint(0, 3))
    selected_bg = random.choice(list(backgrounds.keys()))

# 💫 코알라 꾸미기
final_look = f"""
{backgrounds[selected_bg]}

{accessories.get('왕관', '') if '왕관' in selected_acc else ''}
{accessories.get('모자', '') if '모자' in selected_acc else ''}
{accessories.get('리본', '') if '리본' in selected_acc else ''}
{koala_base}
{tops[selected_top]} {bottoms[selected_bottom]}

{" ".join([accessories[a] for a in selected_acc if a not in ['왕관','모자','리본']])}

{backgrounds[selected_bg]}
"""

# 💖 출력
st.markdown(f"<h1 style='text-align:center; font-size:3em;'>{final_look}</h1>", unsafe_allow_html=True)

# 📸 다운로드 (텍스트로 저장)
st.download_button(
    label="📥 꾸민 코알라 저장하기",
    data=final_look,
    file_name="koala_emoji.txt",
    mime="text/plain",
)

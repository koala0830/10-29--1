import streamlit as st
from PIL import Image
import requests
from io import BytesIO

st.set_page_config(page_title="코알라 꾸미기 🐨", page_icon="🐨", layout="centered")

st.title("🐨 코알라 꾸미기 놀이터")
st.write("귀여운 코알라에게 옷과 소품을 입혀보세요!")

# 🔹 이미지 로드 함수
@st.cache_data
def load_image(url):
    response = requests.get(url)
    return Image.open(BytesIO(response.content)).convert("RGBA")

# 🔹 기본 코알라
base_koala = load_image(
    "https://raw.githubusercontent.com/akshaybahadur21/Koala-DressUp-Demo/main/images/koala_base.png"
)

# 🔹 의상 / 소품 URL 모음 (투명 PNG)
tops = {
    "없음": None,
    "분홍 티셔츠": "https://raw.githubusercontent.com/akshaybahadur21/Koala-DressUp-Demo/main/images/top_pink.png",
    "파란 셔츠": "https://raw.githubusercontent.com/akshaybahadur21/Koala-DressUp-Demo/main/images/top_blue.png",
    "노랑 후드티": "https://raw.githubusercontent.com/akshaybahadur21/Koala-DressUp-Demo/main/images/top_yellow.png",
}

bottoms = {
    "없음": None,
    "청바지": "https://raw.githubusercontent.com/akshaybahadur21/Koala-DressUp-Demo/main/images/bottom_jeans.png",
    "반바지": "https://raw.githubusercontent.com/akshaybahadur21/Koala-DressUp-Demo/main/images/bottom_shorts.png",
    "치마": "https://raw.githubusercontent.com/akshaybahadur21/Koala-DressUp-Demo/main/images/bottom_skirt.png",
}

accessories = {
    "없음": None,
    "모자": "https://raw.githubusercontent.com/akshaybahadur21/Koala-DressUp-Demo/main/images/acc_hat.png",
    "왕관": "https://raw.githubusercontent.com/akshaybahadur21/Koala-DressUp-Demo/main/images/acc_crown.png",
    "선글라스": "https://raw.githubusercontent.com/akshaybahadur21/Koala-DressUp-Demo/main/images/acc_sunglasses.png",
    "안경": "https://raw.githubusercontent.com/akshaybahadur21/Koala-DressUp-Demo/main/images/acc_glasses.png",
    "목걸이": "https://raw.githubusercontent.com/akshaybahadur21/Koala-DressUp-Demo/main/images/acc_necklace.png",
    "리본": "https://raw.githubusercontent.com/akshaybahadur21/Koala-DressUp-Demo/main/images/acc_ribbon.png",
}

# 🔹 사이드바
st.sidebar.header("🎨 꾸미기 옵션")
selected_top = st.sidebar.selectbox("상의 선택", list(tops.keys()))
selected_bottom = st.sidebar.selectbox("하의 선택", list(bottoms.keys()))
selected_acc = st.sidebar.multiselect("소품 선택 (복수 선택 가능)", list(accessories.keys()))

# 🔹 합성용 이미지
final_img = base_koala.copy()

def paste_image(base, url):
    if url:
        overlay = load_image(url)
        base.paste(overlay, (0, 0), overlay)

# 순서대로 겹치기
paste_image(final_img, tops[selected_top])
paste_image(final_img, bottoms[selected_bottom])
for acc in selected_acc:
    paste_image(final_img, accessories[acc])

# 🔹 결과 표시
st.image(final_img, caption="✨ 나만의 꾸민 코알라", use_container_width=True)

# 🔹 다운로드
buf = BytesIO()
final_img.save(buf, format="PNG")
st.download_button(
    "📸 이미지 다운로드",
    data=buf.getvalue(),
    file_name="koala_dressup.png",
    mime="image/png",
)

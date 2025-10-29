import streamlit as st
from PIL import Image
import requests
from io import BytesIO

st.set_page_config(page_title="코알라 꾸미기 🐨", page_icon="🐨", layout="centered")

st.title("🐨 코알라 꾸미기 놀이터")
st.write("코알라에게 예쁜 옷과 멋진 소품을 입혀주세요!")

# 🔹 이미지 로드 함수
def load_image(url):
    response = requests.get(url)
    return Image.open(BytesIO(response.content)).convert("RGBA")

# 🔹 기본 코알라 이미지 (투명 배경 PNG)
BASE_URL = "https://raw.githubusercontent.com/daangn/koala-assets/main/"  # (예시 URL, 나중에 바꿀 수 있음)
base_koala = load_image("https://raw.githubusercontent.com/akshaybahadur21/Koala-DressUp-Demo/main/images/koala_base.png")

# 🔹 의상 & 소품 이미지 (무료 예시 PNG URL 사용)
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

# 🔹 사이드바 옵션
st.sidebar.header("🎨 꾸미기 옵션")
selected_top = st.sidebar.selectbox("상의 선택", list(tops.keys()))
selected_bottom = st.sidebar.selectbox("하의 선택", list(bottoms.keys()))
selected_acc = st.sidebar.multiselect("소품 선택 (복수 선택 가능)", list(accessories.keys()))

# 🔹 이미지 합성
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

# 🔹 다운로드 버튼
buf = BytesIO()
final_img.save(buf, format="PNG")
byte_im = buf.getvalue()

st.download_button(
    label="📸 이미지 다운로드",
    data=byte_im,
    file_name="koala_dressup.png",
    mime="image/png",
)


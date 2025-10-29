import streamlit as st

st.set_page_config(page_title="코알라 꾸미기 🐨", page_icon="🐨", layout="centered")

st.title("🐨 코알라 꾸미기 놀이터 (이모티콘 버전)")
st.write("이모티콘 옷과 소품을 코알라 위에 직접 입혀보세요! 🎨")

html_code = """
<style>
body { text-align: center; }
#playground {
  position: relative;
  width: 320px;
  height: 400px;
  margin: 20px auto;
  background-color: #fdfdfd;
  border: 3px dashed #ccc;
  border-radius: 20px;
  overflow: hidden;
}
#koala {
  font-size: 140px;
  position: absolute;
  top: 100px;
  left: 100px;
  z-index: 1;
}
.item {
  position: absolute;
  font-size: 60px;
  cursor: grab;
  z-index: 2;
}
.palette {
  margin-top: 30px;
}
.palette span {
  font-size: 40px;
  margin: 5px;
  cursor: grab;
}
</style>

<div id="playground">
  <div id="koala">🐨</div>
</div>

<div class="palette">
  <p>👇 아래 이모티콘을 드래그해서 코알라 위에 올려보세요!</p>
  <p>👕옷: 👕👚🧥🩳👗🩲🥋🧶🦺</p>
  <p>🎩모자/머리: 🎩👑🎓🧢⛑️👒🎀</p>
  <p>😎얼굴/소품: 😎🕶️👓🩹💄🤡😷</p>
  <p>💎기타/장신구: 💎📿💍🎁🌸🌼🕯️👜💫🍀🍕🍦🎈</p>
</div>

<script>
const playground = document.getElementById('playground');

let draggedEmoji = null;
document.querySelectorAll('.palette span, .palette p span').forEach(span => {
  span.addEventListener('dragstart', (e) => {
    e.dataTransfer.setData('text/plain', e.target.textContent);
  });
});

playground.addEventListener('dragover', (e) => e.preventDefault());

playground.addEventListener('drop', (e) => {
  e.preventDefault();
  const emoji = e.dataTransfer.getData('text/plain');
  const newItem = document.createElement('div');
  newItem.textContent = emoji;
  newItem.className = 'item';
  newItem.style.left = (e.offsetX - 30) + 'px';
  newItem.style.top = (e.offsetY - 30) + 'px';
  newItem.draggable = true;
  newItem.addEventListener('dragstart', dragStart);
  playground.appendChild(newItem);
});

function dragStart(e) {
  e.dataTransfer.setData('text/plain', e.target.textContent);
}
</script>
"""

st.components.v1.html(html_code, height=700)

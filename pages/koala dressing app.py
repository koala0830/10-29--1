import streamlit as st

st.set_page_config(page_title="코알라 꾸미기 🐨", page_icon="🐨", layout="centered")

st.title("🐨 코알라 꾸미기 놀이터")
st.write("옷과 소품을 드래그해서 코알라에게 입혀보세요!")

# 🧱 HTML + CSS + JS 기반 인터랙티브 꾸미기
html_code = """
<style>
body { text-align: center; }
.container {
  position: relative;
  width: 300px;
  height: 300px;
  margin: auto;
  border: 3px dashed #ccc;
  border-radius: 20px;
  background-color: #f9f9f9;
}
#koala {
  font-size: 120px;
  position: absolute;
  top: 60px;
  left: 100px;
  z-index: 1;
}
.item {
  font-size: 40px;
  position: absolute;
  cursor: grab;
  z-index: 2;
}
.palette {
  margin-top: 20px;
}
.palette span {
  font-size: 40px;
  margin: 8px;
  cursor: grab;
}
</style>

<div class="container" id="canvas">
  <div id="koala">🐨</div>
</div>

<div class="palette">
  <p>👕 옷 / 소품을 드래그해서 코알라에게 입혀보세요 👇</p>
  <span draggable="true">🎩</span>
  <span draggable="true">👑</span>
  <span draggable="true">🎀</span>
  <span draggable="true">🕶️</span>
  <span draggable="true">👚</span>
  <span draggable="true">👖</span>
  <span draggable="true">🩳</span>
  <span draggable="true">👜</span>
  <span draggable="true">🌸</span>
  <span draggable="true">📿</span>
</div>

<script>
const canvas = document.getElementById('canvas');
canvas.addEventListener('dragover', (e) => e.preventDefault());
canvas.addEventListener('drop', (e) => {
  e.preventDefault();
  const emoji = e.dataTransfer.getData('text/plain');
  const newItem = document.createElement('div');
  newItem.textContent = emoji;
  newItem.className = 'item';
  newItem.style.left = (e.offsetX - 20) + 'px';
  newItem.style.top = (e.offsetY - 20) + 'px';
  newItem.draggable = true;
  newItem.addEventListener('dragstart', dragStart);
  canvas.appendChild(newItem);
});

document.querySelectorAll('.palette span').forEach(span => {
  span.addEventListener('dragstart', (e) => {
    e.dataTransfer.setData('text/plain', e.target.textContent);
  });
});

function dragStart(e) {
  e.dataTransfer.setData('text/plain', e.target.textContent);
}
</script>
"""

st.components.v1.html(html_code, height=600)

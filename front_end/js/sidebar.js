const btn = document.getElementById('btn_burger');
const sidebar = document.getElementById('aside');
document.addEventListener("DOMContentLoaded", function() {
    sidebar.classList.toggle('active');
})
btn.onclick = function() {
    sidebar.classList.toggle('active');
  }; 
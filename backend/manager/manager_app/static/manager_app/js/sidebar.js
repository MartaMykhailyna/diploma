// const btn = document.getElementById('btn_burger');
// const sidebar = document.getElementById('aside');
// document.addEventListener("DOMContentLoaded", function() {
//     sidebar.classList.toggle('active');
// })
// btn.onclick = function() {
//     sidebar.classList.toggle('active');
//   }; 
const btn = document.getElementById('btn_burger');
const sidebar = document.getElementById('aside');

// Змінюємо клас "active" при кліку на кнопку
btn.onclick = function() {
  sidebar.classList.toggle('active');
};

// Змінюємо клас "active" при наведенні курсора на меню
sidebar.addEventListener("mouseenter", function() {
  sidebar.classList.add('active');
});

// Змінюємо клас "active" при відведенні курсора від меню
sidebar.addEventListener("mouseleave", function() {
  sidebar.classList.remove('active');
});


// // Находим основное изображение
// const mainImage = document.getElementById('mainImage');

// // Находим все миниатюры
// const thumbnails = document.querySelectorAll('.thumbnail');

// // Функция для изменения главного изображения при клике на миниатюру
// function changeMainImage(event) {
//   mainImage.src = event.target.src;
// }

// // Добавляем обработчик для каждой миниатюры
// thumbnails.forEach(thumbnail => {
//   thumbnail.addEventListener('click', changeMainImage);
// });

// Получаем элементы DOM
var modal = document.getElementById('myModal');
var btn = document.getElementById('openModalBtn');
var span = document.getElementsByClassName('close')[0];

// Открываем модальное окно при нажатии на кнопку
btn.onclick = function() {
  modal.style.display = 'block';
};

// Закрываем модальное окно при нажатии на крестик
span.onclick = function() {
  modal.style.display = 'none';
};

// Закрываем модальное окно при клике вне его области
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = 'none';
  }
};
const redHeader = document.querySelector('#red_header');
const headerElement = document.querySelector('header');

redHeader.addEventListener('click', function () {
  headerElement.style.color = '#FF0000';
});

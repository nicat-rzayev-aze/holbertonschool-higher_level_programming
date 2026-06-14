const redHeader = document.querySelector('#red_header');
const headerElement = document.querySelector('header');

redHeader.addEventListener('click', function () {
  headerElement.classList.add('red');
});

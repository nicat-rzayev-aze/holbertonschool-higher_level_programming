const updateHeader = document.querySelector('#update_header');
const headerElement = document.querySelector('header');

updateHeader.addEventListener('click', function () {
  headerElement.textContent = 'New Header!!!';
});

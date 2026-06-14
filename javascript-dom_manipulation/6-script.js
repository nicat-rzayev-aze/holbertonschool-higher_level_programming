const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
const characterElement = document.querySelector('#character');

fetch(url)
  .then(function (response) {
    return response.json();
  })
  .then(function (data) {
    characterElement.textContent = data.name;
  });

document.addEventListener('DOMContentLoaded', () => {
  const characterElement = document.querySelector('#character');

  if (!characterElement) {
    return;
  }

  const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';

  fetch(url)
    .then((response) => {
      if (!response.ok) {
        throw new Error('Network error');
      }
      return response.json();
    })
    .then((data) => {
      if (data && data.name) {
        characterElement.textContent = data.name;
      }
    })
    .catch(() => {
      // silently ignore errors
    });
});

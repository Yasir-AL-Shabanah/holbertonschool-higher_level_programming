document.addEventListener('DOMContentLoaded', () => {
  const listElement = document.querySelector('#list_movies');

  if (!listElement) {
    return;
  }

  const url = 'https://swapi-api.hbtn.io/api/films/?format=json';

  fetch(url)
    .then((response) => {
      if (!response.ok) {
        throw new Error('Network error');
      }
      return response.json();
    })
    .then((data) => {
      if (!data || !Array.isArray(data.results)) {
        return;
      }

      data.results.forEach((film) => {
        if (film && film.title) {
          const item = document.createElement('li');
          item.textContent = film.title;
          listElement.appendChild(item);
        }
      });
    })
    .catch(() => {
      // silently ignore errors
    });
});

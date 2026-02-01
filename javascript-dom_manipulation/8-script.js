document.addEventListener('DOMContentLoaded', () => {
  const helloElement = document.querySelector('#hello');

  if (!helloElement) {
    return;
  }

  const url = 'https://hellosalut.stefanbohacek.com/?lang=fr';

  fetch(url)
    .then((response) => {
      if (!response.ok) {
        throw new Error('Network error');
      }
      return response.json();
    })
    .then((data) => {
      if (data && data.hello) {
        helloElement.textContent = data.hello;
      }
    })
    .catch(() => {
      // silently ignore errors
    });
});

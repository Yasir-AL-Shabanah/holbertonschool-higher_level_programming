document.addEventListener('DOMContentLoaded', () => {
  const header = document.querySelector('header');
  const redHeader = document.querySelector('#red_header');

  if (!header || !redHeader) {
    return;
  }

  redHeader.addEventListener('click', () => {
    header.style.color = '#FF0000';
  });
});

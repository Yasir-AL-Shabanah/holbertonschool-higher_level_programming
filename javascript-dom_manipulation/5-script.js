document.addEventListener('DOMContentLoaded', () => {
  const header = document.querySelector('header');
  const updateHeader = document.querySelector('#update_header');

  if (!header || !updateHeader) {
    return;
  }

  updateHeader.addEventListener('click', () => {
    header.textContent = 'New Header!!!';
  });
});

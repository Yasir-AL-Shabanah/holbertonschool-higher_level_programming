document.addEventListener('DOMContentLoaded', () => {
  const addItem = document.querySelector('#add_item');
  const list = document.querySelector('.my_list');

  if (!addItem || !list) {
    return;
  }

  addItem.addEventListener('click', () => {
    const item = document.createElement('li');
    item.textContent = 'Item';
    list.appendChild(item);
  });
});

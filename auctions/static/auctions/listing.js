document.addEventListener('DOMContentLoaded', function () {
  // Use buttons to toggle between views
  document
    .querySelector('#description-heading')
    .addEventListener('click', () => loadTab('description'));
  document
    .querySelector('#bids-heading')
    .addEventListener('click', () => loadTab('bids'));
  document
    .querySelector('#comments-heading')
    .addEventListener('click', () => loadTab('comments'));
  // By default, load the description
  loadTab('description');
});

function loadTab(name) {
  document.querySelector('#description-tab').style.display = 'none';
  document.querySelector('#bids-tab').style.display = 'none';
  document.querySelector('#comments-tab').style.display = 'none';
  document.querySelector('#description-heading').style.backgroundColor =
    'inherit';
  document.querySelector('#bids-heading').style.backgroundColor = 'inherit';
  document.querySelector('#comments-heading').style.backgroundColor = 'inherit';

  if (name === 'description') {
    document.querySelector('#description-tab').style.display = 'block';
    document.querySelector('#description-heading').style.backgroundColor =
      'white';
  } else if (name == 'bids') {
    document.querySelector('#bids-tab').style.display = 'block';
    document.querySelector('#bids-heading').style.backgroundColor = 'white';
  } else if (name == 'comments') {
    document.querySelector('#comments-tab').style.display = 'block';
    document.querySelector('#comments-heading').style.backgroundColor = 'white';
  }
}

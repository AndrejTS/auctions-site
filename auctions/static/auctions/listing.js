function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    const cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === name + '=') {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

const csrftoken = getCookie('csrftoken');

try {
  document
    .querySelector('.watchlist-form')
    .addEventListener('submit', watchlist_switch);
} catch (error) {}

function watchlist_switch(e) {
  e.preventDefault();

  const listing_id = document.querySelector('#listing_id').value;
  const url = `/listing/${listing_id}/watchlist/`;
  const watchlistBtnText = document.querySelector('#watchlist-btn-text');

  fetch(url, {
    method: 'POST',
    mode: 'same-origin',
    headers: new Headers({ 'X-CSRFToken': csrftoken }),
  })
    .then((response) => response.json())
    .then((result) => {
      watchlistBtnText.style.opacity = 0;

      setTimeout(() => {
        watchlistBtnText.innerHTML = result['message'];
        watchlistBtnText.style.opacity = 1;
      }, 200);
    });
}

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

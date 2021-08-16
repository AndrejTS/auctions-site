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

async function watchlist_switch(e) {
  e.preventDefault();

  const listing_id = document.querySelector('#listing_id').value;
  const url = `/listing/${listing_id}/watchlist/`;
  const watchlistBtn = document.querySelector('.watchlist-btn');

  const response = await fetch(url, {
    method: 'POST',
    mode: 'same-origin',
    headers: new Headers({ 'X-CSRFToken': csrftoken }),
  });

  const result = await response.json();

  if (result['message'] === 'Added!') {
    watchlistBtn.innerHTML =
      '<svg xmlns="http://www.w3.org/2000/svg" fill="currentColor" class="bi bi-check2" viewBox="0 0 16 16"><path d="M13.854 3.646a.5.5 0 0 1 0 .708l-7 7a.5.5 0 0 1-.708 0l-3.5-3.5a.5.5 0 1 1 .708-.708L6.5 10.293l6.646-6.647a.5.5 0 0 1 .708 0z"/></svg><span id=\'watchlist-btn-text\'>Watching</span>';
  } else {
    watchlistBtn.innerHTML =
      "<span id='watchlist-btn-text'>Add to watchlist</span>";
  }
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
  document.querySelector('#description-heading').style.fontWeight = '400';
  document.querySelector('#bids-heading').style.backgroundColor = 'inherit';
  document.querySelector('#bids-heading').style.fontWeight = '400';
  document.querySelector('#comments-heading').style.backgroundColor = 'inherit';
  document.querySelector('#comments-heading').style.fontWeight = '400';

  if (name === 'description') {
    document.querySelector('#description-tab').style.display = 'block';
    document.querySelector('#description-heading').style.backgroundColor =
      'white';
    document.querySelector('#description-heading').style.fontWeight = '600';
  } else if (name == 'bids') {
    document.querySelector('#bids-tab').style.display = 'flex';
    document.querySelector('#bids-heading').style.backgroundColor = 'white';
    document.querySelector('#bids-heading').style.fontWeight = '600';
  } else if (name == 'comments') {
    document.querySelector('#comments-tab').style.display = 'block';
    document.querySelector('#comments-heading').style.backgroundColor = 'white';
    document.querySelector('#comments-heading').style.fontWeight = '600';
  }
}

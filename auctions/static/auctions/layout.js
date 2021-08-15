// Account menu
const accountButton = document.querySelector('.account-control');
const menu = document.querySelector('.menu');

accountButton.addEventListener('click', () => {
  menu.classList.toggle('show');
});

document.addEventListener('click', (e) => {
  if (!menu.contains(e.target) && !accountButton.contains(e.target)) {
    menu.classList.remove('show');
  }
});

// Account menu mobile
const accountButtonMobile = document.querySelector('#menu-mobile-btn');

const menuMobile = document.querySelector('.menu-mobile');

const grayArea = document.querySelector('#menu-mobile-graying');

accountButtonMobile.addEventListener('click', () => {
  menuMobile.classList.toggle('menu-mobile--active');
  body.classList.toggle('lock-scroll');
});

grayArea.addEventListener('click', () => {
  menuMobile.classList.toggle('menu-mobile--active');
  body.classList.toggle('lock-scroll');
});

// Mobile navigation
const headerAndNavbar = document.getElementById('header-nav-wrapper');
const toggleButton = document.getElementById('nav-mobile-btn');
const navbarMobile = document.getElementById('nav-mobile');
const body = document.getElementsByTagName('body')[0];

toggleButton.addEventListener('click', () => {
  toggleButton.classList.toggle('nav--active');
  navbarMobile.classList.toggle('nav--active');
  if (!menuMobile.classList.contains('menu-mobile--active')) {
    body.classList.toggle('lock-scroll');
  }
});

let lastScrollTop = 0;
window.addEventListener('scroll', function () {
  let scrollTop = window.pageYOffset || document.documentElement.scrollTop;
  if (scrollTop > lastScrollTop) {
    headerAndNavbar.style.top = '-200px';
  } else {
    headerAndNavbar.style.top = '0';
  }
  lastScrollTop = scrollTop;
});

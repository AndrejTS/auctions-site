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

const accountButtonMobile = document.querySelector('#menu-mobile-btn');
const menuMobile = document.querySelector('.menu-mobile');

accountButtonMobile.addEventListener('click', () => {
  menuMobile.classList.toggle('menu-mobile--active');
  accountButtonMobile.classList.toggle('menu-mobile-btn--active');
  body.classList.toggle('lock-scroll');

  //   checkBodyLock();
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
  // Close also menuMobile (if visible)
  //   menuMobile.classList.remove('menu-mobile--active');

  //   checkBodyLock();
});

// function checkBodyLock() {
//   if (
//     !menuMobile.classList.contains('menu-mobile--active') &&
//     !navbarMobile.classList.contains('nav--active')
//   ) {
//     body.classList.remove('lock-scroll');
//   }
// }

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

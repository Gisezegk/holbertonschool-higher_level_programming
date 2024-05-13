const toggle = document.getElementById('toggle_header');
const header = document.querySelector('header');
toggle.addEventListener('click', function() {
  if (header.classList.contains('green')) {
    header.classList.remove('green');
    header.classList.add('red');
  } else {
    header.classList.remove('red');
    header.classList.add('green');
  }
});

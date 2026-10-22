const menu = document.getElementById('menu');
const nav = document.getElementById('nav');
menu.addEventListener('click', () => nav.classList.toggle('open'));
nav.querySelectorAll('a').forEach(link => link.addEventListener('click', () => nav.classList.remove('open')));
document.getElementById('year').textContent = new Date().getFullYear();
document.querySelectorAll('[data-project]').forEach(link => {
  link.addEventListener('click', () => {
    const subject = encodeURIComponent('Question about ' + link.dataset.project);
    document.getElementById('emailLink').href = 'mailto:your.email@example.com?subject=' + subject;
  });
});

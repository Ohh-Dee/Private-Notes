// Highlight active link by section in view
(function () {
  const navLinks = Array.from(document.querySelectorAll('.site-header nav a')).filter(a => a.hash);
  const sections = navLinks.map(a => document.querySelector(a.hash)).filter(Boolean);
  if (!sections.length) return;

  const io = new IntersectionObserver((entries) => {
    entries.forEach(e => {
      if (e.isIntersecting) {
        const id = '#' + e.target.id;
        navLinks.forEach(a => a.classList.toggle('active', a.hash === id));
      }
    });
  }, {
    root: document.querySelector('.snapwrap') || null,
    rootMargin: '-45% 0px -45% 0px',
    threshold: 0
  });

  sections.forEach(sec => io.observe(sec));
})();

// Reveal-on-scroll
(function () {
  const root = document.querySelector('.snapwrap') || null;
  const io = new IntersectionObserver((entries) => {
    entries.forEach(e => { if (e.isIntersecting) e.target.classList.add('in'); });
  }, { root, threshold: 0.12 });

  document.querySelectorAll('.reveal').forEach(el => io.observe(el));
})();

// Nav hover preview
(function () {
  const panel = document.getElementById('nav-preview');
  if (!panel) return;
  const img = panel.querySelector('img');
  const links = document.querySelectorAll('.site-header nav a[data-preview]');

  // Preload images
  links.forEach(a => { const i = new Image(); i.src = a.dataset.preview; });

  const show = (url, alt) => { if (url) { img.src = url; img.alt = alt || ''; panel.classList.add('show'); } };
  const hide = () => panel.classList.remove('show');

  links.forEach(a => {
    a.addEventListener('mouseenter', () => show(a.dataset.preview, a.textContent.trim()));
    a.addEventListener('mouseleave', hide);
    a.addEventListener('focus', () => show(a.dataset.preview, a.textContent.trim()));
    a.addEventListener('blur', hide);
  });

  const root = document.querySelector('.snapwrap') || window;
  root.addEventListener('scroll', hide, { passive: true });
})();

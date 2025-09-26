// Highlight active nav link based on the section in view
(function () {
  const navLinks = Array.from(document.querySelectorAll('.site-header nav a'))
    .filter(a => a.hash);

  const sections = navLinks
    .map(a => document.querySelector(a.hash))
    .filter(Boolean);

  if (sections.length) {
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
  }
})();

// Reveal-on-scroll (subtle fade/slide in)
(function () {
  const root = document.querySelector('.snapwrap') || null;
  const io = new IntersectionObserver((entries) => {
    entries.forEach(e => { if (e.isIntersecting) e.target.classList.add('in'); });
  }, { root, threshold: 0.12 });

  document.querySelectorAll('.reveal').forEach(el => io.observe(el));
})();

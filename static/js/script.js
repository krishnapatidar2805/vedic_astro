document.addEventListener('DOMContentLoaded', function () {

  // ---- Scroll progress bar ----
  const progressBar = document.getElementById('scrollProgress');
  window.addEventListener('scroll', function () {
    if (progressBar) {
      const winScroll = document.body.scrollTop || document.documentElement.scrollTop;
      const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
      const scrolled = height > 0 ? (winScroll / height) * 100 : 0;
      progressBar.style.width = scrolled + '%';
    }
  });

  // ---- Navbar scrolled class ----
  const mainNav = document.getElementById('mainNav');
  window.addEventListener('scroll', function () {
    if (window.scrollY > 40) {
      mainNav && mainNav.classList.add('scrolled');
    } else {
      mainNav && mainNav.classList.remove('scrolled');
    }
  });

  // ---- Page loader ----
  const loader = document.getElementById('page-loader');
  window.addEventListener('load', function () {
    setTimeout(function () {
      if (loader) loader.classList.add('hide');
    }, 350);
  });

  // ---- Scroll to top button ----
  const scrollBtn = document.getElementById('scrollTopBtn');
  window.addEventListener('scroll', function () {
    if (window.scrollY > 300) {
      scrollBtn && scrollBtn.classList.add('show');
    } else {
      scrollBtn && scrollBtn.classList.remove('show');
    }
  });
  if (scrollBtn) {
    scrollBtn.addEventListener('click', function () {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }

  // ---- Navbar active link highlight ----
  const currentPath = window.location.pathname;
  document.querySelectorAll('.nav-link').forEach(function (link) {
    if (link.getAttribute('href') === currentPath) {
      link.classList.add('active');
    }
  });

  // ---- Simple fade-in-on-scroll animation ----
  const animatedEls = document.querySelectorAll('.service-card, .blog-card, .review-card, .gallery-item, .dashboard-card');
  const observer = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      if (entry.isIntersecting) {
        entry.target.style.opacity = 1;
        entry.target.style.transform = 'translateY(0)';
      }
    });
  }, { threshold: 0.1 });

  animatedEls.forEach(function (el) {
    el.style.opacity = 0;
    el.style.transform = 'translateY(24px)';
    el.style.transition = 'opacity .6s ease, transform .6s ease';
    observer.observe(el);
  });

  // ---- Bootstrap tooltips (if any) ----
  const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
  tooltipTriggerList.forEach(function (el) {
    new bootstrap.Tooltip(el);
  });

  // ---- Sacred Vedic Mantra Audio Player ----
  /* ── THEME TOGGLE (LIGHT / DARK MODE) ── */
  const themeToggleBtn = document.getElementById('themeToggleBtn');
  
  function applyTheme(theme) {
    document.documentElement.setAttribute('data-theme', theme);
    localStorage.setItem('site-theme', theme);
  }

  if (themeToggleBtn) {
    themeToggleBtn.addEventListener('click', function (e) {
      e.preventDefault();
      const currentTheme = document.documentElement.getAttribute('data-theme') || 'dark';
      const newTheme = currentTheme === 'light' ? 'dark' : 'light';
      applyTheme(newTheme);
    });
  }
});

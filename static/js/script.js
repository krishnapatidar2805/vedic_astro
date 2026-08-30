document.addEventListener('DOMContentLoaded', function () {

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
  const mantraWidget = document.getElementById('mantraPlayer');
  const mantraLabel = document.querySelector('.mantra-label');
  const sacredAudio = document.getElementById('sacredAudio');

  let audioCtx = null;
  let synthNodes = null;
  let isPlaying = false;

  function startOmSynth() {
    try {
      const AudioCtxClass = window.AudioContext || window.webkitAudioContext;
      audioCtx = new AudioCtxClass();
      const now = audioCtx.currentTime;

      // Cosmic Om Frequency (136.1 Hz) + Harmonics (272.2Hz, 408.3Hz, 432Hz)
      const freqs = [136.1, 272.2, 408.3, 432.0];
      const masterGain = audioCtx.createGain();
      masterGain.gain.setValueAtTime(0, now);
      masterGain.gain.linearRampToValueAtTime(0.18, now + 1.5);
      masterGain.connect(audioCtx.destination);

      const oscillators = freqs.map(function (f, idx) {
        const osc = audioCtx.createOscillator();
        const g = audioCtx.createGain();
        osc.type = idx === 0 ? 'sine' : (idx % 2 === 0 ? 'triangle' : 'sine');
        osc.frequency.setValueAtTime(f, now);

        // Subtle vibrating frequency modulation
        const lfo = audioCtx.createOscillator();
        const lfoGain = audioCtx.createGain();
        lfo.frequency.setValueAtTime(0.25 + idx * 0.1, now);
        lfoGain.gain.setValueAtTime(1.8, now);
        lfo.connect(lfoGain);
        lfoGain.connect(osc.frequency);
        lfo.start();

        g.gain.setValueAtTime(1 / (idx + 1.6), now);
        osc.connect(g);
        g.connect(masterGain);
        osc.start();
        return osc;
      });

      synthNodes = { masterGain: masterGain, oscillators: oscillators };
    } catch (e) {
      console.warn("Web Audio not supported", e);
    }
  }

  function stopOmSynth() {
    if (audioCtx && synthNodes) {
      try {
        const now = audioCtx.currentTime;
        synthNodes.masterGain.gain.linearRampToValueAtTime(0, now + 0.8);
        setTimeout(function () {
          if (audioCtx) {
            audioCtx.close();
            audioCtx = null;
            synthNodes = null;
          }
        }, 1000);
      } catch (e) {}
    }
  }

  if (mantraWidget) {
    mantraWidget.addEventListener('click', function (e) {
      e.preventDefault();
      if (!isPlaying) {
        isPlaying = true;
        mantraWidget.classList.add('playing');
        if (mantraLabel) mantraLabel.textContent = 'Pause Chant';

        if (sacredAudio) {
          sacredAudio.volume = 0.45;
          const playPromise = sacredAudio.play();
          if (playPromise !== undefined) {
            playPromise.catch(function () {
              // Fallback to Web Audio synthesis if external audio file is blocked
              startOmSynth();
            });
          }
        } else {
          startOmSynth();
        }
      } else {
        isPlaying = false;
        mantraWidget.classList.remove('playing');
        if (mantraLabel) mantraLabel.textContent = 'Play Sacred Om';

        if (sacredAudio) {
          sacredAudio.pause();
        }
        stopOmSynth();
      }
    });
  }

  // ---- Cosmic Starfield Canvas Animation ----
  const canvas = document.getElementById('cosmicStarfield');
  if (canvas && canvas.parentElement) {
    const ctx = canvas.getContext('2d');
    let width, height, stars = [];

    function resize() {
      if (!canvas || !canvas.parentElement) return;
      width = canvas.width = canvas.parentElement.offsetWidth;
      height = canvas.height = canvas.parentElement.offsetHeight;
      stars = [];
      const count = Math.floor((width * height) / 8500);
      for (let i = 0; i < count; i++) {
        stars.push({
          x: Math.random() * width,
          y: Math.random() * height,
          radius: Math.random() * 1.6 + 0.4,
          alpha: Math.random() * 0.8 + 0.2,
          speed: Math.random() * 0.015 + 0.005,
          color: Math.random() > 0.35 ? '#d4af37' : '#ffffff'
        });
      }
    }
    resize();
    window.addEventListener('resize', resize);

    function animate() {
      if (!ctx) return;
      ctx.clearRect(0, 0, width, height);
      for (let s of stars) {
        s.alpha += s.speed;
        if (s.alpha > 0.95 || s.alpha < 0.2) s.speed = -s.speed;
        ctx.beginPath();
        ctx.arc(s.x, s.y, s.radius, 0, Math.PI * 2);
        ctx.fillStyle = s.color === '#d4af37' ? `rgba(212, 175, 55, ${s.alpha})` : `rgba(255, 255, 255, ${s.alpha * 0.7})`;
        ctx.shadowBlur = 5;
        ctx.shadowColor = s.color;
        ctx.fill();
      }
      requestAnimationFrame(animate);
    }
    animate();
  }

  // ---- Interactive 12-Rashi Chakra Logic ----
  const rashiBtns = document.querySelectorAll('.rashi-btn');
  const rashiCard = document.getElementById('rashiDisplayCard');
  const glyphEl = document.getElementById('rashiGlyph');
  const nameEl = document.getElementById('rashiName');
  const planetEl = document.getElementById('rashiPlanet');
  const elementEl = document.getElementById('rashiElement');
  const gemEl = document.getElementById('rashiGem');
  const colorEl = document.getElementById('rashiColor');
  const mantraEl = document.getElementById('rashiMantra');
  const descEl = document.getElementById('rashiDesc');

  if (rashiBtns.length > 0 && rashiCard) {
    rashiCard.style.transition = 'opacity 0.22s ease, transform 0.22s ease';
    rashiBtns.forEach(function (btn) {
      btn.addEventListener('click', function () {
        rashiBtns.forEach(function(b) { b.classList.remove('active'); });
        btn.classList.add('active');

        // Smooth transition effect
        rashiCard.style.opacity = '0';
        rashiCard.style.transform = 'scale(0.96)';

        setTimeout(function () {
          if (glyphEl) glyphEl.textContent = btn.dataset.glyph || '♈';
          if (nameEl) nameEl.textContent = btn.dataset.name || '';
          if (planetEl) planetEl.textContent = btn.dataset.planet || '';
          if (elementEl) elementEl.textContent = btn.dataset.element || '';
          if (gemEl) gemEl.textContent = btn.dataset.gem || '';
          if (colorEl) colorEl.textContent = btn.dataset.color || '';
          if (mantraEl) mantraEl.textContent = btn.dataset.mantra || '';
          if (descEl) descEl.textContent = btn.dataset.desc || '';

          rashiCard.style.opacity = '1';
          rashiCard.style.transform = 'scale(1)';
        }, 150);
      });
    });
  }

  // ---- Sacred Temple Bell Chime (Web Audio API) ----
  function playTempleBell() {
    try {
      const AudioCtxClass = window.AudioContext || window.webkitAudioContext;
      const ctx = new AudioCtxClass();
      const now = ctx.currentTime;

      // Temple Bell frequencies (528Hz divine harmonic)
      const freqs = [528, 1056, 1584];
      const master = ctx.createGain();
      master.gain.setValueAtTime(0.18, now);
      master.gain.exponentialRampToValueAtTime(0.0001, now + 2.5);
      master.connect(ctx.destination);

      freqs.forEach(function (freq, idx) {
        const osc = ctx.createOscillator();
        const g = ctx.createGain();
        osc.type = 'sine';
        osc.frequency.setValueAtTime(freq, now);

        g.gain.setValueAtTime(0.25 / (idx + 1), now);
        g.gain.exponentialRampToValueAtTime(0.0001, now + (2.3 - idx * 0.4));
        osc.connect(g);
        g.connect(master);
        osc.start(now);
        osc.stop(now + 2.6);
      });
    } catch (e) {}
  }

  document.querySelectorAll('.temple-chime-btn').forEach(function (btn) {
    btn.addEventListener('click', function () {
      playTempleBell();
    });
  });

});

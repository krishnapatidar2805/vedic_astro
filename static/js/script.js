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

});

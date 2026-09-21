import re

with open('static/css/reference_style.css', 'r', encoding='utf-8') as f:
    ref_css = f.read()

# Custom Astrological & Sub-page extensions matching Dark Cyber Luxury Glass UI
astro_addon = """
/* ═══════════════════════════════════════════════════════════════════════
   VEDIC ASTROLOGY SPECIFIC COMPONENTS (Dark Luxury Glass Integration)
   ═══════════════════════════════════════════════════════════════════════ */

/* ── PAGE LOADER ── */
#page-loader {
  position: fixed;
  inset: 0;
  z-index: 99999;
  background: var(--bg-dark);
  display: flex;
  align-items: center;
  justify-content: center;
  transition: opacity .6s ease, visibility .6s ease;
}
#page-loader.hide { opacity: 0; visibility: hidden; }
.om-loader {
  font-size: 4.5rem;
  background: var(--grad-text-gold);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  animation: pulseOm 1.8s infinite ease-in-out;
  text-shadow: 0 0 35px rgba(245, 158, 11, 0.6);
}
@keyframes pulseOm {
  0%, 100% { transform: scale(0.9); opacity: 0.7; }
  50% { transform: scale(1.15); opacity: 1; filter: drop-shadow(0 0 20px #F59E0B); }
}

/* ── HERO ASTROLOGER PHOTO ── */
.hero-photo-wrap {
  position: relative;
  text-align: center;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 20px;
}
.hero-photo-frame {
  position: relative;
  display: inline-block;
  width: 400px;
  height: 400px;
  border-radius: 50%;
  padding: 7px;
  background: linear-gradient(135deg, #FDE68A 0%, #F59E0B 50%, #6366F1 100%);
  box-shadow: 0 0 50px rgba(245, 158, 11, 0.45), 0 20px 45px rgba(0, 0, 0, 0.85);
  transition: transform 0.4s var(--ease);
}
.hero-photo-frame::before {
  content: '';
  position: absolute;
  inset: -12px;
  border-radius: 50%;
  border: 2px dashed rgba(245, 158, 11, 0.55);
  animation: rotateFrame 24s linear infinite;
  pointer-events: none;
}
@keyframes rotateFrame {
  from { transform: rotate(0deg); }
  to { transform: rotate(360deg); }
}
.hero-photo-box {
  width: 100%;
  height: 100%;
  border-radius: 50%;
  overflow: hidden;
  border: 4px solid var(--bg-dark);
  background: linear-gradient(180deg, #6c8ebf 0%, #8eaed9 35%, #bdd3f0 70%, #ffffff 100%);
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
}
.hero-photo-box img {
  width: 100%;
  height: 100%;
  object-fit: contain;
  transform: scale(1.36);
  object-position: center 30%;
  display: block;
  transition: transform .4s ease;
}
.hero-photo-frame:hover .hero-photo-box img {
  transform: scale(1.40);
}
.hero-photo-badge {
  position: absolute;
  bottom: 12px;
  right: 15px;
  background: rgba(15, 23, 42, 0.95);
  color: #FDE68A;
  border: 1.5px solid #F59E0B;
  padding: 8px 18px;
  border-radius: var(--radius-full);
  font-weight: 700;
  font-size: 0.85rem;
  box-shadow: 0 10px 25px rgba(0,0,0,0.6);
  z-index: 3;
  backdrop-filter: blur(8px);
}
.hero-photo-badge i { color: #F59E0B; margin-right: 6px; }

/* ── SACRED OM AUDIO PLAYER ── */
.mantra-widget {
  position: fixed;
  left: 26px;
  bottom: 30px;
  z-index: 999;
  display: flex;
  align-items: center;
  gap: 10px;
  background: rgba(15, 23, 42, 0.9);
  border: 1.5px solid rgba(245, 158, 11, 0.6);
  padding: 6px 18px 6px 8px;
  border-radius: 40px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.6), 0 0 20px rgba(245, 158, 11, 0.25);
  backdrop-filter: blur(12px);
  cursor: pointer;
  transition: all .35s ease;
}
.mantra-widget:hover {
  transform: translateY(-3px);
  border-color: #FBBF24;
  box-shadow: 0 14px 35px rgba(0, 0, 0, 0.7), 0 0 30px rgba(245, 158, 11, 0.45);
}
.mantra-btn {
  width: 42px;
  height: 42px;
  border-radius: 50%;
  background: var(--grad-amber);
  border: none;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #0F172A;
  font-size: 1.3rem;
  font-weight: 800;
  box-shadow: 0 4px 12px rgba(245, 158, 11, 0.4);
  cursor: pointer;
}
.mantra-widget.playing .mantra-btn {
  animation: pulseGold 2s infinite ease-in-out;
}
@keyframes pulseGold {
  0%, 100% { box-shadow: 0 0 0 0 rgba(245, 158, 11, 0.7); }
  50% { box-shadow: 0 0 0 12px rgba(245, 158, 11, 0); }
}
.mantra-label {
  color: #FDE68A;
  font-size: 0.85rem;
  font-weight: 600;
  letter-spacing: 0.5px;
  white-space: nowrap;
  user-select: none;
}
.sound-wave {
  display: none;
  align-items: center;
  gap: 3px;
  height: 16px;
  margin-left: 2px;
}
.mantra-widget.playing .sound-wave {
  display: inline-flex;
}
.sound-wave span {
  width: 3px;
  height: 100%;
  background: #FBBF24;
  border-radius: 3px;
  animation: waveBar 1.2s infinite ease-in-out;
}
.sound-wave span:nth-child(1) { animation-delay: 0.1s; }
.sound-wave span:nth-child(2) { animation-delay: 0.3s; }
.sound-wave span:nth-child(3) { animation-delay: 0.2s; }
.sound-wave span:nth-child(4) { animation-delay: 0.4s; }
@keyframes waveBar {
  0%, 100% { transform: scaleY(0.25); }
  50% { transform: scaleY(1); }
}

/* ── NAV SEARCH BAR ── */
.nav-search {
  position: relative;
  min-width: 170px;
}
.nav-search input {
  background: rgba(255, 255, 255, 0.05) !important;
  border: 1px solid rgba(255, 255, 255, 0.12) !important;
  color: #FFFFFF !important;
  border-radius: var(--radius-full) !important;
  padding: 6px 36px 6px 14px !important;
  font-size: 0.82rem !important;
}
.nav-search input:focus {
  border-color: #818CF8 !important;
  box-shadow: 0 0 15px rgba(99, 102, 241, 0.3) !important;
  background: rgba(15, 23, 42, 0.9) !important;
}
.nav-search button {
  position: absolute;
  right: 4px;
  top: 50%;
  transform: translateY(-50%);
  background: transparent;
  border: none;
  color: #A5B4FC;
  padding: 4px 8px;
}
.nav-search button:hover { color: #FFFFFF; }

/* ── FESTIVALS & VRAT PAGE ── */
.festival-card {
  background: var(--grad-card);
  border: 1px solid var(--border-glass);
  border-radius: var(--radius);
  padding: 26px;
  box-shadow: var(--shadow-md);
  transition: all 0.35s var(--ease);
}
.festival-card:hover {
  transform: translateY(-6px);
  border-color: rgba(245, 158, 11, 0.4);
  box-shadow: 0 15px 35px rgba(0, 0, 0, 0.6), 0 0 20px rgba(245, 158, 11, 0.2);
}
.festival-icon {
  width: 50px;
  height: 50px;
  border-radius: 14px;
  background: rgba(245, 158, 11, 0.12);
  border: 1px solid rgba(245, 158, 11, 0.3);
  color: #FBBF24;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.4rem;
  flex-shrink: 0;
}
.festival-name {
  color: #FFFFFF;
  font-size: 1.25rem;
  font-weight: 700;
}
.festival-tithi {
  font-size: 0.85rem;
  color: var(--text-muted);
}
.festival-badge {
  background: rgba(245, 158, 11, 0.15);
  color: #FDE68A;
  border: 1px solid rgba(245, 158, 11, 0.35);
  padding: 4px 12px;
  border-radius: var(--radius-full);
  font-size: 0.75rem;
  font-weight: 700;
  white-space: nowrap;
}
.festival-date-highlight {
  background: rgba(255, 255, 255, 0.04);
  border: 1px solid var(--border-glass);
  padding: 8px 14px;
  border-radius: 10px;
  font-size: 0.88rem;
  color: #E2E8F0;
}
.festival-info-box {
  background: rgba(255, 255, 255, 0.02);
  padding: 10px 14px;
  border-radius: 10px;
  border-left: 3px solid #F59E0B;
}
.info-title {
  color: #FDE68A;
  font-size: 0.88rem;
  font-weight: 600;
  margin-bottom: 4px;
}
.festival-mantra-box {
  background: rgba(10, 16, 30, 0.95);
  color: #FDE68A;
  padding: 12px 16px;
  border-radius: 12px;
  border: 1px solid rgba(245, 158, 11, 0.35);
}
.mantra-tag {
  font-size: 0.7rem;
  text-transform: uppercase;
  letter-spacing: 1px;
  background: var(--grad-amber);
  color: #0F172A;
  font-weight: 800;
  padding: 3px 10px;
  border-radius: 6px;
  display: inline-block;
  margin-bottom: 6px;
}
.mantra-text {
  font-size: 0.95rem;
  color: #FFFFFF;
  letter-spacing: 0.5px;
}

/* ── FORMS, AUTH & DASHBOARD ── */
.form-card, .dashboard-card {
  background: var(--grad-card);
  border: 1px solid var(--border-glass);
  border-radius: var(--radius-lg);
  padding: 36px;
  box-shadow: var(--shadow-lg);
}
.dashboard-stat {
  background: linear-gradient(145deg, rgba(30, 27, 75, 0.9), rgba(15, 23, 42, 0.95));
  border: 1px solid rgba(99, 102, 241, 0.3);
  color: #FFFFFF;
  border-radius: var(--radius);
  padding: 24px;
  text-align: center;
}
.dashboard-stat .num {
  font-family: var(--ff-display);
  font-size: 2.2rem;
  font-weight: 800;
  color: #FBBF24;
}
.status-badge {
  padding: 4px 12px;
  border-radius: var(--radius-full);
  font-size: 0.78rem;
  font-weight: 700;
}
.status-pending { background: rgba(245, 158, 11, 0.2); color: #FCD34D; border: 1px solid rgba(245, 158, 11, 0.4); }
.status-confirmed { background: rgba(16, 185, 129, 0.2); color: #6EE7B7; border: 1px solid rgba(16, 185, 129, 0.4); }
.status-completed { background: rgba(99, 102, 241, 0.2); color: #A5B4FC; border: 1px solid rgba(99, 102, 241, 0.4); }
.status-cancelled { background: rgba(239, 68, 68, 0.2); color: #FCA5A5; border: 1px solid rgba(239, 68, 68, 0.4); }

/* ── BUTTON OVERRIDES FOR VEDIC LUXURY ── */
.btn-gold {
  background: var(--grad-amber);
  color: #0F172A !important;
  font-weight: 800;
  box-shadow: 0 4px 18px rgba(245, 158, 11, 0.35);
}
.btn-gold:hover {
  transform: translateY(-3px);
  box-shadow: 0 8px 25px rgba(245, 158, 11, 0.55);
  color: #0F172A !important;
}
.btn-outline-gold {
  border: 1.5px solid #F59E0B;
  color: #FCD34D !important;
  background: transparent;
}
.btn-outline-gold:hover {
  background: var(--grad-amber);
  color: #0F172A !important;
  box-shadow: 0 6px 20px rgba(245, 158, 11, 0.4);
}
.btn-navy {
  background: var(--grad-primary);
  color: #FFFFFF !important;
}
.btn-navy:hover {
  transform: translateY(-3px);
  box-shadow: 0 8px 25px rgba(139, 92, 246, 0.5);
  color: #FFFFFF !important;
}

/* ── RESPONSIVE TWEAKS ── */
@media (max-width: 991px) {
  .hero-photo-frame { width: 330px; height: 330px; }
  .hero-photo-wrap { margin-top: 30px; }
  .hero-stats { grid-template-columns: repeat(2, 1fr); }
  .promo-banner-wrap { margin-top: 80px; }
}
@media (max-width: 576px) {
  .hero-photo-frame { width: 270px; height: 270px; }
  .hero-photo-badge { bottom: -6px; right: 50%; transform: translateX(50%); white-space: nowrap; }
  .mantra-widget { left: 16px; bottom: 20px; padding: 5px 12px 5px 6px; }
  .mantra-btn { width: 36px; height: 36px; font-size: 1.1rem; }
  .mantra-label { font-size: 0.78rem; }
}
"""

combined_css = ref_css + "\n" + astro_addon

with open('static/css/style.css', 'w', encoding='utf-8') as f:
    f.write(combined_css)

print("Successfully merged and written static/css/style.css! Total bytes:", len(combined_css))

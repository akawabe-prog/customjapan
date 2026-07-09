/* CUSTOM JAPAN corporate v2 — scroll motion */

/* ---- loader failsafe (runs before anything that could throw) ---- */
(function () {
  var dismiss = function () {
    var l = document.getElementById('loader');
    if (l) l.classList.add('is-done');
  };
  // ライブラリ未読込・JSエラー時でも本文を覆い続けないよう保険で必ず解除
  window.addEventListener('load', function () { setTimeout(dismiss, 1000); });
  setTimeout(dismiss, 3500);
})();

/* ---- lightweight mobile menu (works even if GSAP/Lenis fail) ---- */
(function () {
  var header = document.getElementById('header');
  var menuBtn = document.getElementById('menuBtn');
  var mobileMenu = document.getElementById('mobileMenu');
  if (!menuBtn || !mobileMenu || !header) return;
  window.__cjCloseMenu = function () {
    header.classList.remove('is-menu-open');
    mobileMenu.classList.remove('is-open');
    menuBtn.setAttribute('aria-expanded', 'false');
  };
  menuBtn.addEventListener('click', function () {
    var open = mobileMenu.classList.toggle('is-open');
    header.classList.toggle('is-menu-open', open);
    menuBtn.setAttribute('aria-expanded', open ? 'true' : 'false');
  });
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') window.__cjCloseMenu();
  });
})();

(function () {
  if (typeof gsap === 'undefined' || typeof ScrollTrigger === 'undefined' || typeof Lenis === 'undefined') {
    // アニメーションライブラリが無くてもページは通常表示・スクロール可能
    return;
  }
  gsap.registerPlugin(ScrollTrigger);

  /* ---- Lenis smooth scroll ---- */
  const lenis = new Lenis({ lerp: 0.09, smoothWheel: true });
  window.lenis = lenis;
  lenis.on('scroll', ScrollTrigger.update);
  gsap.ticker.add((t) => lenis.raf(t * 1000));
  gsap.ticker.lagSmoothing(0);

  /* anchor links via lenis */
  document.querySelectorAll('a[href^="#"]').forEach((a) => {
    a.addEventListener('click', (e) => {
      const target = document.querySelector(a.getAttribute('href'));
      if (!target) return;
      e.preventDefault();
      if (window.__cjCloseMenu) window.__cjCloseMenu();
      lenis.scrollTo(target, { offset: 0, duration: 1.4 });
    });
  });

  /* ---- header state ---- */
  const header = document.getElementById('header');
  if (header) {
    ScrollTrigger.create({
      start: 'top -80',
      onUpdate: (self) => header.classList.toggle('is-scrolled', self.scroll() > 80),
    });
  }

  /* ---- mascot floater (back to top) ---- */
  const mascotTop = document.getElementById('mascotTop');
  if (mascotTop) {
    ScrollTrigger.create({
      start: 'top -600',
      onUpdate: (self) => mascotTop.classList.toggle('is-visible', self.scroll() > 600),
    });
    mascotTop.addEventListener('click', () => lenis.scrollTo(0, { duration: 1.6 }));
  }

  /* ---- loader → hero intro (top page only) ---- */
  const loader = document.getElementById('loader');
  const hasHero = !!document.querySelector('.hero');
  if (hasHero) {
    const heroTl = gsap.timeline({ paused: true });
    heroTl
      .to('.hero__line span', { y: 0, duration: 1.3, ease: 'power4.out', stagger: 0.14 })
      .to('.hero__eyebrow span', { y: 0, duration: 1, ease: 'power3.out' }, 0.25)
      .to('.hero__sub', { opacity: 1, duration: 1.2, ease: 'power2.out' }, 0.9)
      .to('.hero__desc', { opacity: 1, duration: 1.2, ease: 'power2.out' }, 1.1);

    window.addEventListener('load', () => {
      setTimeout(() => {
        if (loader) loader.classList.add('is-done');
        heroTl.play();
      }, 900);
    });

    gsap.to('.hero__video', { scale: 1, duration: 6, ease: 'power2.out' });
    gsap.to('.hero__video', {
      yPercent: 12,
      ease: 'none',
      scrollTrigger: { trigger: '.hero', start: 'top top', end: 'bottom top', scrub: true },
    });
    gsap.to('.hero__content', {
      opacity: 0,
      yPercent: -20,
      ease: 'none',
      scrollTrigger: { trigger: '.hero', start: 'top top', end: '70% top', scrub: true },
    });
  } else if (loader) {
    window.addEventListener('load', () => loader.classList.add('is-done'));
  }

  /* ---- generic reveal ---- */
  document.querySelectorAll('.reveal').forEach((el) => {
    gsap.to(el, {
      opacity: 1,
      y: 0,
      duration: 1.2,
      ease: 'power3.out',
      scrollTrigger: { trigger: el, start: 'top 86%' },
    });
  });

  /* ---- brand mosaic: clip reveal stagger ---- */
  if (document.querySelector('.brand-tile')) {
    gsap.set('.brand-tile', { opacity: 0, y: 60 });
    ScrollTrigger.batch('.brand-tile', {
      start: 'top 90%',
      onEnter: (batch) =>
        gsap.to(batch, { opacity: 1, y: 0, duration: 1.1, ease: 'power3.out', stagger: 0.1 }),
    });
  }

  /* ---- smart feature: subtle video parallax ---- */
  if (document.querySelector('.smart-feature__video')) {
    gsap.fromTo(
      '.smart-feature__video',
      { yPercent: -6 },
      {
        yPercent: 6,
        ease: 'none',
        scrollTrigger: { trigger: '.smart-feature', start: 'top bottom', end: 'bottom top', scrub: true },
      }
    );
  }

  /* ---- statement: char-by-char scrub ---- */
  document.querySelectorAll('.st-line').forEach((line) => {
    const text = line.textContent;
    line.textContent = '';
    [...text].forEach((ch) => {
      const s = document.createElement('span');
      s.className = 'char';
      s.textContent = ch;
      line.appendChild(s);
    });
  });
  if (document.querySelector('.statement .char')) {
    gsap.to('.statement .char', {
      opacity: 1,
      stagger: 0.06,
      ease: 'none',
      scrollTrigger: {
        trigger: '.statement__title',
        start: 'top 78%',
        end: 'bottom 45%',
        scrub: 0.6,
      },
    });
  }

  /* ---- numbers count up ---- */
  document.querySelectorAll('.count').forEach((el) => {
    const target = +el.dataset.count;
    const obj = { v: 0 };
    gsap.to(obj, {
      v: target,
      duration: 2,
      ease: 'power3.out',
      scrollTrigger: { trigger: el, start: 'top 85%' },
      onUpdate: () => (el.textContent = Math.round(obj.v).toLocaleString()),
    });
  });

  /* ---- business marquee ---- */
  const track = document.querySelector('.marquee-track');
  if (track) {
    gsap.to(track, { xPercent: -50, ease: 'none', duration: 38, repeat: -1 });
  }

  /* ---- horizontal scrollers: drag to scroll ---- */
  document.querySelectorAll('#eventsScroller, #strengthsScroller').forEach((scroller) => {
    let isDown = false, startX = 0, startLeft = 0, moved = 0;
    scroller.addEventListener('pointerdown', (e) => {
      isDown = true; moved = 0; startX = e.clientX; startLeft = scroller.scrollLeft;
      scroller.setPointerCapture(e.pointerId);
    });
    scroller.addEventListener('pointermove', (e) => {
      if (!isDown) return;
      moved = e.clientX - startX;
      if (Math.abs(moved) > 4) scroller.classList.add('is-dragging');
      scroller.scrollLeft = startLeft - moved;
    });
    ['pointerup', 'pointercancel'].forEach((ev) =>
      scroller.addEventListener(ev, () => { isDown = false; scroller.classList.remove('is-dragging'); })
    );
    // prevent click navigation after a drag
    scroller.addEventListener('click', (e) => {
      if (Math.abs(moved) > 6) { e.preventDefault(); }
    }, true);
  });

  /* ---- slider arrow nav ---- */
  document.querySelectorAll('.str-nav').forEach((nav) => {
    const track = document.getElementById(nav.dataset.scroller);
    if (!track) return;
    const step = () => {
      const card = track.querySelector('.str-card');
      const gap = parseFloat(getComputedStyle(track).columnGap || getComputedStyle(track).gap || 24) || 24;
      return card ? card.getBoundingClientRect().width + gap : track.clientWidth * 0.8;
    };
    const prev = nav.querySelector('[data-dir="prev"]');
    const next = nav.querySelector('[data-dir="next"]');
    const update = () => {
      const max = track.scrollWidth - track.clientWidth - 2;
      if (prev) prev.disabled = track.scrollLeft <= 2;
      if (next) next.disabled = track.scrollLeft >= max;
    };
    if (prev) prev.addEventListener('click', () => track.scrollBy({ left: -step(), behavior: 'smooth' }));
    if (next) next.addEventListener('click', () => track.scrollBy({ left: step(), behavior: 'smooth' }));
    track.addEventListener('scroll', update, { passive: true });
    window.addEventListener('resize', update);
    update();
  });

  /* ---- recruit bg parallax ---- */
  if (document.querySelector('.recruit__bg img')) {
    gsap.fromTo(
      '.recruit__bg img',
      { yPercent: -10 },
      {
        yPercent: 0,
        ease: 'none',
        scrollTrigger: { trigger: '.recruit', start: 'top bottom', end: 'bottom top', scrub: true },
      }
    );
  }

  /* ---- pause offscreen videos ---- */
  const vids = document.querySelectorAll('video[autoplay]');
  const io = new IntersectionObserver(
    (entries) =>
      entries.forEach((en) => {
        const v = en.target;
        if (en.isIntersecting) { v.play().catch(() => {}); } else { v.pause(); }
      }),
    { rootMargin: '200px' }
  );
  vids.forEach((v) => io.observe(v));
})();

/* Pinnacle Precision Defence — progressive enhancement only.
   Every page works with JS disabled; this adds nav menus, the homepage
   rotator, accordions, scroll reveal, and client-side form validation. */
(function () {
  'use strict';

  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* --- Desktop nav dropdowns ------------------------------------------- */
  function initNav() {
    var triggers = Array.prototype.slice.call(
      document.querySelectorAll('[data-nav-trigger]')
    );
    if (!triggers.length) return;

    function closeAll(except) {
      triggers.forEach(function (t) {
        if (t === except) return;
        t.setAttribute('aria-expanded', 'false');
        var p = document.getElementById(t.getAttribute('aria-controls'));
        if (p) p.removeAttribute('data-open');
      });
    }

    triggers.forEach(function (trigger) {
      var panel = document.getElementById(trigger.getAttribute('aria-controls'));
      if (!panel) return;
      var wrap = trigger.closest('.nav__item');
      var hideTimer;

      function open() {
        window.clearTimeout(hideTimer);
        closeAll(trigger);
        trigger.setAttribute('aria-expanded', 'true');
        panel.setAttribute('data-open', '');
      }
      function close() {
        trigger.setAttribute('aria-expanded', 'false');
        panel.removeAttribute('data-open');
      }
      function scheduleClose() {
        hideTimer = window.setTimeout(close, 160);
      }

      trigger.addEventListener('click', function (e) {
        e.preventDefault();
        trigger.getAttribute('aria-expanded') === 'true' ? close() : open();
      });
      wrap.addEventListener('mouseenter', open);
      wrap.addEventListener('mouseleave', scheduleClose);
      wrap.addEventListener('focusin', open);
      wrap.addEventListener('focusout', function (e) {
        if (!wrap.contains(e.relatedTarget)) close();
      });
    });

    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') closeAll(null);
    });
    document.addEventListener('click', function (e) {
      if (!e.target.closest('.nav__item')) closeAll(null);
    });
  }

  /* --- Mobile drawer --------------------------------------------------- */
  function initDrawer() {
    var burger = document.querySelector('[data-burger]');
    var drawer = document.getElementById('site-drawer');
    if (!burger || !drawer) return;

    burger.addEventListener('click', function () {
      var open = burger.getAttribute('aria-expanded') === 'true';
      burger.setAttribute('aria-expanded', String(!open));
      open ? drawer.removeAttribute('data-open') : drawer.setAttribute('data-open', '');
    });

    window.addEventListener('resize', function () {
      if (window.innerWidth > 980) {
        burger.setAttribute('aria-expanded', 'false');
        drawer.removeAttribute('data-open');
      }
    });
  }

  /* --- Homepage rotator ------------------------------------------------ */
  function initRotator() {
    var rotator = document.querySelector('[data-rotator]');
    if (!rotator) return;

    var tabs = Array.prototype.slice.call(rotator.querySelectorAll('[role="tab"]'));
    var panels = Array.prototype.slice.call(rotator.querySelectorAll('[role="tabpanel"]'));
    if (!tabs.length) return;

    var index = 0;
    var timer = null;
    var DWELL = 7000;

    function show(i, animate) {
      index = (i + tabs.length) % tabs.length;
      tabs.forEach(function (tab, n) {
        var on = n === index;
        tab.setAttribute('aria-selected', String(on));
        tab.setAttribute('tabindex', on ? '0' : '-1');
      });
      panels.forEach(function (panel, n) {
        panel.classList.remove('is-fading');
        n === index
          ? panel.setAttribute('data-active', '')
          : panel.removeAttribute('data-active');
      });
      if (animate) panels[index].classList.add('is-fading');
    }

    function start() {
      if (reduceMotion) return;
      stop();
      timer = window.setInterval(function () { show(index + 1, true); }, DWELL);
    }
    function stop() {
      if (timer) window.clearInterval(timer);
      timer = null;
    }

    tabs.forEach(function (tab, n) {
      tab.addEventListener('click', function () { show(n, true); stop(); });
      tab.addEventListener('keydown', function (e) {
        var next = { ArrowRight: 1, ArrowLeft: -1 }[e.key];
        if (!next) return;
        e.preventDefault();
        show(index + next, true);
        tabs[index].focus();
        stop();
      });
    });

    rotator.addEventListener('mouseenter', stop);
    rotator.addEventListener('mouseleave', start);
    rotator.addEventListener('focusin', stop);

    show(0);
    start();
  }

  /* --- Accordions ------------------------------------------------------ */
  function initAccordions() {
    document.querySelectorAll('[data-acc] .acc__btn').forEach(function (btn) {
      var body = document.getElementById(btn.getAttribute('aria-controls'));
      if (!body) return;
      btn.addEventListener('click', function () {
        var open = btn.getAttribute('aria-expanded') === 'true';
        btn.setAttribute('aria-expanded', String(!open));
        open ? body.removeAttribute('data-open') : body.setAttribute('data-open', '');
      });
    });
  }

  /* --- Scroll reveal --------------------------------------------------- */
  function initReveal() {
    var targets = document.querySelectorAll('[data-reveal]');
    if (!targets.length) return;

    if (reduceMotion || !('IntersectionObserver' in window)) {
      targets.forEach(function (el) { el.classList.add('is-in'); });
      return;
    }

    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        var el = entry.target;
        var delay = parseInt(el.getAttribute('data-reveal') || '0', 10);
        window.setTimeout(function () { el.classList.add('is-in'); }, delay);
        io.unobserve(el);
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });

    targets.forEach(function (el) { io.observe(el); });
  }

  /* --- Contact form ----------------------------------------------------
     No backend is wired up yet. Until an endpoint exists the form blocks
     submission and tells the operator, rather than silently losing an
     enquiry. See CONTENT-TODO.md ("Form endpoint").                     */
  function initForm() {
    var form = document.querySelector('[data-enquiry-form]');
    if (!form) return;
    var status = form.querySelector('[data-form-status]');

    form.addEventListener('submit', function (e) {
      if (form.getAttribute('action')) return; // real endpoint configured
      e.preventDefault();
      if (!form.checkValidity()) { form.reportValidity(); return; }
      if (status) {
        status.hidden = false;
        status.textContent =
          'This form has no submission endpoint configured yet. Please email ' +
          (form.getAttribute('data-fallback-email') || 'the enquiries address') +
          ' directly, or configure an endpoint before going live.';
        status.focus();
      }
    });
  }

  /* --- Footer year ----------------------------------------------------- */
  function initYear() {
    document.querySelectorAll('[data-year]').forEach(function (el) {
      el.textContent = String(new Date().getFullYear());
    });
  }

  function boot() {
    initNav();
    initDrawer();
    initRotator();
    initAccordions();
    initReveal();
    initForm();
    initYear();
  }

  document.readyState === 'loading'
    ? document.addEventListener('DOMContentLoaded', boot)
    : boot();
})();

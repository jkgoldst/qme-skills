(function () {
  var root = document.documentElement;

  // Theme toggle (persisted). Default follows prefers-color-scheme via CSS.
  var themeBtn = document.getElementById('theme-toggle');
  function isDark() {
    var t = root.dataset.theme;
    if (t) return t === 'dark';
    return window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
  }
  function syncThemeLabel() { themeBtn.textContent = isDark() ? 'Light' : 'Dark'; }
  themeBtn.addEventListener('click', function () {
    var next = isDark() ? 'light' : 'dark';
    root.dataset.theme = next;
    try { localStorage.setItem('qme-theme', next); } catch (e) {}
    syncThemeLabel();
  });
  syncThemeLabel();

  // Mobile nav
  var navBtn = document.getElementById('mobile-nav-toggle');
  var nav = document.getElementById('mobile-nav');
  navBtn.addEventListener('click', function () {
    var open = nav.hidden;
    nav.hidden = !open;
    navBtn.setAttribute('aria-expanded', String(open));
  });

  // Install tabs
  var tabs = Array.prototype.slice.call(document.querySelectorAll('.tab'));
  tabs.forEach(function (tab) {
    tab.addEventListener('click', function () {
      tabs.forEach(function (t) {
        var on = t === tab;
        t.classList.toggle('active', on);
        t.setAttribute('aria-selected', String(on));
        document.getElementById(t.getAttribute('aria-controls')).hidden = !on;
      });
    });
  });

  // Copy install command
  var copyBtn = document.getElementById('copy-install');
  var copyTimer;
  copyBtn.addEventListener('click', function () {
    var cmd = copyBtn.getAttribute('data-cmd');
    if (navigator.clipboard) navigator.clipboard.writeText(cmd).catch(function () {});
    copyBtn.textContent = 'Copied';
    clearTimeout(copyTimer);
    copyTimer = setTimeout(function () { copyBtn.textContent = 'Copy'; }, 1800);
  });
})();

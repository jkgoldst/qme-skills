(function () {
  var root = document.documentElement;
  var themeBtn = document.getElementById('theme-toggle');
  function isDark() {
    var theme = root.dataset.theme;
    if (theme) return theme === 'dark';
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

  var navBtn = document.getElementById('mobile-nav-toggle');
  var nav = document.getElementById('mobile-nav');
  navBtn.addEventListener('click', function () {
    var open = nav.hidden;
    nav.hidden = !open;
    navBtn.setAttribute('aria-expanded', String(open));
  });

  var tabs = Array.prototype.slice.call(document.querySelectorAll('.tab'));
  function activate(tab) {
    tabs.forEach(function (item) {
      var selected = item === tab;
      item.classList.toggle('active', selected);
      item.setAttribute('aria-selected', String(selected));
      item.tabIndex = selected ? 0 : -1;
      document.getElementById(item.getAttribute('aria-controls')).hidden = !selected;
    });
  }
  tabs.forEach(function (tab, index) {
    tab.addEventListener('click', function () { activate(tab); });
    tab.addEventListener('keydown', function (event) {
      var next;
      if (event.key === 'ArrowRight') next = (index + 1) % tabs.length;
      if (event.key === 'ArrowLeft') next = (index + tabs.length - 1) % tabs.length;
      if (event.key === 'Home') next = 0;
      if (event.key === 'End') next = tabs.length - 1;
      if (next === undefined) return;
      event.preventDefault();
      activate(tabs[next]);
      tabs[next].focus();
    });
  });

  var status = document.querySelector('.copy-status');
  document.querySelectorAll('.copy-install').forEach(function (button) {
    var timer;
    button.addEventListener('click', async function () {
      try {
        if (!navigator.clipboard) throw new Error('Clipboard unavailable');
        await navigator.clipboard.writeText(button.dataset.cmd);
        button.textContent = 'Copied';
        status.textContent = 'Install command copied.';
      } catch (e) {
        button.textContent = 'Copy failed';
        status.textContent = 'Could not copy. Select and copy the command above.';
      }
      clearTimeout(timer);
      timer = setTimeout(function () { button.textContent = 'Copy'; }, 1800);
    });
  });
})();

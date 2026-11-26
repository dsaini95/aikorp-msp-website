/* AIKorp site script: navigation, pricing toggle, contact form. */
{
  // ---- SETTINGS: paste a form endpoint (Formspree, Basin, Web3Forms, Power Automate HTTP trigger...) to receive enquiries.
  const FORM_ENDPOINT = '';

  // Mobile menu
  const burger = document.querySelector('.burger');
  const menu = document.querySelector('.menu');
  if (burger && menu) {
    burger.addEventListener('click', () => {
      const open = menu.classList.toggle('show');
      burger.setAttribute('aria-expanded', open);
    });
  }

  // Dropdowns (click / keyboard; hover handled in CSS on desktop)
  document.querySelectorAll('.has-drop > button').forEach(btn => {
    btn.addEventListener('click', e => {
      e.stopPropagation();
      const li = btn.parentElement;
      const open = li.classList.toggle('open');
      btn.setAttribute('aria-expanded', open);
    });
  });
  document.addEventListener('click', e => {
    document.querySelectorAll('.has-drop.open').forEach(li => {
      if (!li.contains(e.target)) { li.classList.remove('open'); li.querySelector('button').setAttribute('aria-expanded', 'false'); }
    });
  });
  document.addEventListener('keydown', e => {
    if (e.key === 'Escape') document.querySelectorAll('.has-drop.open').forEach(li => li.classList.remove('open'));
  });

  // Footer year
  document.querySelectorAll('[data-year]').forEach(el => { el.textContent = new Date().getFullYear(); });

  // Pricing toggle: monthly vs annual (annual = 10% off, rounded to the nearest ₹10)
  const toggle = document.querySelector('.toggle');
  if (toggle) {
    const set = mode => {
      toggle.querySelectorAll('button').forEach(b => b.setAttribute('aria-pressed', b.dataset.mode === mode));
      document.querySelectorAll('[data-monthly]').forEach(el => {
        const m = Number(el.dataset.monthly);
        const v = mode === 'annual' ? Math.round(m * 0.9 / 10) * 10 : m;
        el.textContent = '₹' + v.toLocaleString('en-IN');
      });
      document.querySelectorAll('[data-term]').forEach(el => { el.textContent = mode === 'annual' ? 'billed annually' : 'billed monthly'; });
    };
    toggle.addEventListener('click', e => { const b = e.target.closest('button'); if (b) set(b.dataset.mode); });
    set('monthly');
  }

  // Contact form
  const form = document.querySelector('#contact-form');
  if (form) {
    const msg = document.querySelector('#form-msg');
    // Prefill topic from ?plan= or #plan-name links
    const want = (location.hash || '').replace('#', '');
    const sel = form.querySelector('#topic');
    if (want && sel) [...sel.options].forEach(o => { if (o.value === want) sel.value = want; });

    form.addEventListener('submit', async e => {
      e.preventDefault();
      let ok = true;
      form.querySelectorAll('[required]').forEach(f => {
        const err = form.querySelector('#err-' + f.id);
        let bad = f.type === 'checkbox' ? !f.checked : !f.value.trim();
        if (!bad && f.type === 'email') bad = !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(f.value);
        if (err) err.textContent = bad ? (f.type === 'email' && f.value ? 'Please enter a valid email.' : 'Required') : '';
        if (bad) ok = false;
      });
      if (!ok) { form.querySelector('.err:not(:empty)')?.previousElementSibling?.focus?.(); return; }

      msg.classList.add('show');
      if (!FORM_ENDPOINT) {
        // No form service yet: hand the enquiry to the visitor's email app, with WhatsApp as a backup.
        const d = new FormData(form), g = k => (d.get(k) || '').toString().trim();
        const topic = form.querySelector('#topic');
        const topicTxt = topic ? topic.options[topic.selectedIndex].text : '';
        const bodyTxt = `Name: ${g('name')}\nCompany: ${g('company')}\nEmail: ${g('email')}\nPhone: ${g('phone')}\nUsers: ${g('users')}\nInterested in: ${topicTxt}\n\n${g('message')}`;
        location.href = 'mailto:support@aikorp.in?subject=' + encodeURIComponent('Website enquiry: ' + topicTxt + ' (' + g('company') + ')') + '&body=' + encodeURIComponent(bodyTxt);
        msg.innerHTML = 'Your email app should open with your request ready to send. If it does not, email <a href="mailto:support@aikorp.in">support@aikorp.in</a> or <a href="https://wa.me/918826158409?text=' + encodeURIComponent('Hi AIKorp, ' + topicTxt + ' for ' + g('company') + '. ' + g('message')) + '">send it on WhatsApp</a>.';
        return;
      }
      msg.textContent = 'Sending…';
      try {
        const r = await fetch(FORM_ENDPOINT, { method: 'POST', headers: { Accept: 'application/json' }, body: new FormData(form) });
        if (!r.ok) throw new Error(r.status);
        form.reset();
        msg.textContent = 'Thanks! Your request is in. We reply within one business day.';
      } catch {
        msg.textContent = 'Sorry, something went wrong. Please email us directly instead.';
      }
    });
  }
}

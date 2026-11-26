# AIKorp website

A static, multi-page marketing site for AIKorp (Microsoft 365-focused MSP). Plain HTML, CSS and JavaScript, no build step needed to host it.

## Pages
- index.html: Home
- services.html: all 8 services (with #anchors for each)
- pricing.html: per-user managed plans, comparison table, FAQ
- about.html, cases.html, blog.html, contact.html

## Before going live
1. **Contact details**: email (support@aikorp.in), phone/WhatsApp (+91 88261 58409) and city (New Delhi) are already set. To change them, edit the variables at the top of `tools/build.py` and run `python3 tools/build.py .` from this folder.
2. **Contact form**: set `FORM_ENDPOINT` at the top of `assets/main.js` to a form service URL (e.g. Formspree, Web3Forms, Basin, or a Power Automate HTTP trigger). Until then the form shows a "preview mode" notice and sends nothing.
3. **Prices**: the plan prices (₹799 / ₹1,499 / ₹2,499 per user per month, plus 18% GST) are suggestions. Change them in `tools/build.py` (PLANS) or in pricing.html (`data-monthly` attributes).
4. **Service commitments** on the home page (15 min response, 24/7 monitoring...) are promises to customers. Only keep the ones you can deliver.
5. **About / team**: replace placeholder profiles. **Case studies**: replace sample scenarios with real ones (with client permission). **Blog**: posts are marked "Coming soon".

## Microsoft trademark note
The site does not claim Microsoft Partner status or use Microsoft logos. Product names are used descriptively and the footer carries a trademark disclaimer. Keep it that way unless you join the Microsoft AI Cloud Partner Program.

## Hosting
Upload the folder to any static host: Azure Static Web Apps, Cloudflare Pages, Netlify, GitHub Pages, or regular web hosting.

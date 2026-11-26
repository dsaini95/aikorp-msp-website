#!/usr/bin/env python3
"""Generates the AIKorp static site pages into the output folder."""
import sys, os
OUT = sys.argv[1]

# ---------- placeholder business details (edit these) ----------
EMAIL = "support@aikorp.in"
PHONE = "+91 88261 58409"
TEL = "+918826158409"
WA = "https://wa.me/918826158409"
CITY = "New Delhi, India"
HOURS = "Mon to Sat, 9:00 to 19:00 IST"

# ---------- icons (original line icons) ----------
P = {
 'cloud': '<path d="M7 18a4.5 4.5 0 0 1-.6-9 6 6 0 0 1 11.4 1.5A3.8 3.8 0 0 1 17.5 18Z"/><path d="M12 16v-5m-2.2 2.2L12 11l2.2 2.2"/>',
 'chat': '<path d="M4 5h11a2 2 0 0 1 2 2v6a2 2 0 0 1-2 2H9l-4 3v-3H4a2 2 0 0 1-2-2V7a2 2 0 0 1 2-2Z"/><path d="M19 9h1a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-1v2.5L16 18h-3"/>',
 'laptop': '<rect x="4" y="5" width="16" height="11" rx="1.5"/><path d="M2 19h20M10 9.5l2 2 3-3"/>',
 'shield': '<path d="M12 3 4.5 6v5.5c0 4.6 3.1 8.2 7.5 9.5 4.4-1.3 7.5-4.9 7.5-9.5V6Z"/><path d="m9 12 2 2 4-4"/>',
 'backup': '<ellipse cx="12" cy="6" rx="7" ry="2.8"/><path d="M5 6v6c0 1.5 3.1 2.8 7 2.8M19 6v4"/><path d="M5 12v6c0 1.5 3.1 2.8 7 2.8"/><path d="M15.5 15.5a3.5 3.5 0 1 1 1 4.8M15.4 13.5v2.2h2.2"/>',
 'headset': '<path d="M4 14v-2a8 8 0 0 1 16 0v2"/><rect x="3" y="13" width="4" height="6" rx="1.5"/><rect x="17" y="13" width="4" height="6" rx="1.5"/><path d="M19 19c0 1.7-2 2.5-5 2.5"/>',
 'spark': '<path d="M12 3c.6 3.9 2.1 5.4 6 6-3.9.6-5.4 2.1-6 6-.6-3.9-2.1-5.4-6-6 3.9-.6 5.4-2.1 6-6Z"/><path d="M18.5 15c.3 1.7 1 2.3 2.5 2.5-1.6.3-2.2 1-2.5 2.5-.3-1.6-1-2.2-2.5-2.5 1.5-.2 2.2-.8 2.5-2.5Z"/>',
 'flow': '<rect x="3" y="3" width="6" height="6" rx="1.5"/><rect x="15" y="15" width="6" height="6" rx="1.5"/><rect x="15" y="3" width="6" height="6" rx="1.5"/><path d="M9 6h6M18 9v6M6 9v6a3 3 0 0 0 3 3h6"/>',
 'mail': '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3.5 6.5 8.5 6.5 8.5-6.5"/>',
 'folder': '<path d="M3 7a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2Z"/><path d="M8 13h8"/>',
 'key': '<circle cx="8" cy="15" r="4"/><path d="m11 12 8-8m-3 3 2 2m-4 0 1.5 1.5"/>',
 'lock': '<rect x="5" y="10" width="14" height="10" rx="2"/><path d="M8 10V7a4 4 0 0 1 8 0v3M12 14v2.5"/>',
 'check': '<path d="m5 12.5 4.5 4.5L19 7.5"/>',
 'phone': '<path d="M5 3h4l2 5-2.5 1.5a11 11 0 0 0 6 6L16 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 5a2 2 0 0 1 2-2Z"/>',
 'pin': '<path d="M12 21s-7-6.2-7-11.5a7 7 0 0 1 14 0C19 14.8 12 21 12 21Z"/><circle cx="12" cy="9.5" r="2.5"/>',
 'clock': '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
 'users': '<circle cx="9" cy="8" r="3.5"/><path d="M2.5 20a6.5 6.5 0 0 1 13 0M16 4.6a3.5 3.5 0 0 1 0 6.8M18 14a6.5 6.5 0 0 1 3.5 6"/>',
 'chart': '<path d="M4 20V10M10 20V4M16 20v-7M22 20H2"/>',
 'target': '<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1"/>',
 'handshake': '<path d="m11 17 2 2a1.5 1.5 0 0 0 2-2l-1-1m-3 1-2.5-2.5m2.5 2.5a1.5 1.5 0 0 1-2 2l-3-3a1.5 1.5 0 0 1 2-2m6 1 1 1a1.5 1.5 0 0 0 2-2l-4-4-2 1.5a2 2 0 0 1-2.5-3L13 5h3l5 5M3 10l5-5h3"/>',
 'wa': '<path d="M4 20l1.3-4.2A8.5 8.5 0 1 1 8.4 19Z"/><path d="M9 8.5c0 3.5 3 6.5 6.5 6.5l1-1.6-2-1-1 .8a4.5 4.5 0 0 1-2.2-2.2l.8-1-1-2Z"/>',
 'menu': '<path d="M4 7h16M4 12h16M4 17h16"/>',
 'chev': '<path d="m6 9 6 6 6-6"/>',
 'arrow': '<path d="M5 12h14m-6-6 6 6-6 6"/>',
}
def ic(name, cls=''):
    c = f' class="{cls}"' if cls else ''
    return f'<svg{c} viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{P[name]}</svg>'

LOGO = '''<svg viewBox="0 0 40 40" aria-hidden="true"><rect width="40" height="40" rx="11" fill="#0b3b40"/><path d="M11 29 19.2 11h1.6L29 29" fill="none" stroke="#fff" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round"/><path d="M14.8 22.5h10.4" stroke="#17b5a5" stroke-width="3.2" stroke-linecap="round"/><circle cx="30" cy="11" r="3.2" fill="#ff6a3d"/></svg>'''

SERVICES = [
 dict(slug='migration', icon='cloud', name='Microsoft 365 migration',
  short='Move email, files and users from Google Workspace, on-prem Exchange or another tenant with zero lost mail.',
  pts=['Discovery and migration plan','Google Workspace and IMAP moves','Exchange on-prem and hybrid cut-overs','Tenant-to-tenant moves after mergers','File server to SharePoint and OneDrive','Weekend cut-over with day-one support'],
  out='You get a written plan, a tested pilot group and a cut-over that happens outside working hours, so Monday morning just works.'),
 dict(slug='collaboration', icon='chat', name='Exchange, Teams and SharePoint',
  short='Set up and look after mail, meetings, chat and intranet the way your people actually work.',
  pts=['Exchange Online and mail flow','Teams structure, calling and meeting rooms','SharePoint intranet and document libraries','OneDrive known-folder move','Shared mailboxes and permissions','Governance and naming policies'],
  out='A tidy workspace where people can find files, external sharing is controlled, and nobody waits on IT for a new team or mailbox.'),
 dict(slug='endpoint', icon='laptop', name='Intune and endpoint management',
  short='Every laptop and phone enrolled, patched and compliant, from unboxing to retirement.',
  pts=['Windows Autopilot zero-touch setup','Intune compliance and configuration','App deployment and updates','iOS and Android device management','BitLocker and remote wipe','Patch reporting'],
  out='New starters open a box, sign in and are productive in minutes. Lost devices can be wiped in seconds.'),
 dict(slug='security', icon='shield', name='Security and compliance',
  short='Harden identity, email and devices with Defender, Entra ID and Purview, and keep watching.',
  pts=['MFA and Conditional Access','Defender for Business and Office 365','Phishing and spoofing protection','Secure Score improvement plan','Purview data loss prevention','Alert monitoring and response'],
  out='Fewer risky sign-ins, safer inboxes and a clear monthly view of where you stand and what we fixed.'),
 dict(slug='backup', icon='backup', name='Backup and recovery',
  short='Independent, third-party backup for mailboxes, OneDrive, SharePoint and Teams.',
  pts=['Daily automated backups','Point-in-time restores','Long-term retention options','Ransomware recovery runbook','Leaver mailbox archiving','Quarterly restore tests'],
  out='When a file is deleted, overwritten or encrypted, we get it back. Restores are tested, not assumed.'),
 dict(slug='helpdesk', icon='headset', name='Managed helpdesk',
  short='Friendly, fast support for your team by phone, email, Teams and portal.',
  pts=['Unlimited user support on managed plans','Onboarding and offboarding','Licence and admin changes','Remote fixes for M365 issues','Ticket portal and reporting','Named account manager'],
  out='One number to call and people who already know your setup. Every request is tracked and reported.'),
 dict(slug='copilot', icon='spark', name='Copilot and AI readiness',
  short='Get your data, permissions and people ready before you switch on Microsoft 365 Copilot.',
  pts=['Oversharing and permissions review','Sensitivity labels and data hygiene','Pilot group design','Prompt training workshops','Usage and value tracking','Responsible AI policy template'],
  out='Copilot only shows people what they should see, and your team knows how to get real value from it.'),
 dict(slug='power-platform', icon='flow', name='Power Platform and automation',
  short='Replace spreadsheets and manual steps with Power Apps, Power Automate and Power BI.',
  pts=['Approval and request workflows','Simple line-of-business apps','SharePoint list solutions','Power BI dashboards','Environment and DLP governance','Handover and training'],
  out='Hours of manual work removed each week, built on tools you already pay for.'),
]

NAV = [('index.html','Home'),('services.html','Services'),('pricing.html','Pricing'),('cases.html','Case studies'),('blog.html','Blog'),('about.html','About'),('contact.html','Contact')]

def header(cur):
    drop = ''.join(f'<a href="services.html#{s["slug"]}"><span class="ico">{ic(s["icon"])}</span><span><strong>{s["name"]}</strong><span>{s["short"].split(",")[0].split(" with")[0].rstrip(".")}.</span></span></a>' for s in SERVICES)
    items = []
    for href, label in NAV[2:]:
        cur_attr = ' aria-current="page"' if href == cur else ''
        items.append(f'<li><a href="{href}"{cur_attr}>{label}</a></li>')
    svc_cur = ' aria-current="page"' if cur == 'services.html' else ''
    return f'''<a class="skip" href="#main" style="position:absolute;left:-999px">Skip to content</a>
<header class="site-header"><div class="wrap nav">
  <a class="logo" href="index.html" aria-label="AIKorp home">{LOGO}<span>AI<b>Korp</b></span></a>
  <button class="burger" aria-label="Open menu" aria-expanded="false" aria-controls="menu">{ic('menu')}</button>
  <ul class="menu" id="menu">
    <li class="has-drop"><button aria-expanded="false" aria-haspopup="true"{svc_cur}>Services {ic('chev','chev')}</button>
      <div class="drop">{drop}</div></li>
    {''.join(items)}
    <li class="mobile-cta"><a class="btn btn-primary" href="contact.html">Book a call</a></li>
  </ul>
  <a class="btn btn-primary nav-cta" href="contact.html">Book a call</a>
</div></header>'''

def footer():
    svc = ''.join(f'<li><a href="services.html#{s["slug"]}">{s["name"]}</a></li>' for s in SERVICES[:6])
    return f'''<footer><div class="wrap">
  <div class="f-grid">
    <div><a class="logo" href="index.html">{LOGO}<span>AI<b>Korp</b></span></a>
      <p style="margin-top:16px;max-width:36ch">Managed IT for growing businesses, specialising in Microsoft 365. Migrate, secure, support.</p>
      <ul><li><a href="mailto:{EMAIL}">{EMAIL}</a></li><li><a href="tel:{TEL}">{PHONE}</a></li><li><a href="{WA}">WhatsApp: {PHONE}</a></li><li>{CITY}</li></ul></div>
    <div><h4>Services</h4><ul>{svc}<li><a href="services.html">All services</a></li></ul></div>
    <div><h4>Company</h4><ul><li><a href="about.html">About</a></li><li><a href="cases.html">Case studies</a></li><li><a href="blog.html">Blog</a></li><li><a href="contact.html">Contact</a></li></ul></div>
    <div><h4>Get started</h4><ul><li><a href="pricing.html">Managed plans</a></li><li><a href="contact.html#assessment">Free M365 health check</a></li><li><a href="contact.html">Book a call</a></li></ul></div>
  </div>
  <div class="f-bottom">
    <span>© <span data-year>2026</span> AIKorp. All rights reserved.</span>
    <span>AIKorp is an independent managed service provider and is not affiliated with, endorsed by, or a partner of Microsoft Corporation. Microsoft, Microsoft 365, Exchange, Teams, SharePoint, OneDrive, Intune, Entra, Defender, Purview, Copilot, Power Apps, Power Automate, Power BI and Power Platform are trademarks of the Microsoft group of companies. Product names are used only to describe the services we provide.</span>
  </div>
</div></footer>'''

def page(fname, title, desc, body):
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/styles.css">
<link rel="icon" href="data:image/svg+xml,{LOGO.replace('"', "'").replace('#', '%23').replace('<svg', '<svg xmlns=%27http://www.w3.org/2000/svg%27')}">
</head>
<body>
{header(fname)}
<main id="main">
{body}
</main>
{footer()}
<a class="wa-float" href="{WA}" aria-label="Chat with AIKorp on WhatsApp">{ic('wa')}<span>WhatsApp us</span></a>
<script src="assets/main.js"></script>
</body>
</html>
'''
    with open(os.path.join(OUT, fname), 'w') as f:
        f.write(html)

CTA = f'''<section class="band"><div class="wrap"><div class="cta-band">
  <div><h2>Get a free Microsoft 365 health check</h2><p>In 30 minutes we review your security settings, licences and backup, then send you a short report with quick wins. No obligation.</p></div>
  <a class="btn btn-primary" href="contact.html#assessment">Book my health check</a>
</div></div></section>'''

def checks(items):
    return '<ul class="checks">' + ''.join(f'<li>{ic("check")}<span>{t}</span></li>' for t in items) + '</ul>'

# ================= HOME =================
CHIPS = [('Exchange Online','mail','#1f6fd1'),('Teams','chat','#5b5fc7'),('SharePoint and OneDrive','folder','#0f8a8a'),('Intune','laptop','#2b7a3d'),('Entra ID','key','#0b5cad'),('Defender','shield','#c2410c'),('Purview','lock','#7c3aed'),('Copilot','spark','#d6336c'),('Power Platform','flow','#6d28d9')]
chips = ''.join(f'<span class="chip"><i style="background:{c}">{ic(i)}</i>{n}</span>' for n,i,c in CHIPS)
svc_cards = ''.join(f'<a class="card" href="services.html#{s["slug"]}"><span class="ico">{ic(s["icon"])}</span><h3>{s["name"]}</h3><p>{s["short"]}</p><span class="more">Learn more →</span></a>' for s in SERVICES)

home = f'''
<section class="hero"><div class="wrap hero-grid">
  <div>
    <h1>Microsoft 365, fully managed, <strong>so your team can just work.</strong></h1>
    <p class="lead">AIKorp is a managed service provider focused on Microsoft 365. We migrate, secure and support your email, files, devices and Teams for one predictable price per user.</p>
    <div class="hero-actions"><a class="btn btn-primary" href="contact.html">Book a call</a><a class="btn btn-ghost" href="pricing.html">See managed plans</a></div>
    <ul class="trust"><li>{ic('check')}Fixed per-user pricing</li><li>{ic('check')}Month-to-month option</li><li>{ic('check')}Security-first setup</li></ul>
  </div>
  <div class="console" role="img" aria-label="Illustration: AIKorp managing migration, security and helpdesk around a Microsoft 365 tenant">
    <div class="console-card">
      <svg class="lines" viewBox="0 0 100 100" preserveAspectRatio="none" aria-hidden="true">
        <g fill="none" stroke="rgba(255,255,255,.5)" stroke-width="1.3">
          <path d="M12 19 L28 30 L54 30" vector-effect="non-scaling-stroke"/>
          <path d="M82 45 L78 40 L67 40" vector-effect="non-scaling-stroke"/>
          <path d="M15 85 L24 80 L48 80" vector-effect="non-scaling-stroke"/>
        </g>
      </svg>
      <div class="core" style="left:10%;top:49%;width:70%"><small>AIKorp managed tenant</small><b>Microsoft 365, under control</b><div class="meter"><span class="dot"></span>Monitoring, backups and patching on</div></div>
    </div>
    <span class="lbl" style="left:59.5%;top:33.8%">Cloud migration</span>
    <span class="lbl" style="right:33%;top:42.4%">Security and compliance</span>
    <span class="lbl" style="left:54.5%;top:76.8%">Managed helpdesk</span>
    <span class="orb" style="left:2%;top:4%">{ic('cloud')}</span>
    <span class="orb o2" style="left:79%;top:44%">{ic('shield')}</span>
    <span class="orb o3" style="left:5%;top:70%">{ic('headset')}</span>
  </div>
</div></section>

<section class="strip"><div class="wrap">
  <p>The Microsoft 365 workloads we deploy, secure and support every day</p>
  <div class="chips">{chips}</div>
</div></section>

<section class="band"><div class="wrap">
  <div class="section-head"><div><span class="kicker">What we do</span><h2>Everything Microsoft 365, handled by one team</h2></div><p class="lead">From the first migration to everyday support, you get M365 experts who look after the whole stack, not just the tickets.</p></div>
  <div class="grid">{svc_cards}</div>
</div></section>

<section class="band alt"><div class="wrap split">
  <div>
    <span class="kicker">Why AIKorp</span>
    <h2>A focused MSP beats a generalist</h2>
    <p class="lead">We do one platform and do it deeply. That means faster fixes, safer configurations and advice you can act on.</p>
    {checks(['<strong>M365 experts, not generalists.</strong> Identity, mail, devices, security and automation, all in one place.','<strong>Security baseline on day one.</strong> MFA, Conditional Access, device compliance and backup are part of every plan.','<strong>Plain-English reporting.</strong> A monthly report showing what we fixed, what changed and what we recommend.','<strong>Independent advice.</strong> We are not tied to selling you licences, so we recommend only what you need.'])}
    <a class="btn btn-ghost" href="about.html">About us</a>
  </div>
  <div class="panel">
    <h3>Our service commitments</h3>
    <p style="margin:0">What every managed customer can count on.</p>
    <div class="stat-row">
      <div class="stat"><b>15 min</b><span>Response target for critical issues</span></div>
      <div class="stat"><b>24/7</b><span>Monitoring of alerts and backups</span></div>
      <div class="stat"><b>1 day</b><span>New starter set up, device to mailbox</span></div>
      <div class="stat"><b>Monthly</b><span>Health and security report</span></div>
    </div>
  </div>
</div></section>

<section class="band"><div class="wrap">
  <div class="center"><span class="kicker">How it works</span><h2>From first call to fully managed in four steps</h2><p class="lead">A clear, low-risk path for businesses of 5 to 500 users.</p></div>
  <div class="steps" style="margin-top:36px">
    <div class="step"><h3>Discovery call</h3><p>A 30-minute chat about your team, your tools and what is getting in the way.</p></div>
    <div class="step"><h3>Health check</h3><p>We review your tenant security, licences, devices and backup, and share findings.</p></div>
    <div class="step"><h3>Onboard and fix</h3><p>We document everything, close the security gaps and migrate what needs moving.</p></div>
    <div class="step"><h3>Managed for you</h3><p>Ongoing support, monitoring and monthly reviews, for a fixed per-user fee.</p></div>
  </div>
</div></section>
{CTA}
'''
page('index.html', 'AIKorp | Managed Microsoft 365 services', 'AIKorp is a managed service provider specialising in Microsoft 365: migration, security, Intune, backup, helpdesk and Copilot readiness.', home)

# ================= SERVICES =================
subnav = ''.join(f'<a href="#{s["slug"]}">{s["name"]}</a>' for s in SERVICES)
svc_blocks = ''.join(f'''<article class="svc" id="{s['slug']}">
  <div><span class="ico">{ic(s['icon'])}</span><h2>{s['name']}</h2><p class="lead">{s['short']}</p><a class="btn btn-primary" href="contact.html">Talk to an expert</a></div>
  <div><h3>What is included</h3><ul>{''.join(f"<li>{ic('check')}<span>{p}</span></li>" for p in s['pts'])}</ul><p class="outcome"><strong>What you get:</strong> {s['out']}</p></div>
</article>''' for s in SERVICES)
services = f'''
<section class="page-hero"><div class="wrap">
  <div class="crumbs"><a href="index.html">Home</a> / Services</div>
  <h1>Microsoft 365 services, end to end</h1>
  <p class="lead">Pick a single project or let us manage the lot. Every service is delivered by M365 specialists and documented so you always know how your environment is set up.</p>
</div></section>
<nav class="subnav" aria-label="Services"><div class="wrap scroll">{subnav}</div></nav>
<section><div class="wrap">{svc_blocks}</div></section>
{CTA}
'''
page('services.html', 'Services | AIKorp', 'Microsoft 365 migration, Exchange, Teams, SharePoint, Intune, security and compliance, backup, managed helpdesk, Copilot readiness and Power Platform.', services)

# ================= PRICING =================
PLANS = [
 dict(name='Essentials', price=799, slug='plan-essentials', for_='For small teams that need reliable support and the basics done right.',
  pts=['Helpdesk, business hours','Microsoft 365 admin and licence management','Onboarding and offboarding','MFA and security baseline','Monthly health report']),
 dict(name='Business', price=1499, slug='plan-business', pop=True, for_='Our most popular plan: full management of users, devices and security.',
  pts=['Everything in Essentials','Intune device management and patching','Defender for Business setup and monitoring','Email security and anti-phishing','Microsoft 365 cloud backup','24/7 support for critical issues']),
 dict(name='Secure+', price=2499, slug='plan-secure', for_='For regulated or security-conscious businesses that want more.',
  pts=['Everything in Business','Conditional Access hardening','Purview data loss prevention','Quarterly security and Secure Score reviews','Copilot readiness review','Virtual IT manager (vCIO) meetings']),
]
plans = ''.join(f'''<div class="plan{' pop' if p.get('pop') else ''}">{'<span class="tag">Most popular</span>' if p.get('pop') else ''}
  <h3>{p['name']}</h3><p class="for">{p['for_']}</p>
  <p class="price"><span data-monthly="{p['price']}">₹{p['price']:,}</span> <small>per user / month</small></p><p class="note" data-term>billed monthly</p>
  <ul>{''.join(f"<li>{ic('check')}<span>{x}</span></li>" for x in p['pts'])}</ul>
  <a class="btn {'btn-primary' if p.get('pop') else 'btn-ghost'}" href="contact.html#{p['slug']}">Choose {p['name']}</a>
</div>''' for p in PLANS)
ROWS = [('Helpdesk support','Business hours','Business hours + 24/7 critical','Business hours + 24/7 critical'),
 ('M365 user and licence admin','y','y','y'),('MFA and security baseline','y','y','y'),('Monthly report','y','y','y'),
 ('Intune device management','n','y','y'),('Patch management','n','y','y'),('Defender setup and monitoring','n','y','y'),
 ('Microsoft 365 backup','Add-on','y','y'),('Conditional Access hardening','n','Standard','Advanced'),
 ('Purview data loss prevention','n','n','y'),('Quarterly security review','n','n','y'),('vCIO strategy meetings','n','n','Quarterly')]
def cell(v):
    return {'y':'<td class="y" aria-label="Included">✓</td>','n':'<td class="n" aria-label="Not included">–</td>'}.get(v, f'<td>{v}</td>')
rows = ''.join('<tr><td>'+r[0]+'</td>'+''.join(cell(v) for v in r[1:])+'</tr>' for r in ROWS)
FAQ = [
 ('Are Microsoft 365 licences included?','No. Plan prices cover our management and support only. You can keep buying licences from Microsoft or your current reseller, and we will manage and right-size them for you so you never pay for seats you do not use.'),
 ('Is there a minimum contract?','Plans are available month to month. Annual agreements get a 10% discount. All prices are in Indian rupees and GST at 18% is added to every invoice. Onboarding projects are quoted separately as a fixed fee.'),
 ('What does onboarding cost?','It depends on the size and state of your environment. After the free health check we send a fixed-fee quote, so there are no surprises.'),
 ('Do you charge for migrations?','Migrations are fixed-fee projects quoted after discovery. Customers who join a managed plan get a discounted migration rate.'),
 ('Do you support on-site work?','We are remote-first, which keeps prices low. On-site visits within our area are available at an hourly rate.'),
 ('Are you a Microsoft Partner?','AIKorp is an independent MSP and is not a Microsoft Partner. Our team are Microsoft 365 specialists, and being independent means our advice is not shaped by sales targets.'),
]
faq = ''.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q,a in FAQ)
pricing = f'''
<section class="page-hero"><div class="wrap center">
  <div class="crumbs"><a href="index.html">Home</a> / Pricing</div>
  <h1>Simple, per-user managed plans</h1>
  <p class="lead">One predictable monthly price per user. Add or remove people as your team changes.</p>
  <div class="toggle" role="group" aria-label="Billing period"><button data-mode="monthly" aria-pressed="true">Monthly</button><button data-mode="annual" aria-pressed="false">Annual, save 10%</button></div>
</div></section>
<section style="padding-bottom:56px"><div class="wrap">
  <div class="plans">{plans}</div>
  <p class="note center" style="margin-top:20px">Prices in INR, excluding 18% GST and Microsoft licences. Minimum 5 users. Onboarding and migration projects are quoted separately.</p>
</div></section>
<section class="band alt"><div class="wrap">
  <h2>Compare plans</h2>
  <div class="scroll" style="margin-top:24px"><table class="cmp"><thead><tr><th>Feature</th><th>Essentials</th><th>Business</th><th>Secure+</th></tr></thead><tbody>{rows}</tbody></table></div>
</div></section>
<section class="band"><div class="wrap split" style="align-items:start">
  <div><h2>Projects and add-ons</h2><p class="lead">Need one thing done well? We also take on fixed-fee projects, with or without a managed plan.</p>
  {checks(['Microsoft 365 and tenant-to-tenant migrations','SharePoint intranet builds','Copilot readiness assessment and pilot','Power Platform apps and automations','Security assessment and remediation'])}
  <a class="btn btn-primary" href="contact.html">Request a quote</a></div>
  <div class="faq"><h2>Questions</h2>{faq}</div>
</div></section>
{CTA}
'''
page('pricing.html', 'Pricing | AIKorp', 'Per-user managed Microsoft 365 plans from AIKorp: Essentials, Business and Secure+.', pricing)

# ================= ABOUT =================
VALUES = [('target','Focused','We specialise in Microsoft 365, so we know it deeply and keep up with every change.'),
 ('shield','Secure by default','Every customer gets a hardened baseline. Security is never an upsell.'),
 ('handshake','Honest and independent','We recommend what you need, not what earns a commission.'),
 ('chart','Measurable','Monthly reports, clear SLAs and no jargon, so you see the value every month.')]
about = f'''
<section class="page-hero"><div class="wrap">
  <div class="crumbs"><a href="index.html">Home</a> / About</div>
  <h1>Your Microsoft 365 team, without the hiring</h1>
  <p class="lead">AIKorp was founded to give growing businesses the kind of Microsoft 365 expertise usually only large companies can afford, delivered by a small team that answers the phone.</p>
</div></section>
<section class="band"><div class="wrap split">
  <div><span class="kicker">Our mission</span><h2>Make Microsoft 365 secure, simple and productive for every small business</h2>
  <p class="lead">Most businesses use a fraction of what they pay for and leave security settings at their defaults. We close that gap with a clear plan, a strong baseline and ongoing care.</p>
  <p>We are an independent managed service provider. We are not a Microsoft Partner and are not affiliated with Microsoft. That keeps our advice neutral: we work for you, not for a licence quota.</p></div>
  <div class="panel"><h3>Who we work with</h3>{checks(['Professional services: legal, accounting, consulting','Healthcare clinics and practices','Non-profits and charities','Construction, logistics and field teams','Startups scaling past their first 10 hires'])}</div>
</div></section>
<section class="band alt"><div class="wrap">
  <div class="center"><span class="kicker">What we stand for</span><h2>Our values</h2></div>
  <div class="grid" style="margin-top:32px">{''.join(f'<div class="card"><span class="ico">{ic(i)}</span><h3>{t}</h3><p>{d}</p></div>' for i,t,d in VALUES)}</div>
</div></section>
<section class="band"><div class="wrap">
  <div class="section-head"><div><span class="kicker">The team</span><h2>People you will actually talk to</h2></div><p class="lead">Add your team here with a photo, role and a line about their M365 specialism.</p></div>
  <div class="grid">
    <div class="card"><span class="ico">{ic('users')}</span><h3>Founder name</h3><p>Founder and lead consultant. Microsoft 365, identity and security.</p></div>
    <div class="card"><span class="ico">{ic('headset')}</span><h3>Team member</h3><p>Service desk lead. Day-to-day support and onboarding.</p></div>
    <div class="card"><span class="ico">{ic('laptop')}</span><h3>Team member</h3><p>Endpoint engineer. Intune, Autopilot and device security.</p></div>
  </div>
  <p class="sample" style="margin-top:14px">Placeholder profiles: replace with your real team.</p>
</div></section>
{CTA}
'''
page('about.html', 'About | AIKorp', 'AIKorp is an independent MSP specialising in Microsoft 365 for growing businesses.', about)

# ================= CASES =================
CASES = [
 ('cloud','#0f6e70','Migration','Accounting firm, 25 users','Google Workspace to Microsoft 365',
  'Staff juggled Google Workspace for email and a local file server for client folders, with no MFA and no offsite backup.',
  'Phased migration of mail, calendars and files to Exchange Online and SharePoint over one weekend, with Intune enrolment and MFA for all users.',
  'One platform for mail, files and Teams, protected sign-ins and daily backup.'),
 ('shield','#a3401a','Security','Healthcare clinic, 40 users','Security hardening after a phishing scare',
  'A staff member entered their password on a fake sign-in page. Security settings were still at defaults.',
  'Conditional Access, Defender for Office 365 policies, phishing simulation training and Purview labels for patient documents.',
  'Risky sign-ins blocked automatically and a clear monthly security report for the practice manager.'),
 ('spark','#5b3aa8','Copilot','Consulting firm, 60 users','Preparing for Microsoft 365 Copilot',
  'Leadership wanted Copilot, but years of "anyone with the link" sharing meant sensitive files were widely exposed.',
  'Permissions and oversharing review, sensitivity labels, a 10-person pilot and prompt training workshops.',
  'Copilot rolled out with confidence that people only see what they are allowed to see.'),
]
cases = ''.join(f'''<article class="post case"><div class="thumb" style="background:linear-gradient(140deg,{c},#062428)">{ic(i)}</div><div class="body">
  <span class="pill">{tag}</span><span class="meta">{who}</span><h3>{t}</h3>
  <dl><dt>Challenge</dt><dd>{ch}</dd><dt>Approach</dt><dd>{ap}</dd><dt>What the client gets</dt><dd>{res}</dd></dl>
</div></article>''' for i,c,tag,who,t,ch,ap,res in CASES)
cases_pg = f'''
<section class="page-hero"><div class="wrap">
  <div class="crumbs"><a href="index.html">Home</a> / Case studies</div>
  <h1>How we help businesses like yours</h1>
  <p class="lead">Typical Microsoft 365 engagements, from first migration to Copilot rollout.</p>
</div></section>
<section style="padding:24px 0 72px"><div class="wrap">
  <p class="sample" style="margin-bottom:20px">Sample scenarios showing the kind of work we do. Replace them with your real customer stories, with permission, as you win them.</p>
  <div class="grid g3">{cases}</div>
</div></section>
{CTA}
'''
page('cases.html', 'Case studies | AIKorp', 'Example Microsoft 365 migration, security and Copilot engagements by AIKorp.', cases_pg)

# ================= BLOG =================
POSTS = [('shield','#a3401a','Security','The 10 Microsoft 365 security settings every small business should change today','MFA is only the start. Here are the defaults that leave most tenants exposed, and how to fix them.'),
 ('cloud','#0f6e70','Migration','Google Workspace to Microsoft 365: a step-by-step migration checklist','What to plan, what to test and how to avoid losing a single email on cut-over weekend.'),
 ('spark','#5b3aa8','Copilot','Is your data ready for Copilot? A 15-minute self-assessment','Oversharing is the biggest Copilot risk. Use these questions to find out where you stand.'),
 ('backup','#1f6fd1','Backup','Does Microsoft back up your Microsoft 365 data?','Retention is not backup. What is protected by default, what is not, and why it matters.'),
 ('laptop','#2b7a3d','Devices','Zero-touch laptops: how Autopilot and Intune speed up onboarding','Ship a sealed laptop to a new hire and have it ready in minutes, fully secured.'),
 ('chat','#5b5fc7','Teams','Teams sprawl: a simple governance plan for growing companies','Naming, ownership and lifecycle rules that keep Teams tidy without slowing people down.')]
posts = ''.join(f'''<article class="post"><div class="thumb" style="background:linear-gradient(140deg,{c},#062428)">{ic(i)}</div><div class="body">
  <span class="meta"><span class="pill">{tag}</span> &nbsp;Coming soon</span><h3>{t}</h3><p>{d}</p></div></article>''' for i,c,tag,t,d in POSTS)
blog = f'''
<section class="page-hero"><div class="wrap">
  <div class="crumbs"><a href="index.html">Home</a> / Blog</div>
  <h1>Microsoft 365 insights</h1>
  <p class="lead">Practical guides on security, migration, devices and AI for business owners and IT leads.</p>
</div></section>
<section style="padding:24px 0 72px"><div class="wrap"><div class="grid g3">{posts}</div></div></section>
<section class="band alt"><div class="wrap center"><h2>Get new guides in your inbox</h2><p class="lead">One useful Microsoft 365 tip a month. No spam.</p><a class="btn btn-primary" href="contact.html#newsletter">Subscribe</a></div></section>
'''
page('blog.html', 'Blog | AIKorp', 'Microsoft 365 security, migration, Intune and Copilot guides from AIKorp.', blog)

# ================= CONTACT =================
contact = f'''
<section class="page-hero"><div class="wrap">
  <div class="crumbs"><a href="index.html">Home</a> / Contact</div>
  <h1>Book a call with a Microsoft 365 expert</h1>
  <p class="lead">Tell us a little about your business. We will reply within one business day to set up a 30-minute discovery call or your free health check.</p>
</div></section>
<section style="padding:16px 0 80px"><div class="wrap contact-grid">
  <form class="card" id="contact-form" novalidate>
    <div class="fields">
      <div class="field"><label for="name">Full name *</label><input id="name" name="name" autocomplete="name" required><span class="err" id="err-name"></span></div>
      <div class="field"><label for="email">Work email *</label><input id="email" name="email" type="email" autocomplete="email" required><span class="err" id="err-email"></span></div>
      <div class="field"><label for="company">Company *</label><input id="company" name="company" autocomplete="organization" required><span class="err" id="err-company"></span></div>
      <div class="field"><label for="phone">Phone</label><input id="phone" name="phone" type="tel" autocomplete="tel"><span class="err"></span></div>
      <div class="field"><label for="users">Number of users</label><select id="users" name="users"><option>1 to 10</option><option selected>11 to 50</option><option>51 to 150</option><option>151 to 500</option><option>500+</option></select></div>
      <div class="field"><label for="topic">I am interested in</label><select id="topic" name="topic">
        <option value="assessment">Free Microsoft 365 health check</option><option value="plan-essentials">Essentials plan</option><option value="plan-business">Business plan</option><option value="plan-secure">Secure+ plan</option>
        <option value="migration">Migration project</option><option value="security">Security and compliance</option><option value="copilot">Copilot readiness</option><option value="newsletter">Newsletter</option><option value="other">Something else</option></select></div>
      <div class="field full"><label for="message">How can we help? *</label><textarea id="message" name="message" required placeholder="Current setup, pain points, timelines..."></textarea><span class="err" id="err-message"></span></div>
      <div class="field full"><label class="chk"><input type="checkbox" id="consent" name="consent" required> I agree to AIKorp contacting me about my enquiry. *</label><span class="err" id="err-consent"></span></div>
    </div>
    <button class="btn btn-primary" type="submit" style="margin-top:18px">Send request</button>
    <p class="form-msg" id="form-msg" role="status" aria-live="polite"></p>
  </form>
  <aside class="info">
    <div class="card"><span class="ico">{ic('mail')}</span><div><strong>Email</strong><br><a href="mailto:{EMAIL}">{EMAIL}</a></div></div>
    <div class="card"><span class="ico">{ic('phone')}</span><div><strong>Phone</strong><br><a href="tel:{TEL}">{PHONE}</a></div></div>
    <div class="card"><span class="ico">{ic('wa')}</span><div><strong>WhatsApp</strong><br><a href="{WA}">Chat on WhatsApp</a><br><span class="note">{PHONE}</span></div></div>
    <div class="card"><span class="ico">{ic('clock')}</span><div><strong>Office hours</strong><br>{HOURS}<br><span class="note">24/7 critical support on Business and Secure+</span></div></div>
    <div class="card"><span class="ico">{ic('pin')}</span><div><strong>Location</strong><br>{CITY}<br><span class="note">Remote support everywhere</span></div></div>
    <div class="card" style="display:block"><h3 style="font-size:17px">What happens next</h3>{checks(['We reply within one business day','30-minute discovery call','Free health check report','A clear proposal, no pressure'])}</div>
  </aside>
</div></section>
'''
page('contact.html', 'Contact | AIKorp', 'Book a call or a free Microsoft 365 health check with AIKorp.', contact)
print('built', sorted(os.listdir(OUT)))

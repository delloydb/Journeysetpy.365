// Basic interactive bits: nav toggle, smooth scroll, contact form stub, reveal on scroll
document.addEventListener('DOMContentLoaded', ()=> {
  // sticky nav active link switching on scroll
  const links = Array.from(document.querySelectorAll('.nav-link'));
  const sections = links.map(l => document.querySelector(l.getAttribute('href')));
  const headerOffset = 80;

  function onScroll(){
    const y = window.scrollY;
    sections.forEach((sec, i) => {
      if(!sec) return;
      const top = sec.offsetTop - headerOffset;
      const bottom = top + sec.offsetHeight;
      if (y >= top && y < bottom) {
        links.forEach(ln => ln.classList.remove('active'));
        links[i].classList.add('active');
      }
    });
  }
  window.addEventListener('scroll', onScroll, {passive:true});
  onScroll();

  // smooth scroll for internal links
  document.querySelectorAll('a[href^="#"]').forEach(a => {
    a.addEventListener('click', (e) => {
      const target = document.querySelector(a.getAttribute('href'));
      if(target){
        e.preventDefault();
        target.scrollIntoView({behavior:'smooth', block:'start'});
        // close mobile nav if open
        if(document.getElementById('nav').classList.contains('open')){
          document.getElementById('nav').classList.remove('open');
        }
      }
    });
  });

  // mobile nav toggle
  const navToggle = document.getElementById('navToggle');
  navToggle?.addEventListener('click', () => {
    document.getElementById('nav').classList.toggle('open');
  });

  // reveal on scroll (very small)
  const revealElements = document.querySelectorAll('.section, .project-card, .skill-card');
  const obs = new IntersectionObserver((entries)=>{
    entries.forEach(e=>{
      if(e.isIntersecting) e.target.classList.add('reveal');
    });
  }, {threshold: 0.12});
  revealElements.forEach(el => obs.observe(el));

  // contact form (stub)
  const form = document.getElementById('contactForm');
  form?.addEventListener('submit', (e) => {
    e.preventDefault();
    const data = new FormData(form);
    const payload = Object.fromEntries(data.entries());
    // For now: show a friendly confirmation and clear
    alert('Message sent — thank you, Sheriff will respond soon.');
    form.reset();
    console.log('Contact payload:', payload);
  });

  // footer year
  const yearEl = document.getElementById('year');
  if(yearEl) yearEl.textContent = new Date().getFullYear();
});

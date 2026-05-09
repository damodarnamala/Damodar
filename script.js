/* ============================================
   DAMODAR NAMALA — Portfolio Interactions
   ============================================ */

document.addEventListener('DOMContentLoaded', () => {
    initNavigation();
    initScrollAnimations();
    initNavScrollEffect();
    initSmoothScroll();
    initCounterAnimations();
    initThemeToggle();
    initColorToggle();
});

/* --- Navigation Toggle (Mobile) --- */
function initNavigation() {
    const toggle = document.getElementById('navToggle');
    const menu = document.getElementById('navMenu');
    
    if (!toggle || !menu) return;
    
    toggle.addEventListener('click', () => {
        toggle.classList.toggle('active');
        menu.classList.toggle('active');
    });

    // Close menu on link click
    menu.querySelectorAll('.nav-link').forEach(link => {
        link.addEventListener('click', () => {
            toggle.classList.remove('active');
            menu.classList.remove('active');
        });
    });

    // Close menu on outside click
    document.addEventListener('click', (e) => {
        if (!toggle.contains(e.target) && !menu.contains(e.target)) {
            toggle.classList.remove('active');
            menu.classList.remove('active');
        }
    });
}

/* --- Navigation Scroll Effect --- */
function initNavScrollEffect() {
    const nav = document.getElementById('nav');
    if (!nav) return;
    
    let lastScroll = 0;
    
    window.addEventListener('scroll', () => {
        const currentScroll = window.pageYOffset;
        
        if (currentScroll > 50) {
            nav.classList.add('scrolled');
        } else {
            nav.classList.remove('scrolled');
        }
        
        lastScroll = currentScroll;
    }, { passive: true });
}

/* --- Scroll Animations (Intersection Observer) --- */
function initScrollAnimations() {
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                
                // Stagger children if container
                const children = entry.target.querySelectorAll('.stagger-child');
                children.forEach((child, index) => {
                    setTimeout(() => {
                        child.classList.add('visible');
                    }, index * 100);
                });
            }
        });
    }, observerOptions);

    // Add fade-in class to animatable elements
    const animatableSelectors = [
        '.section-header',
        '.expertise-card',
        '.timeline-item',
        '.project-card',
        '.skill-category',
        '.metric-card',
        '.credential-card',
        '.contact-card',
        '.about-content',
        '.about-card',
        '.clients-section'
    ];

    animatableSelectors.forEach(selector => {
        document.querySelectorAll(selector).forEach(el => {
            el.classList.add('fade-in');
            observer.observe(el);
        });
    });
}

/* --- Smooth Scrolling --- */
function initSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                const offset = 80;
                const targetPosition = target.getBoundingClientRect().top + window.pageYOffset - offset;
                
                window.scrollTo({
                    top: targetPosition,
                    behavior: 'smooth'
                });
            }
        });
    });
}

/* --- Counter Animations --- */
function initCounterAnimations() {
    const counters = document.querySelectorAll('.stat-number');
    
    const counterObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting && !entry.target.dataset.animated) {
                entry.target.dataset.animated = 'true';
                animateCounter(entry.target);
            }
        });
    }, { threshold: 0.5 });

    counters.forEach(counter => counterObserver.observe(counter));
}

function animateCounter(element) {
    const text = element.textContent;
    const number = parseFloat(text);
    
    if (isNaN(number)) return;
    
    const duration = 1500;
    const startTime = performance.now();
    const suffix = text.replace(/[\d.]/g, '');
    const isDecimal = text.includes('.');
    const decimalPlaces = isDecimal ? (text.split('.')[1] || '').replace(/[^\d]/g, '').length : 0;

    function update(currentTime) {
        const elapsed = currentTime - startTime;
        const progress = Math.min(elapsed / duration, 1);
        
        // Ease out cubic
        const eased = 1 - Math.pow(1 - progress, 3);
        const current = number * eased;
        
        if (isDecimal) {
            element.textContent = current.toFixed(decimalPlaces) + suffix;
        } else {
            element.textContent = Math.floor(current) + suffix;
        }
        
        if (progress < 1) {
            requestAnimationFrame(update);
        } else {
            element.textContent = text;
        }
    }
    
    requestAnimationFrame(update);
}

/* --- Active Navigation Link Highlighting --- */
window.addEventListener('scroll', () => {
    const sections = document.querySelectorAll('.section, .hero');
    const navLinks = document.querySelectorAll('.nav-link:not(.nav-link--cta)');
    
    let current = '';
    
    sections.forEach(section => {
        const sectionTop = section.offsetTop - 100;
        if (window.pageYOffset >= sectionTop) {
            current = section.getAttribute('id');
        }
    });
    
    navLinks.forEach(link => {
        link.classList.remove('active');
        if (link.getAttribute('href') === `#${current}`) {
            link.classList.add('active');
        }
    });
}, { passive: true });

/* --- Theme Toggle --- */
function initThemeToggle() {
    const toggle = document.getElementById('themeToggle');
    if (!toggle) return;

    const saved = localStorage.getItem('theme');
    if (saved) {
        document.documentElement.setAttribute('data-theme', saved);
    }

    toggle.addEventListener('click', () => {
        const current = document.documentElement.getAttribute('data-theme');
        const next = current === 'light' ? 'dark' : 'light';
        document.documentElement.setAttribute('data-theme', next);
        localStorage.setItem('theme', next);
    });
}

/* --- Color Scheme Toggle --- */
function initColorToggle() {
    const toggle = document.getElementById('colorToggle');
    if (!toggle) return;

    const colors = ['default', 'emerald', 'amber', 'rose', 'cyan', 'highcontrast'];
    const saved = localStorage.getItem('colorScheme');
    if (saved && saved !== 'default') {
        document.documentElement.setAttribute('data-color', saved);
    }

    toggle.addEventListener('click', () => {
        const current = document.documentElement.getAttribute('data-color') || 'default';
        const currentIndex = colors.indexOf(current);
        const nextIndex = (currentIndex + 1) % colors.length;
        const next = colors[nextIndex];

        if (next === 'default') {
            document.documentElement.removeAttribute('data-color');
        } else {
            document.documentElement.setAttribute('data-color', next);
        }
        localStorage.setItem('colorScheme', next);
    });
}

    // Animate sections on scroll
    const sections = document.querySelectorAll("section");

    const options = {
        root: null,
        threshold: 0.1,
    };
    
    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add("visible");
                observer.unobserve(entry.target);
            }
        });
    }, options);
    
    sections.forEach(section => {
        section.classList.add("invisible");
        observer.observe(section);
    });
    
    // CSS class for visible sections
    document.querySelectorAll("section").forEach((section) => {
        section.classList.add("invisible");
    });
    
    const style = document.createElement('style');
    style.innerHTML = `
    .invisible {
        opacity: 0;
        transform: translateY(20px);
        transition: opacity 0.5s, transform 0.5s;
    }
    
    .visible {
        opacity: 1;
        transform: translateY(0);
    }
    `;
    document.head.appendChild(style);
    
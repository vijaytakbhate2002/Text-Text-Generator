// Toggle sidebar menu for mobile view
function toggleMenu() {
    document.getElementById("navbarLinks").classList.toggle("active");
}

// Change navbar background on scroll
window.addEventListener('scroll', function () {
    const navbar = document.getElementById("navbar");
    if (window.scrollY > 50) {
        navbar.classList.add('scrolled');
    } else {
        navbar.classList.remove('scrolled');
    }
});

// Add animation delay for each link in the sidebar
document.querySelectorAll('.navbar-links li').forEach((link, index) => {
    link.style.animationDelay = `${index * 0.1}s`;
});

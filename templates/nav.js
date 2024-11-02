// Toggle mobile menu
function toggleMenu() {
    const navbarLinks = document.getElementById('navbarLinks');
    navbarLinks.classList.toggle('active');
}

// Navbar scroll effect
window.onscroll = function() {
    const navbar = document.getElementById('navbar');
    if (window.scrollY > 50) {
        navbar.classList.add('scrolled');
    } else {
        navbar.classList.remove('scrolled');
    }
};

let currentIndex = 0;

function nextSlide() {
    const carousel = document.querySelector('.carousel');
    const items = document.querySelectorAll('.carousel-item');
    currentIndex = (currentIndex + 1) % items.length;
    carousel.style.transform = `translateX(-${currentIndex * 100}%)`;
}

function prevSlide() {
    const carousel = document.querySelector('.carousel');
    const items = document.querySelectorAll('.carousel-item');
    currentIndex = (currentIndex - 1 + items.length) % items.length;
    carousel.style.transform = `translateX(-${currentIndex * 100}%)`;
}

// Filtering Portfolio
function filterPortfolio(category) {
    const items = document.querySelectorAll('.portfolio-item');
    items.forEach(item => {
        if (category === 'all' || item.classList.contains(category)) {
            item.style.display = 'block';
        } else {
            item.style.display = 'none';
        }
    });
}

// Show the scroll-up button when the user scrolls down
window.onscroll = function() {
    const scrollUpButton = document.getElementById("scroll-up-btn");

    if (document.body.scrollTop > 200 || document.documentElement.scrollTop > 200) {
        scrollUpButton.style.display = "block";
    } else {
        scrollUpButton.style.display = "none";
    }
};

// Scroll to the top when the user clicks the button
document.getElementById("scroll-up-btn").onclick = function() {
    window.scrollTo({ top: 0, behavior: 'smooth' });
};


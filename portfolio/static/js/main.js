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

// JavaScript for Scroll-Up Button
document.addEventListener("DOMContentLoaded", function () {
    const scrollUpBtn = document.getElementById("scroll-up-btn");

    // Show/hide the button when scrolling
    window.addEventListener("scroll", function () {
        if (window.scrollY > 200) { // Show the button after scrolling down 200px
            scrollUpBtn.classList.add("show");
            scrollUpBtn.classList.remove("hide");
        } else {
            scrollUpBtn.classList.add("hide");
            scrollUpBtn.classList.remove("show");
        }
    });

    // Scroll to the top when the button is clicked
    scrollUpBtn.addEventListener("click", function () {
        window.scrollTo({
            top: 0,
            behavior: "smooth" // Smooth scrolling effect
        });
    });
});


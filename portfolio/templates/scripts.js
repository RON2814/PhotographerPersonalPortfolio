document.addEventListener('DOMContentLoaded', () => {
    let currentIndex = 0;

    function updateCarousel(index) {
        const carousel = document.querySelector('.carousel');
        const items = document.querySelectorAll('.carousel-item');

        if (carousel && items.length > 0) {
            currentIndex = (index + items.length) % items.length; // Ensure index wraps around
            carousel.style.transform = `translateX(-${currentIndex * 100}%)`;
        }
    }

    function nextSlide() {
        updateCarousel(currentIndex + 1);
    }

    function prevSlide() {
        updateCarousel(currentIndex - 1);
    }

    function filterPortfolio(category) {
        const items = document.querySelectorAll('.portfolio-item');

        if (items) {
            items.forEach(item => {
                if (category === 'all' || item.classList.contains(category)) {
                    item.style.display = 'block';
                } else {
                    item.style.display = 'none';
                }
            });
        }
    }

    // Attach event listeners for carousel buttons
    const nextButton = document.querySelector('.carousel-button:nth-of-type(2)');
    const prevButton = document.querySelector('.carousel-button:nth-of-type(1)');

    if (nextButton) nextButton.addEventListener('click', nextSlide);
    if (prevButton) prevButton.addEventListener('click', prevSlide);

    // Attach filter buttons to the portfolio filter function
    const filterButtons = document.querySelectorAll('.portfolio-nav button');

    if (filterButtons) {
        filterButtons.forEach(button => {
            button.addEventListener('click', () => {
                const category = button.textContent.toLowerCase();
                filterPortfolio(category);
            });
        });
    }
});

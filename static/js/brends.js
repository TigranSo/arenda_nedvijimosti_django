const container = document.querySelector('.partner-container');
const items = document.querySelectorAll('.partner-item');
const leftButton = document.getElementById('scroll-left');
const rightButton = document.getElementById('scroll-right');
let scrollPosition = 0;

leftButton.addEventListener('click', () => {
    scrollPosition = Math.max(scrollPosition - container.clientWidth, 0);
    container.scrollTo({
        left: scrollPosition,
        behavior: 'smooth',
    });
});

rightButton.addEventListener('click', () => {
    scrollPosition = Math.min(
        scrollPosition + container.clientWidth,
        container.scrollWidth - container.clientWidth
    );
    container.scrollTo({
        left: scrollPosition,
        behavior: 'smooth',
    });
});

// Toggle menu for navbar
const menu = document.querySelector('.menu');
const menuItems = document.querySelectorAll('.menu-items');
const menuBtn = document.querySelector('.menu-btn');
const closeIcon = document.querySelector('#closeMenu');
const openIcon = document.querySelector('#openMenu');

function toggleMenu() {
	if (menu.classList.contains('showMenu')) {
		menu.classList.remove('showMenu');
		closeIcon.style.display = 'none';
		openIcon.style.display = 'block';
	} else {
		menu.classList.add('showMenu');
		closeIcon.style.display = 'block';
		openIcon.style.display = 'none';
	}
}

menuBtn.addEventListener('click', toggleMenu);

menuItems.forEach(menuItem => {
	menuItem.addEventListener('click', toggleMenu);
});


// Rotating text animation
document.addEventListener('DOMContentLoaded', function() {
    const texts = document.querySelectorAll('.text');
    let currentIdx = 0;

    function animateText() {
        texts.forEach((text, idx) => {
            if (idx === currentIdx) {
                text.classList.add('active');
            } else {
                text.classList.remove('active');
            }
        });
        currentIdx = (currentIdx + 1) % texts.length;
    }

    setInterval(animateText, 2000); // Adjust the animation / rotation speed (in milliseconds)
});










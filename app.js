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

// Display random quotes by author using fetch
// Load the JSON file with quotes
// Load the JSON file with quotes
fetch('exports/quotes.json')
    .then(response => {
        if (!response.ok) {
            console.error('Network response was not ok');
            return;
        }
        return response.json();
    })
    .then(data => {
        console.log(data); // Logging the retrieved JSON data for debugging

        // Store quotes data
        const quoteData = data;

        // Function to generate random quote
        function generateQuote() {
            // Select a random quote and author
            const randomIndex = Math.floor(Math.random() * data.length);
            const randomQuote = quoteData[randomIndex];

            // Display the quote and author
            const quoteElem = document.querySelector('#message');
            const authorElem = document.querySelector('#author');

            quoteElem.textContent = `"${randomQuote.quotes}"`;
            authorElem.textContent = '- ' + randomQuote.author;
        }

        // Call the function initially to display a random quote
        generateQuote();

        // Set interval to generate new quote every 6 seconds
        setInterval(generateQuote, 4000);
    })
    .catch(error => console.error('Error fetching quotes:', error));

// Rotating text animation
document.addEventListener('DOMContentLoaded', function () {
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










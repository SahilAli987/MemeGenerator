// Background animation configuration
const emojis = ['😂', '🤣', '😎', '🔥', '💯', '🎉', '✨', '🌟', '🚀', '💪'];
const memeText = ['LOL', 'ROFL', 'OMG', 'YEET', 'BRUH', 'NICE', 'EPIC'];
const colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEEAD', '#D4A5A5', '#9B59B6'];

function createBackgroundElements() {
    const container = document.getElementById('background-container');
    if (!container) return;
    
    // Create falling emojis
    for (let i = 0; i < 15; i++) {
        const element = document.createElement('div');
        element.className = 'falling-element';
        element.textContent = emojis[Math.floor(Math.random() * emojis.length)];
        element.style.left = `${Math.random() * 100}vw`;
        element.style.fontSize = `${Math.random() * 20 + 20}px`;
        element.style.animationDuration = `${Math.random() * 10 + 5}s`;
        container.appendChild(element);
    }

    // Create floating meme text
    for (let i = 0; i < 8; i++) {
        const element = document.createElement('div');
        element.className = 'floating-element';
        element.textContent = memeText[Math.floor(Math.random() * memeText.length)];
        element.style.left = `${Math.random() * 100}vw`;
        element.style.top = `${Math.random() * 100}vh`;
        element.style.color = colors[Math.floor(Math.random() * colors.length)];
        element.style.fontSize = `${Math.random() * 15 + 15}px`;
        element.style.fontWeight = 'bold';
        element.style.animationDelay = `${Math.random() * 5}s`;
        container.appendChild(element);
    }
}

// Initialize background elements
document.addEventListener('DOMContentLoaded', () => {
    createBackgroundElements();
    
    // Periodically refresh background elements
    setInterval(() => {
        const container = document.getElementById('background-container');
        if (container) {
            container.innerHTML = '';
            createBackgroundElements();
        }
    }, 20000); // Refresh every 20 seconds
}); 
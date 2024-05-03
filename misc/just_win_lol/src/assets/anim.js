document.addEventListener('htmx:afterRequest', function(evt) {
    let handCards = document.querySelectorAll(".hand .card");
    let handCardAmount = document.querySelector(".hand-drawn-amount");
    handCardAmount.innerText = `${handCards.length}/${handCards.length}`;
    animCards(evt, handCards);
});

document.addEventListener('DOMContentLoaded', function(evt) {
    let jokerCards = document.querySelectorAll(".jokers .card");
    let jokerCardAmount = document.querySelector(".jokers-amount");
    jokerCardAmount.innerText = `${jokerCards.length}/5`;
    animCards(evt, jokerCards);
});

function animCards(evt, cards) {
    cards.forEach((card, idx) => {
        // subtle fan
        card.style.setProperty("--rotateZ", idx-((cards.length-1)/2) + "deg");

        card.addEventListener("mousemove", (event) => {
            const clampDeg = 15;
            var elemMidX = event.currentTarget.offsetWidth / 2;
            var elemMidY = event.currentTarget.offsetHeight / 2;
            var x = ((event.offsetX - elemMidX) / elemMidX) * clampDeg;
            var y = ((event.offsetY - elemMidY) / elemMidY) * -clampDeg;
    
            card.style.setProperty("--rotateX", y + "deg");
            card.style.setProperty("--rotateY", x + "deg");
            card.style.setProperty("--scale", "1.1");
        });
        card.addEventListener("mouseleave", (event) => {
            card.style.setProperty("--rotateX", "0deg");
            card.style.setProperty("--rotateY", "0deg");
            card.style.setProperty("--scale", "1");
        });
    });
}
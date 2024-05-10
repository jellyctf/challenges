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

function rotateCard(card, x, y) {
    card.style.setProperty("--rotateX", y + "deg");
    card.style.setProperty("--rotateY", x + "deg");
}

function ambientCardTilt(card) {
    var now = Date.now() / 1500;
    //var x = Math.cos(now) * 20;
    //var y = Math.sin(now) * 20;
    var ambient_tilt = 0.2;
    var idx = card.rand
    var tilt_angle = now*(1.56 + (idx/1.14212)%1) + idx/1.35122;
    var x = (0.5 + 0.5*ambient_tilt*Math.cos(tilt_angle) * 120);
    var y = (0.5 + 0.5*ambient_tilt*Math.sin(tilt_angle) * 120);
    rotateCard(card, x, y);
}

function animCards(evt, cards) {
    cards.forEach((card, idx) => {
        // subtle fan
        card.style.setProperty("--rotateZ", idx-((cards.length-1)/2) + "deg");
        card.intervalID = setInterval(function() {ambientCardTilt(card)}, 50);
        card.rand = Math.random() * 1000

        card.addEventListener("mousemove", (event) => {
            clearInterval(card.intervalID);
            const clampDeg = 15;
            var elemMidX = event.currentTarget.offsetWidth / 2;
            var elemMidY = event.currentTarget.offsetHeight / 2;
            var x = ((event.offsetX - elemMidX) / elemMidX) * clampDeg;
            var y = ((event.offsetY - elemMidY) / elemMidY) * -clampDeg;
            rotateCard(card, x, y);
            card.style.setProperty("--scale", "1.1");
        });
        card.addEventListener("mouseleave", (event) => {
            rotateCard(card, 0, 0);
            card.style.setProperty("--scale", "1");
            card.intervalID = setInterval(function() {ambientCardTilt(card)}, 50);
        });
    });
}
document.addEventListener('htmx:afterRequest', function(evt) {
    let cards = document.querySelectorAll(".card");
    cards.forEach((card, idx) => {
        card.style.setProperty("--rotateZ", (idx-cards.length/2) + "deg")
        card.addEventListener("mousemove", (event) => {
            const clampDeg = 15;
            var elemMidX = event.currentTarget.offsetWidth / 2;
            var elemMidY = event.currentTarget.offsetHeight / 2;
            var x = ((event.offsetX - elemMidX) / elemMidX) * clampDeg;
            var y = -1 * (((event.offsetY - elemMidY) / elemMidY) * clampDeg);
    
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
});
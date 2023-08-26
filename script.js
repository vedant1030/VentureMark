document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector(".trademark-form");
    const resultMessage = document.querySelector(".result-message");
    const availableSpan = document.querySelector(".available");

    form.addEventListener("submit", function (event) {
        event.preventDefault();

        // Simulate availability check (you can replace this with your actual logic)
        const isAvailable = Math.random() < 0.5;

        if (isAvailable) {
            availableSpan.textContent = "available";
            resultMessage.style.color = "#27ae60";
        } else {
            availableSpan.textContent = "not available";
            resultMessage.style.color = "#e74c3c";
        }
    });
});

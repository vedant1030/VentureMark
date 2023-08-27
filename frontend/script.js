document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector(".trademark-form");
    const resultMessage = document.querySelector(".result-message");
    const availableSpan = document.querySelector(".available");

    form.addEventListener("submit", async function (event) {
        event.preventDefault();

        const trademarkInput = form.querySelector("input[name='trademark']").value;

        // Make an API request to your Flask backend
        try {
            const response = await fetch("/check-trademark", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({ trademark: trademarkInput }),
            });

            if (!response.ok) {
                throw new Error("Failed to fetch data");
            }

            const data = await response.json();

            if (data.available) {
                availableSpan.textContent = "available";
                resultMessage.style.color = "#27ae60";
            } else {
                availableSpan.textContent = "not available";
                resultMessage.style.color = "#e74c3c";
            }

            // Show the result message
            resultMessage.style.display = "block";
        } catch (error) {
            console.error(error);
            // Handle the error, e.g., display an error message to the user
        }
    });
});
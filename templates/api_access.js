document.addEventListener("DOMContentLoaded", () => {
    const form = document.querySelector("form");
    const modelNameInput = document.getElementById("model_name");
    const apiKeyInput = document.getElementById("api_key");
    const errorMessage = document.createElement("div");

    errorMessage.classList.add("error-message");
    form.appendChild(errorMessage);

    form.addEventListener("submit", (e) => {
        errorMessage.style.display = "none";

        if (!modelNameInput.value.trim() || !apiKeyInput.value.trim()) {
            e.preventDefault();
            errorMessage.textContent = "Please fill in all required fields.";
            errorMessage.style.display = "block";
        }
    });

    [modelNameInput, apiKeyInput].forEach(input => {
        input.addEventListener("focus", () => {
            input.style.boxShadow = "0 0 8px rgba(255, 218, 121, 0.5)";
        });
        input.addEventListener("blur", () => {
            input.style.boxShadow = "none";
        });
    });
});

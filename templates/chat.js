// Function to send a message and animate
function sendMessage(userInput) {
    const chatBox = document.querySelector('.chat-box');
    
    // Create user message element
    const userMessage = document.createElement('div');
    userMessage.classList.add('message', 'user-message');
    userMessage.textContent = userInput;
    
    // Append user message to chat box
    chatBox.appendChild(userMessage);
    
    // Simulate bot response
    setTimeout(() => {
        const botMessage = document.createElement('div');
        botMessage.classList.add('message', 'bot-message');
        botMessage.textContent = "Bot: " + simulateBotResponse(userInput); // You can replace this with actual response
        chatBox.appendChild(botMessage);
        chatBox.scrollTop = chatBox.scrollHeight; // Scroll to the bottom
    }, 1000); // Simulated delay for bot response
}

// Simulated bot response function
function simulateBotResponse(input) {
    return "This is a simulated response to: " + input;
}

// Modify form submission to include the sendMessage function
document.querySelector('.input-container form').addEventListener('submit', function(e) {
    e.preventDefault(); // Prevent form from submitting normally
    const userInput = this.user_input.value;
    sendMessage(userInput); // Call sendMessage function
    this.reset(); // Clear the input
});


// Animation effect on button click
document.addEventListener("DOMContentLoaded", function() {
    const sendButton = document.querySelector(".input-container button");
    const inputField = document.querySelector(".input-container input[type='text']");

    sendButton.addEventListener("click", function(event) {
        if (inputField.value.trim() === "") {
            event.preventDefault(); // Prevent submission if input is empty
            inputField.focus();
            inputField.style.borderColor = "red"; // Highlight border if empty
            setTimeout(() => {
                inputField.style.borderColor = "#4a90e2";
            }, 500);
        }
    });
});

function selectAction(action) {
    document.getElementById('selectedAction').value = action; // Set the hidden input value
    return true; // Allow the form to be submitted
}


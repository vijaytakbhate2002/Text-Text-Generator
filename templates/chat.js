// function selectAction(action) {
//     document.getElementById("selectedAction").value = action;
//     document.getElementById("actionForm").submit();
//     return false;
// }

// function sendMessage(userInput) {
//     const chatBox = document.querySelector('.chat-box');
    
//     const userMessage = document.createElement('div');
//     userMessage.classList.add('message', 'user-message');
//     userMessage.textContent = userInput;
    
//     chatBox.appendChild(userMessage);
    
//     setTimeout(() => {
//         const botMessage = document.createElement('div');
//         botMessage.classList.add('message', 'bot-message');
//         botMessage.textContent = "Bot: " + simulateBotResponse(userInput); 
//         chatBox.scrollTop = chatBox.scrollHeight; 
//     }, 1000); 
// }

// function simulateBotResponse(input) {
//     return "This is a simulated response to: " + input;
// }

// // Modify form submission to include the sendMessage function
// document.querySelector('.input-container form').addEventListener('submit', function(e) {
//     e.preventDefault(); // Prevent form from submitting normally
//     const userInput = this.user_input.value;
//     sendMessage(userInput); // Call sendMessage function
//     // this.reset(); // Clear the input
// });

// document.addEventListener("DOMContentLoaded", () => {
//     const actionForm = document.getElementById("actionForm");
//     const selectedAction = document.getElementById("selectedAction");

//     // Add event listeners for each button
//     document.getElementById("paraphraserButton").addEventListener("click", (event) => handleAction(event, "Paraphraser"));
//     document.getElementById("grammarCheckerButton").addEventListener("click", (event) => handleAction(event, "Grammar Checker"));
//     document.getElementById("aiDetectorButton").addEventListener("click", (event) => handleAction(event, "AI Detector"));
//     document.getElementById("plagiarismCheckerButton").addEventListener("click", (event) => handleAction(event, "Plagiarism Checker"));
//     document.getElementById("summarizerButton").addEventListener("click", (event) => handleAction(event, "Summarizer"));
//     document.getElementById("shortAnswerButton").addEventListener("click", (event) => handleAction(event, "Short Answer"));
//     document.getElementById("clearButton").addEventListener("click", (event) => handleAction(event, "Just Chat"));

//     function handleAction(event, action) {
//         // Prevent the default form submission
//         event.preventDefault();

//         // Set the selected action
//         selectedAction.value = action;

//         // Submit the form
//         actionForm.submit();
//     }
// });


function sendMessage(userInput) {
    const chatBox = document.querySelector('.chat-box');
    
    const userMessage = document.createElement('div');
    userMessage.classList.add('message', 'user-message');
    userMessage.textContent = userInput;
    chatBox.appendChild(userMessage);

    setTimeout(() => {
        const botMessage = document.createElement('div');
        botMessage.classList.add('message', 'bot-message');
        botMessage.textContent = "Bot: " + simulateBotResponse(userInput);
        chatBox.appendChild(botMessage);
        chatBox.scrollTop = chatBox.scrollHeight;
    }, 1000);
}

function simulateBotResponse(input) {
    return "This is a simulated response to: " + input;
}

document.querySelector('.input-container form').addEventListener('submit', function(e) {
    e.preventDefault();
    const userInput = this.user_input.value;
    sendMessage(userInput);
    this.reset(); // Clear the input field after sending the message
});

document.addEventListener("DOMContentLoaded", () => {
    const actionForm = document.getElementById("actionForm");
    const selectedAction = document.getElementById("selectedAction");

    const handleAction = (event, action) => {
        event.preventDefault();
        selectedAction.value = action;
        actionForm.submit();
    };

    document.getElementById("paraphraserButton").addEventListener("click", (event) => handleAction(event, "Paraphraser"));
    document.getElementById("grammarCheckerButton").addEventListener("click", (event) => handleAction(event, "Grammar Checker"));
    document.getElementById("aiDetectorButton").addEventListener("click", (event) => handleAction(event, "AI Detector"));
    document.getElementById("plagiarismCheckerButton").addEventListener("click", (event) => handleAction(event, "Plagiarism Checker"));
    document.getElementById("summarizerButton").addEventListener("click", (event) => handleAction(event, "Summarizer"));
    document.getElementById("shortAnswerButton").addEventListener("click", (event) => handleAction(event, "Short Answer"));
    document.getElementById("clearButton").addEventListener("click", (event) => handleAction(event, "Just Chat"));
});
function handleAction(event, action) {
    event.preventDefault();
    document.getElementById("selectedAction").value = action;
    document.getElementById("actionForm").submit();
}

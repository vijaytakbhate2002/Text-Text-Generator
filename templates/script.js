function selectAction(action, button) {
    // Set the hidden input field with the selected action
    const selectedActionInput = document.getElementById("selectedAction");
    selectedActionInput.value = action;

    // Remove active class from all buttons
    const buttons = document.querySelectorAll(".sidebar button");
    buttons.forEach(btn => {
        btn.classList.remove("active");
    });

    // Add active class to the clicked button
    button.classList.add("active");

    // Submit the form if desired
    document.getElementById("actionForm").submit();
}

function clearSelection() {
    // Clear the selected action
    document.getElementById("selectedAction").value = "";

    // Optionally remove active class from all buttons
    const buttons = document.querySelectorAll(".sidebar button");
    buttons.forEach(btn => {
        btn.classList.remove("active");
    });
}


async function analyzeAnxiety() {

    const text = document.getElementById("text_response").value;

    if (!text) {
        alert("Please enter how you feel about your exams.");
        return;
    }

    try {

        const response = await fetch("/predict", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                text: text
            })
        });

        const data = await response.json();

        const resultCard = document.getElementById("resultCard");
        const badge = document.getElementById("resultBadge");

        resultCard.classList.remove("hidden");

        badge.innerText = "Anxiety Level: " + data.anxiety_level;

    }

    catch (error) {

        console.error(error);
        alert("Server error. Make sure Flask server is running.");

    }
}
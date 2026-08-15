function runEmotionDetector() {
    const textToAnalyze = document.getElementById("textToAnalyze").value;
    const responseArea = document.getElementById("system_response");

    responseArea.textContent = "Analyzing text...";
    fetch(`/emotionDetector?textToAnalyze=${encodeURIComponent(textToAnalyze)}`)
        .then((response) => response.text())
        .then((message) => {
            responseArea.textContent = message;
        })
        .catch(() => {
            responseArea.textContent = "Unable to contact the application. Please try again.";
        });
}

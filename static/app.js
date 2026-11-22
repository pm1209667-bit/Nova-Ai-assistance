console.log("NOVA AI Assistant Started!");

function speak(message) {
    let speech = new SpeechSynthesisUtterance(message);
    speech.lang = "en-US";
    window.speechSynthesis.speak(speech);
}

function startAssistant() {
    speak("Hello! I am Nova, your personal AI assistant.");
}

startAssistant();

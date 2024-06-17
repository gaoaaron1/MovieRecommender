import { ref } from 'vue';

const transcript = ref('');
const isRecording = ref(false);
let triggerRecommendation; // Define a placeholder for the function

const Recognition = window.SpeechRecognition || window.webkitSpeechRecognition;
const sr = new Recognition();

sr.continuous = true;
sr.interimResults = true;

sr.onstart = () => {
    console.log('SR Started');
    isRecording.value = true;
};

sr.onend = () => {
    console.log('SR Stopped');
    isRecording.value = false;
};

sr.onresult = (evt) => {
    for (let i = 0; i < evt.results.length; i++) {
        const result = evt.results[i];

        if (result.isFinal) {
            CheckForCommand(result);
        }
    }

    const t = Array.from(evt.results)
        .map(result => result[0])
        .map(result => result.transcript)
        .join('')
        .toLowerCase(); // Convert to lowercase

    transcript.value = t;
};

const CheckForCommand = (result) => {
    const t = result[0].transcript.toLowerCase();
    console.log(t);

    // Check for specific voice commands
    if (t.includes('stop recording')) {
        sr.stop();

    } else if (t.includes('what is the time') || t.includes('what\'s the time')) {
        sr.stop();
        alert(new Date().toLocaleTimeString());
        setTimeout(() => sr.start(), 100);
    
    } else if (t.includes('recommend me')) {
        sr.stop();
        const movieTitle = extractMovieTitle(t);
        if (movieTitle) {
            console.log('Recommend movie:', movieTitle);
            triggerRecommendation(movieTitle); // Call the function passed from App.vue
        } else {
            console.log('No movie title found in command.');
        }
    }
};

// Function to extract movie title from voice command
function extractMovieTitle(command) {
    const keywords = ['recommend me', 'recommend', 'movie'];
    for (const keyword of keywords) {
        if (command.includes(keyword)) {
            const startIndex = command.indexOf(keyword) + keyword.length;
            return command.substring(startIndex).trim();
        }
    }
    return '';
}

const ToggleMic = () => {
    if (isRecording.value) {
        sr.stop();
    } else {
        sr.start();
    }
};

export {
    transcript,
    isRecording,
    ToggleMic,
    setRecommendationTrigger // Export the function to set the recommendation trigger
};

function setRecommendationTrigger(func) {
    triggerRecommendation = func;
}

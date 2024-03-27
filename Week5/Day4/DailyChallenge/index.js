// In todays exercise we will be creating a Mad Libs game.
// If you’ve never played this game, a mad lib is a game where you fill in a bunch of blank inputs with different word types (ie : noun, adjective, verb),
// and then a story is generated based on the words you chose, and sometimes the story is surprisingly funny.

// Follow these steps :

// Get the value of each of the inputs in the HTML file when the form is submitted. Remember the event.preventDefault()
// Make sure the values are not empty
// Write a story that uses each of the values.
// Make sure you check the console for errors when playing the game.
// Bonus: Add a “shuffle” button to the HTML file, when clicked the button should change the story currently displayed (but keep the values entered by the user).
// The user could click the button at least three times and get a new story. Display the stories randomly.



// Function to get random story
function getRandomStory() {
    const stories = [
        'Once upon a time, there was a {{noun}} who lived in a {{adjective}} house. One day, {{person}} decided to {{verb}} to the {{place}}.',
        '{{person}} found a {{noun}} in the {{place}} and felt {{adjective}}. Then {{person}} {{verb}} happily ever after.'
    ];
    return stories[Math.floor(Math.random() * stories.length)];
}

// Function to replace placeholders in story with user inputs
function replacePlaceholders(story, inputs) {
    for (let key in inputs) {
        story = story.replace(new RegExp('{{' + key + '}}', 'g'), inputs[key]);
    }
    return story;
}

// Function to display the story
function displayStory() {
    const inputs = {
        noun: document.getElementById('noun').value.trim(),
        adjective: document.getElementById('adjective').value.trim(),
        person: document.getElementById('person').value.trim(),
        verb: document.getElementById('verb').value.trim(),
        place: document.getElementById('place').value.trim()
    };

    // Check if any input field is empty
    for (let key in inputs) {
        if (inputs[key] === '') {
            alert('Please fill in all the input fields.');
            return;
        }
    }

    const storyTemplate = getRandomStory();
    const story = replacePlaceholders(storyTemplate, inputs);

    document.getElementById('story').textContent = story;
}

// Event listener for form submission
document.getElementById('libform').addEventListener('submit', function (event) {
    event.preventDefault();
    displayStory();
});

// Event listener for shuffle button
document.getElementById('lib-button').addEventListener('click', function () {
    displayStory();
});
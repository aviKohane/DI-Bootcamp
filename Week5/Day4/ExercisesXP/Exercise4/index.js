// 🌟 Exercice 4 : Volume Of A Sphere
// Instructions
// Write a JavaScript program to calculate the volume of a sphere. 
// V = 4/3 π r³
// The formula for the volume of a sphere is V = 4/3 π r³, where V = volume and r = radius. The radius of a sphere is half its diameter.

function calculateVolume(radius) {
    return 4 / 3 * Math.PI * Math.pow(radius, 3);
}

// Event listener for form submission
document.getElementById('MyForm').addEventListener('submit', function (event) {
    // Prevent default form submission behavior
    event.preventDefault();
    // Get the radius input value
    const radius = parseFloat(document.getElementById('radius').value);

    // Check if the input is a valid number
    if (!isNaN(radius)) {
        // Calculate the volume of the sphere
        const volume = calculateVolume(radius);

        // Display the volume in the volume input field
        document.getElementById('volume').value = volume.toFixed(2);
    } else {
        // If the input is not a valid number, display an error message
        alert('Please enter a valid number for the radius.');
    }
});
// In this exercise we will be creating a webpage with a black background 
// as the universe and we will fill the universe with planets and their moons.
// We will provide the HTML page.
// You only have to work with a JS file.

// Create an array which value is the planets of the solar system.
// For each planet in the array, create a <div> using createElement. This div should have a class named "planet".
// Each planet should have a different background color. 
// (Hint: you could add a new class to each planet - each class containing a different background-color).
// Finally append each div to the <section> in the HTML (presented below).
// Bonus: Do the same process to create the moons.
// Be careful, each planet has a certain amount of moons. How should you display them?
// Should you still use an array for the planets ? Or an array of objects ?


// Array of planets with their respective moons
const planets = [
    { name: 'Venus', moons: 0 },
    { name: 'Earth', moons: 1 },
    { name: 'Mercury', moons: 0 },
    { name: 'Mars', moons: 2 },
    { name: 'Jupiter', moons: 10 },
    { name: 'Saturn', moons: 2 },
    { name: 'Uranus', moons: 7 },
    { name: 'Neptune', moons: 4 }
];

for (const planet of planets) {
    const planetDiv = document.createElement('div');
    // planetDiv.classList.add('planet');
    // planetDiv.classList.add(planet.name.toLowerCase())
    planetDiv.classList.add("planet", planet.name.toLowerCase())
    planetDiv.textContent = planet.name;
    // Create moons for the planet
    for (let i = 0; i < planet.moons; i++) {
        const moonDiv = document.createElement('div');
        moonDiv.classList.add('moon');
        // search on internet : js change element position
        moonDiv.style.left = i * 15 + "px";
        planetDiv.appendChild(moonDiv);
    }

    const section = document.querySelector('.listPlanets');
    section.appendChild(planetDiv)

}
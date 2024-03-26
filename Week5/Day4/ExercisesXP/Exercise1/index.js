// <!-- 🌟 Exercise 1 : Change The Article
// Instructions
// Copy the code below, into a structured HTML file:

// <article>
//     <h1> Some Facts </h1>
//     <h2> The Chocolate </h2>
//     <h3> History of the chocolate </h3>
//     <p> Chocolate is made from tropical Theobroma cacao tree seeds. 
//     Its earliest use dates back to the Olmec civilization in Mesoamerica.</p>
//     <p> After the European discovery of the Americas, chocolate became 
//     very popular in the wider world, and its demand exploded. </p>
//     <p> Chocolate has since become a popular food product that millions enjoy every day, 
//     thanks to its unique, rich, and sweet taste.</p> 
//     <p> But what effect does eating chocolate have on our health?</p> 
// </article>


// Using a DOM property, retrieve the h1 and console.log it.
let h1 = document.querySelector("h1");
console.log(h1);

// Using DOM methods, remove the last paragraph in the <article> tag.
document.querySelector("article").lastElementChild.remove();

// Add an event listener which will change the background color of the h2 to red, when it’s clicked on.
let h2 = document.querySelector("h2");
h2.addEventListener("click", handleBackgroundColor);
function handleBackgroundColor() {
    h2.style.backgroundColor = "red";
}

// Add an event listener which will hide the h3 when it’s clicked on (use the display:none property).
let h3 = document.querySelector("h3");
h3.addEventListener("click", () => {
    h3.style.display = "none";
});

// Add a <button> to the HTML file, that when clicked on, should make the text of all the paragraphs, bold.
let allParagraphs = document.querySelectorAll("p");
function handleBold() {
    allParagraphs.forEach(paragraph => {
        paragraph.style.fontWeight = 'bold';
    });

}
document.querySelector("button").addEventListener("click", handleBold);

// BONUS : When you hover on the h1, set the font size to a random pixel size between 0 to 100.(Check out this documentation)
h1.addEventListener('mouseover', () => {
    const randomSize = Math.floor(Math.random() * 101);
    h1.style.fontSize = randomSize + 'px';
});

// BONUS : When you hover on the 2nd paragraph, it should fade out (Check out “fade css animation” on Google) -->
h2.addEventListener("mouseover", () => {
    h2.classList.add("fadeOut")
})
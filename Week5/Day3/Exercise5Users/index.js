
// 🌟 Exercise 5 : Users
// Instructions

// Using Javascript:
// Retrieve the div and console.log it
let myContainer = document.getElementById("container");
console.log(myContainer);

// Change the name “Pete” to “Richard”.
let pet = document.getElementsByTagName("li")[1].textContent = "Richard";

// Delete the second < li > of the second < ul >.
document.getElementsByTagName("li")[3].remove();

// Change the name of the first < li > of each < ul > to your name. (Hint : use a loop)
let firstLis = document.querySelectorAll('ul.list li:first-child');
firstLis.forEach(li => {
    li.textContent = 'Avi';
});

// Using Javascript:
// Add a class called student_list to both of the < ul > 's.
let lists = document.querySelectorAll('ul.list');
lists.forEach(ul => {
    ul.classList.add('student_list');
});

// Add the classes university and attendance to the first < ul >.
lists[0].classList.add('university', 'attendance');

// Using Javascript:
// Add a “light blue” background color and some padding to the < div >.
let myDiv = document.querySelector('div');
myDiv.style.backgroundColor = 'lightblue';
myDiv.style.padding = '4vh';

// Do not display the < li > that contains the text node “Dan”.(the last < li > of the first < ul >)
let dan = document.getElementsByTagName("li")[3];
dan.style.display = "none";

// Add a border to the < li > that contains the text node “Richard”.(the second < li > of the < ul >)
let richard = document.getElementsByTagName("li")[1];
richard.style.border = "5px solid red";

// Change the font size of the whole body.
document.querySelector("body").style.fontSize = "2em";

// Bonus: If the background color of the div is “light blue”,
// alert “Hello x and y” (x and y are the users in the div).
if (myDiv.style.backgroundColor === "lightblue") {
    let x = firstLis[0].textContent;
    let y = richard.textContent;
    alert("hello " + x + " and " + y + ".");
}
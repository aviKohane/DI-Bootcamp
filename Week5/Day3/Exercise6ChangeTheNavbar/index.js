// 🌟 Exercise 6 : Change The Navbar
// Instructions
// Create a new structured HTML file and a new Javascript file

// Using Javascript, in the <div>, change the value of the id attribute from navBar to socialNetworkNavigation,
// using the setAttribute method.
document.getElementById('navBar').setAttribute('id', 'socialNetworkNavigation');
// We are going to add a new <li> to the <ul>.
// First, create a new <li> tag (use the createElement method).
let newLi = document.createElement("li");

// Create a new text node with “Logout” as its specified text.
// Append the text node to the newly created list node (<li>).
// Finally, append this updated list node to the unordered list (<ul>), using the appendChild method.
let newTextNode = document.createTextNode("Logout");
newLi.appendChild(newTextNode);
document.querySelector('ul').appendChild(newLi);

// Use the firstElementChild and the lastElementChild properties to retrieve the first and last <li> elements from their parent element (<ul>).
let firstLi = document.querySelector("ul").firstElementChild;
console.log(firstLi)
let lastLi = document.querySelector("ul").lastElementChild;
console.log(lastLi)

// Display the text of each link. (Hint: use the textContent property).
document.querySelectorAll("li").forEach(li => {
    console.log(li.textContent)

});

// Documentation
// Creating/Adding/Deleting DOM Nodes
// 1. Creating Elements: CreateElement()
//   Syntax : document.createElement('tag')
//   let newDiv = document.createElement('div')


// 2. Creating Text: CreateTextNode()
// Syntax : document.createTextNode('text')
// let newTextNode = document.createTextNode('Here I am');


// 3. Adding Element : AppendChild()
// Adding an element as the last child of the node parent

// Syntax: `element.appendChild`
// newDiv.appendChild(newTextNode);
// document.body.appendChild(newDiv);


// 4. Accessing / Changing The HTML Content Of An Element: InnerHTML
// document.getElementById("header").textContent = "Hello World!";
// document.getElementsByTagName("div")[0].innerHTML = "<h1>Hello World!</h1>"


// 5. Deleting Elements: RemoveChild()
// let parentElem = document.getElementById("main");
// let childElem = document.getElementById("hint");
// parentElem.removeChild(childElem);


// Some More Examples:
// // getElementById('id')
// document.getElementById('demo');

// // getElementsByClassName('class')
// document.getElementsByClassName('demo');

// // getElementsByTagName('tag')
// document.getElementsByTagName('p');

// // querySelector('css selector')
// document.querySelector('#demo-query');

// // querySelectorAll('css selector')
//     let demoQueryAll = document.querySelectorAll('.demo-query-all');

//     demoQueryAll.forEach(query => {
//       query.style.border = '1px solid green';
//     });

// 🌟 Exercise 1 : Find The Numbers Divisible By 23
// Instructions
// Create a function call displayNumbersDivisible() that takes no parameter.
// In the function, loop through numbers 0 to 500.

// Console.log all the numbers divisible by 23.

// At the end, console.log the sum of all numbers that are divisible by 23.

// Outcome : 0 23 46 69 92 115 138 161 184 207 230 253 276 299 322 345
// 368 391 414 437 460 483
// Sum : 5313


// Bonus: Add a parameter divisor to the function.

// displayNumbersDivisible(divisor)

// Example:
// displayNumbersDivisible(3) : Console.log all the numbers divisible by 3,
// and their sum
// displayNumbersDivisible(45) : Console.log all the numbers divisible by 45,
// and their sum
let sum = 0;
let divisor = 1;
function displayNumbersDivisible(divisor) {
    for (let i = 0; i < 501; i++) {
        if (i % divisor == 0) {
            console.log(i)
            sum += i;
        }
    }
    console.log("sum : " + sum)
}
displayNumbersDivisible(3);
displayNumbersDivisible(45);





// 🌟 Exercise 2 : Shopping List
// Instructions
// Add the stock and prices objects to your js file.

// Create an array called shoppingList with the following items: “banana”, “orange”, and “apple”. 
// It means that you have 1 banana, 1 orange and 1 apple in your cart.

// Create a function called myBill() that takes no parameters.

// The function should return the total price of your shoppingList. In order to do this you must follow these rules:
// The item must be in stock. (Hint : check out if .. in)
// If the item is in stock find out the price in the prices object.

// Call the myBill() function.

// Bonus: If the item is in stock, decrease the item’s stock by 1
const stock = {
    "banana": 6,
    "apple": 0,
    "pear": 12,
    "orange": 32,
    "blueberry": 1
}
const prices = {
    "banana": 4,
    "apple": 2,
    "pear": 1,
    "orange": 1.5,
    "blueberry": 10
}

let shoppingList = ['banana', 'orange', 'apple'];
function myBill() {
    let price = 0;
    for (let i = 0; i < shoppingList.length; i++) {
        if (stock[shoppingList[i]] > 0) {
            price += prices[shoppingList[i]];
            stock[shoppingList[i]] -= 1;
        }
    }
    console.log(price);
    //checking the stock has decrease.
    console.log(stock);
}

myBill();


// Exercise 3 : What’s In My Wallet ?
// Instructions
// Note: Read the illustration (point 4), while reading the instructions

// Create a function named changeEnough(itemPrice, amountOfChange) that receives two arguments :
// an item price
// and an array representing the amount of change in your pocket.
// In the function, determine whether or not you can afford the item.
// If the sum of the change is bigger or equal than the item’s price (ie. it means that you can afford the item), the function should return true
// If the sum of the change is smaller than the item’s price (ie. it means that you cannot afford the item) the function should return false
// Change will always be represented in the following order: quarters, dimes, nickels, pennies.
// A quarters is 0.25
// A dimes is 0.10
// A nickel is 0.05
// A penny is 0.01

// 4. To illustrate:
// After you created the function, invoke it like this:
// The value 4.25 represents the item’s price
// The array [25, 20, 5, 0] represents 25 quarters, 20 dimes, 5 nickels and 0 pennies.
// The function should return true, since having 25 quarters, 20 dimes, 5 nickels and 0 pennies gives you 6.25 + 2 + .25 + 0 = 8.50 which is bigger than 4.25 (the total amount due)
function changeEnough(itemPrice, amountOfChange) {
    const QUARTER_VALUE = 0.25;
    const DIME_VALUE = 0.10;
    const NICKEL_VALUE = 0.05;
    const PENNY_VALUE = 0.01;

    const totalChange = amountOfChange[0] * QUARTER_VALUE +
        amountOfChange[1] * DIME_VALUE +
        amountOfChange[2] * NICKEL_VALUE +
        amountOfChange[3] * PENNY_VALUE;

    return totalChange >= itemPrice;
}

console.log(changeEnough(4.25, [25, 20, 5, 0])); // true
console.log(changeEnough(14.11, [2, 100, 0, 0])); // false
console.log(changeEnough(0.75, [0, 0, 20, 5])); // true


// 🌟 Exercise 4 : Vacations Costs
// Instructions
// Let’s create functions that calculate your vacation’s costs:

// Define a function called hotelCost().
// It should ask the user for the number of nights they would like to stay in the hotel.
// If the user doesn’t answer or if the answer is not a number, ask again.
// The hotel costs $140 per night. The function should return the total price of the hotel.
function hotelCost() {
    let numberNights;
    do {
        numberNights = prompt("Please enter the number of nights you would like to stay in the hotel:");
    } while (isNaN(numberNights) || numberNights === null || numberNights.trim() === "");

    return 140 * parseInt(numberNights);
}
// Define a function called planeRideCost().
// It should ask the user for their destination.
// If the user doesn’t answer or if the answer is not a string, ask again.
// The function should return a different price depending on the location.
// “London”: 183$
// “Paris” : 220$
// All other destination : 300$
function planeRideCost() {
    let destination;
    do {
        destination = prompt("Please enter your destination(London,Paris or other):").toLowerCase();
    } while (destination !== "paris" && destination !== "london" && destination !== "other");
    switch (destination) {
        case "london":
            return 183;
        case "paris":
            return 220;
        default:
            return 300;
    }

}
// Define a function called rentalCarCost().
// It should ask the user for the number of days they would like to rent the car.
// If the user doesn’t answer or if the answer is not a number, ask again.
// Calculate the cost to rent the car. The car costs $40 everyday.
// If the user rents a car for more than 10 days, they get a 5% discount.
// The function should return the total price of the car rental.
function rentalCarCost() {
    let rentCarDays;
    do {
        rentCarDays = prompt("Please enter the number of days you would like to rent the car:")
    } while (isNaN(rentCarDays) && rentCarDays === null && rentCarDays.trim() === "");
    let carCost = parseInt(rentCarDays * 40);
    if (parseInt(rentCarDays) > 10) {
        carCost *= 0.95;
    }
    return carCost;

}
// Define a function called totalVacationCost() that returns the total cost of the user’s vacation by calling the 3 functions that you created above.
// Example : The car cost: $x, the hotel cost: $y, the plane tickets cost: $z.
// Hint: You have to call the functions hotelCost(), planeRideCost() and rentalCarCost() inside the function totalVacationCost().
function totalVacationCost() {
    const hotel = hotelCost();
    const planeTicket = planeRideCost();
    const carRental = rentalCarCost();

    const totalCost = hotel + planeTicket + carRental;
    console.log(`The hotel cost: $${hotel}, the plane tickets cost: $${planeTicket}, the car rental cost: $${carRental}.`);
    console.log(`Total vacation cost: $${totalCost}.`);
    return totalCost;
}

// Call the function totalVacationCost()
totalVacationCost();

// Bonus: Instead of using a prompt inside the 3 first functions, only use a prompt inside the totalVacationCost() function. You need to change the 3 first functions, accordingly.



// Exercise 7 : My Book List
// Instructions

// The point of this challenge is to display a list of two books on your browser.

// In the body of the HTML page, create an empty section:
// <section class="listBooks"></section>

// In the js file, create an array called allBooks. This is an array of objects. Each object is a book that has 4 keys (ie. 4 properties) :
// title,
// author,
// image : a url,
// alreadyRead : which is a boolean (true or false).
// Create an array called allBooks
// Initiate the array with 2 books of your choice (ie. Add manually 2 books objects in the array)
const allBooks = [
    {
        title: "Harry Potter and the Philosopher's Stone",
        author: 'J. K. Rowling',
        image: 'https://upload.wikimedia.org/wikipedia/en/thumb/7/7a/Harry_Potter_and_the_Philosopher%27s_Stone_banner.jpg/330px-Harry_Potter_and_the_Philosopher%27s_Stone_banner.jpg',
        alreadyRead: false
    },
    {
        title: 'The Little Prince',
        author: '	Antoine de Saint-Exupéry',
        image: 'https://upload.wikimedia.org/wikipedia/en/0/05/Littleprince.JPG',
        alreadyRead: true
    },

];


// Requirements : All the instructions below need to be coded in the js file:
// Using the DOM, render each book inside a div (the div must be added to the <section> created in part 1).
// For each book :
// You have to display the book’s title and the book’s author.
// Example: HarryPotter written by JKRolling.
// The width of the image has to be set to 100px.
// If the book is already read. Set the color of the book’s details to red.


// Iterate through each book in the allBooks array
allBooks.forEach(book => {
    // Create a div element to contain each book
    let bookDiv = document.createElement('div');

    // Set the class of the book div
    bookDiv.classList.add('book');

    // Create a paragraph element for displaying the book details
    let detailsPara = document.createElement('p');

    // Set the text content of the details paragraph
    detailsPara.textContent = `${book.title} written by ${book.author}.`;

    // Set the color of the details paragraph to red if the book is already read
    if (book.alreadyRead) {
        detailsPara.style.color = 'red';
    }

    // Create an image element for displaying the book cover
    let imageElement = document.createElement('img');

    // Set the source and width attributes of the image element
    imageElement.src = book.image;
    imageElement.width = '100';

    // Append the details paragraph and image element to the book div
    bookDiv.appendChild(detailsPara);
    bookDiv.appendChild(imageElement);

    // Append the book div to the section element
    document.querySelector('section').appendChild(bookDiv);
});

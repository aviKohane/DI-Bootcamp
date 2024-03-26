// 🌟 Exercise 2 : Work With Forms
// Instructions
// Copy the code below, into a structured HTML file:

// <form>
//   <label for="fname">First name:</label><br>
//   <input type="text" id="fname" name="firstname"><br>
//   <label for="lname">Last name:</label><br>
//   <input type="text" id="lname" name="lastname"><br><br>
//   <input type="submit" value="Submit" id="submit">
// </form> 
// <ul class="usersAnswer"></ul>


// Retrieve the form and console.log it.
let form = document.querySelector('form');
console.log(form);

// Retrieve the inputs by their id and console.log them.
const fnameInput = document.getElementById('fname');
const lnameInput = document.getElementById('lname');
const submitInput = document.getElementById('submit')
console.log(fnameInput, lnameInput, submitInput)

// Retrieve the inputs by their name attribute and console.log them.
const firstnameInput = document.getElementsByName('firstname')[0];
const lastnameInput = document.getElementsByName('lastname')[0];
console.log(firstnameInput, lastnameInput);

// When the user submits the form (ie. submit event listener)
// use event.preventDefault(), why ?
// get the values of the input tags,
// make sure that they are not empty,
// create an li per input value,
// then append them to a the <ul class="usersAnswer"></ul>, below the form.
// The output should be :

// <ul class="usersAnswer">
//     <li>first name of the user</li>
//     <li>last name of the user</li>
// </ul>

// When the user submits the form
form.addEventListener('submit', (event) => {
    // Prevent the default form submission behavior
    event.preventDefault();

    // Get the values of the input tags
    const fnameValue = fnameInput.value.trim();
    const lnameValue = lnameInput.value.trim();

    // Check if input values are not empty
    if (fnameValue !== '' && lnameValue !== '') {
        // Create li elements for each input value
        const fnameLi = document.createElement('li');
        const lnameLi = document.createElement('li');

        fnameLi.textContent = fnameValue;
        lnameLi.textContent = lnameValue;

        // Append li elements to the ul
        const usersAnswerUl = document.querySelector('.usersAnswer');
        usersAnswerUl.appendChild(fnameLi);
        usersAnswerUl.appendChild(lnameLi);
    }
});

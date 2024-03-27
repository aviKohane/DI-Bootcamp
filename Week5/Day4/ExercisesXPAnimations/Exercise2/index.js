// 🌟 Exercise 2 : Move The Box
// Instructions



// In your Javascript file, use setInterval to move the <div id="animate"> to the right side of the <div id="container">, 
// when the button is clicked on.
// The <div id="animate"> should move 1px to the right every milisecond, until it reaches the end of the <div id="container">.
// Hint : use clearInterval as soon as the box reaches the right end side of the container
// Hint : check out the demonstration in the Course Noted named JS Functions


function myMove() {
    let elem = document.getElementById("animate");
    let pos = 0;
    let id = setInterval(frame, 1);
    function frame() {
        if (pos == 350) { // Adjust this value based on the container width
            clearInterval(id);
        } else {
            pos++;
            elem.style.left = pos + 'px';
        }
    }
}

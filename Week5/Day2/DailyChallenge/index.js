let sentence = "This movie is not so bad !";
let wordNot = sentence.indexOf('not');
console.log(wordNot);
let wordBad = sentence.indexOf('bad');
console.log(wordBad);
let subSentence = sentence.slice(wordNot, (wordBad + "bad".length));
console.log("Your original string is : " + sentence);
// console.log(subSentence);
// console.log('hello');
if (wordNot < wordBad) {
    if (wordNot === -1) {
        console.log("The result is : " + sentence);
    }
    else {
        sentence = sentence.replace(subSentence, "good");
        console.log("The result is : " + sentence);
    }

}
else if (wordBad < wordNot) {
    console.log("The result is : " + sentence);
}


// Write a JavaScript program that recreates the pattern below.
// Do this challenge twice: first by using one loop, then by using two nested for loops (Nested means one inside the other - check out this tutorial of nested loops).
// Do this Daily Challenge by yourself, without looking at the answers on the internet.
// *  
// * *  
// * * *  
// * * * *  
// * * * * *
// * * * * * *
let starsLine = ""
for (let i = 0; i < 6; i++) {
    starsLine += "* ";
    console.log(starsLine);
}

for (let i = 1; i <= 6; i++) {
    let pattern = '';
    for (let j = 1; j <= i; j++) {
        pattern += '* ';
    }
    console.log(pattern);
}

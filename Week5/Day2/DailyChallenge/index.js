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


var input_string = null;

do {
  input_string = window.prompt("What is your input string?");
} while (input_string === null);

console.log("Yo, your string is " + input_string.length + " characters long!")

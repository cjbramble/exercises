var people = window.prompt("How many people?");
var pizzas = window.prompt("How many pizzas do you have?");
var slices = window.prompt("How many slices does each pizza have?");

var product = (pizzas * slices);
var quotient = (product / people);
var remainder = (product % people);

console.log(`${people} people with ${pizzas} pizzas.\nEach person gets ${quotient} pieces of pizza.\nThere are ${remainder} leftover pieces.`);

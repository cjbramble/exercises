var current_age_input = window.prompt("What is your current age?");
var age_to_retire_input = window.prompt("What age would you like to retire?");

var current_age = parseInt(current_age_input);
var age_to_retire = parseInt(age_to_retire_input);

var years_to_retire = (age_to_retire - current_age);

var today = new Date();
var year = today.getFullYear();

console.log(`You have about ${years_to_retire} years to retire.`);
console.log(`It's ${year}, so you can retire in ${year + years_to_retire}.`);

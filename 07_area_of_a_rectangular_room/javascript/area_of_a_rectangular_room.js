const FEET_TO_METERS = 0.09290304;

var length_input = window.prompt("What is the length of the room in feet?");
var width_input = window.prompt("What is the width of the room in feet?");

var length_in_feet = parseInt(length_input);
var width_in_feet = parseInt(width_input);

var area_in_feet = (length_in_feet * width_in_feet);
var area_in_meters = (area_in_feet * FEET_TO_METERS);

console.log(`You entered dimensions of ${length_in_feet} in feet by ${width_in_feet} feet.`)
console.log(`The area is\n${area_in_feet} square feet\n${area_in_meters} square meters.`)

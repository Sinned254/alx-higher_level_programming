#!/usr/bin/node
// Define the add function
function add (a, b) {
  return a + b;
}

// Get the command-line arguments
const args = process.argv.slice(2);

// Convert the arguments to integers
const num1 = parseInt(args[0]);
const num2 = parseInt(args[1]);

console.log(add(num1, num2));

#!/usr/bin/node
// Get the command-line arguments
const args = process.argv.slice(2);

// Convert the first argument to an integer
const number = parseInt(args[0]);

// Check if the conversion was successful and print the corresponding message
if (!isNaN(number)) {
  console.log(`My number: ${number}`);
} else {
  console.log('Not a number');
}

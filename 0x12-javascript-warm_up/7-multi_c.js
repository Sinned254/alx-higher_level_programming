#!/usr/bin/node
// Get the command-line arguments
const args = process.argv.slice(2);

// Convert the first argument to an integer
const x = parseInt(args[0]);

// Check if the conversion was successful and print the corresponding message
if (!isNaN(x)) {
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}

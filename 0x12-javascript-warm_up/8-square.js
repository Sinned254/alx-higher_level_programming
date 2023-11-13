#!/usr/bin/node
// Get the command-line arguments
const args = process.argv.slice(2);

// Convert the first argument to an integer
const size = parseInt(args[0]);

// Check if the conversion was successful and print the corresponding message
if (!isNaN(size)) {
  // Loop to print the square
  for (let i = 0; i < size; i++) {
    let row = '';
    for (let j = 0; j < size; j++) {
      row += 'X';
    }
    console.log(row);
  }
} else {
  console.log('Missing size');
}

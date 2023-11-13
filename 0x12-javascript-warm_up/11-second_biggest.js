#!/usr/bin/node
// Get the command-line arguments
const args = process.argv.slice(2);

// Convert arguments to integers
const numbers = args.map(Number);

// Check the number of arguments and find the second biggest integer
if (numbers.length === 0 || numbers.length === 1) {
  console.log(0);
} else {
  // Find the second biggest integer
  const sortedNumbers = numbers.sort((a, b) => b - a);
  console.log(sortedNumbers[1]);
}

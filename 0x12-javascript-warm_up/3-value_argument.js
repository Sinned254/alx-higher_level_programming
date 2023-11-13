#!/usr/bin/node
// Get the command-line arguments
const args = process.argv.slice(2);

// Check if the first argument exists and print it
if (args[0] !== undefined) {
  console.log(args[0]);
} else {
  console.log('No argument');
}

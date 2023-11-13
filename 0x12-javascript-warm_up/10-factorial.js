#!/usr/bin/node

// Define the factorial function
function factorial (n) {
  if (isNaN(n)) {
    return 1;
  }

  // Base case: factorial of 0 is 1
  if (n === 0) {
    return 1;
  } else {
    // Recursive case: n! = n * (n-1)!
    return n * factorial(n - 1);
  }
}

// Get the command-line arguments
const args = process.argv.slice(2);

// Convert the argument to an integer
const num = parseInt(args[0]);

// Print the factorial using the factorial function
console.log(factorial(num));

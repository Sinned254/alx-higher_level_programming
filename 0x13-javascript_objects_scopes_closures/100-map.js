#!/usr/bin/node
const { list } = require('./100-data');

// Use map to create a new array where each value is the original value multiplied by its index
const newList = list.map((value, index) => value * index);

// Print both the initial list and the new list
console.log('Initial List:', list);
console.log('New List:', newList);

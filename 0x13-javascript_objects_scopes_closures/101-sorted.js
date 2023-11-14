#!/usr/bin/node
const { dict } = require('./101-data');

// Create a new dictionary where keys are occurrences and values are lists of user ids
const occurrencesDict = Object.keys(dict).reduce((newDict, userId) => {
  const occurrences = dict[userId];

  if (!newDict[occurrences]) {
    newDict[occurrences] = [];
  }

  newDict[occurrences].push(userId);

  return newDict;
}, {});

// Print the new dictionary
console.log(occurrencesDict);

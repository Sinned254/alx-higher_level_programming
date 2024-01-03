#!/usr/bin/node
const fs = require('fs');
const filePath = process.argv[2];
const stringToWrite = process.argv[3];

// Write the string to the file in utf-8 encoding
fs.writeFile(filePath, stringToWrite, 'utf-8', (err) => {
  if (err) {
    console.log(err);
  }
});

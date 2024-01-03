#!/usr/bin/node
const fs = require('fs');
const request = require('request');
const url = process.argv[2];
const filePath = process.argv[3];

// Make a GET request to the specified URL
request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else if (response.statusCode !== 200) {
    console.log(`Code: ${response.statusCode}`);
  } else {
    // Write the body response to the specified file in utf-8 encoding
    fs.writeFile(filePath, body, 'utf-8', (err) => {
      if (err) {
        console.log(error);
      }
    });
  }
});

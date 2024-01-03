#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

// Make a GET request and display the status code
request.get(url, (error, response) => {
  if (error) {
    console.log(error);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});

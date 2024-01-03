#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Make a GET request to the Star Wars API
request.get(apiUrl, { json: true }, (error, response, body) => {
  if (error) {
    console.log(error);
  } else if (response.statusCode !== 200) {
    console.log(`Code: ${response.statusCode}`);
  } else {
    console.log(`${body.title}`);
  }
});

#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Make a GET request to the Star Wars API for the specified movie ID
request.get(apiUrl, { json: true }, (error, response, movie) => {
  if (error) {
    console.error(`Error: ${error.message}`);
  } else if (response.statusCode !== 200) {
    console.error(`Error: Request failed with status code ${response.statusCode}`);
  } else {
    // Display one character name per line
    movie.characters.forEach(characterUrl => {
      request.get(characterUrl, { json: true }, (charError, charResponse, character) => {
        if (charError) {
          console.error(`Error: ${charError.message}`);
        } else if (charResponse.statusCode !== 200) {
          console.error(`Error: Request failed with status code ${charResponse.statusCode}`);
        } else {
          console.log(character.name);
        }
      });
    });
  }
});

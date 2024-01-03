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
    // Display one character name per line in the same order as the 'characters' list
    const characterPromises = movie.characters.map(characterUrl => {
      return new Promise((resolve, reject) => {
        request.get(characterUrl, { json: true }, (charError, charResponse, character) => {
          if (charError) {
            reject(charError.message);
          } else if (charResponse.statusCode !== 200) {
            console.log('code:', response.statusCode);
          } else {
            resolve(character.name);
          }
        });
      });
    });

    // Resolve promises and print character names in order
    Promise.all(characterPromises)
      .then(characterNames => {
        characterNames.forEach(name => console.log(name));
      })
      .catch(err => console.error(`Error: ${err}`));
  }
});

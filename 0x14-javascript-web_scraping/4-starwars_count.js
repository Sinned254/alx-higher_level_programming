#!/usr/bin/node
const request = require('request');
const apiUrl = process.argv[2];

// Make a GET request to the Star Wars API films endpoint
request.get(apiUrl, { json: true }, (error, response, body) => {
  if (error) {
    console.log(error);
  } else if (response.statusCode !== 200) {
    console.log(`Code: ${response.statusCode}`);
  } else {
    // Filter movies where Wedge Antilles is present (character ID 18)
    const moviesWithWedge = body.results.filter(movie =>
      movie.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')
    );
    console.log(`${moviesWithWedge.length}`);
  }
});

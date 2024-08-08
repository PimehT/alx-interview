#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];

if (!movieId) {
  console.error('Please provide a Movie ID');
  process.exit(1);
}

const apiUrl = 'https://swapi.dev/api/films/';

request(`${apiUrl}${movieId}/`, (error, response, body) => {
  if (error) {
    console.error('Error fetching movie details:', error);
    process.exit(1);
  }

  const movieData = JSON.parse(body);
  const characters = movieData.characters;

  if (!characters || characters.length === 0) {
    console.log('No characters found for this movie');
    return;
  }

  characters.forEach((characterUrl, index) => {
    request(characterUrl, (error, response, body) => {
      if (error) {
        console.error('Error fetching character details:', error);
        process.exit(1);
      }

      const characterData = JSON.parse(body);
      console.log(characterData.name);
    });
  });
});

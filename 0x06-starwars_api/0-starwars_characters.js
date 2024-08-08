#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];

if (!movieId) {
  console.error('Please provide a Movie ID');
  process.exit(1);
}

const apiUrl = 'https://swapi-api.hbtn.io/api';

request(`${apiUrl}/films/${movieId}/`, async (error, response, body) => {
  if (error) {
    console.log(error);
  }

  const movieData = JSON.parse(body);
  const characters = movieData.characters;

  for (const character of characters) {
    await new Promise((resolve, reject) => {
      request(character, (error, response, body) => {
        if (error) {
          reject(error);
        } else {
          console.log(JSON.parse(body).name);
          resolve(body);
        }
      });
    });
  }
});

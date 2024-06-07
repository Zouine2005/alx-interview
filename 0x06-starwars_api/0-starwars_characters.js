#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const filmEndPoint = `https://swapi-api.hbtn.io/api/films/${movieId}`;

const requestCharacters = async () => {
  return new Promise((resolve, reject) => {
    request(filmEndPoint, (err, res, body) => {
      if (err) {
        reject(`Error: ${err}`);
      } else if (res.statusCode !== 200) {
        reject(`StatusCode: ${res.statusCode}`);
      } else {
        const jsonBody = JSON.parse(body);
        resolve(jsonBody.characters);
      }
    });
  });
};

const requestNames = async (people) => {
  const names = [];
  for (const person of people) {
    const name = await new Promise((resolve, reject) => {
      request(person, (err, res, body) => {
        if (err) {
          reject(`Error: ${err}`);
        } else if (res.statusCode !== 200) {
          reject(`StatusCode: ${res.statusCode}`);
        } else {
          const jsonBody = JSON.parse(body);
          resolve(jsonBody.name);
        }
      });
    });
    names.push(name);
  }
  return names;
};

const getCharNames = async () => {
  try {
    const people = await requestCharacters();
    const names = await requestNames(people);

    names.forEach((name, index) => {
      if (index === names.length - 1) {
        process.stdout.write(name);
      } else {
        process.stdout.write(name + '\n');
      }
    });
  } catch (error) {
    console.error(error);
  }
};

getCharNames();

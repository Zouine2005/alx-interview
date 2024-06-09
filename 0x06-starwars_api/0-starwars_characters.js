// Import the axios library for making HTTP requests
const axios = require('axios');

// URL to get character data from the first film
const url = 'https://swapi.dev/api/films/1/';

// Make an HTTP request using axios
axios.get(url)
  .then(response => {
    const data = response.data;
    console.log('Character names in the film:');
    data.characters.forEach(characterUrl => {
      axios.get(characterUrl)
        .then(characterResponse => {
          console.log(characterResponse.data.name);
        })
        .catch(error => {
          console.error('Error fetching character data:', error.message);
        });
    });
  })
  .catch(error => {
    console.error('Error fetching film data:', error.message);
  });

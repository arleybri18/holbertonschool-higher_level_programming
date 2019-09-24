#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const result = JSON.parse(body).results;
    const listChar = result.map(listC => listC.characters);
    let count = 0;
    listChar.filter(function (it) {
      if (it.includes('https://swapi.co/api/people/18/')) {
        count++;
      }
    });
    console.log(count);
  }
});

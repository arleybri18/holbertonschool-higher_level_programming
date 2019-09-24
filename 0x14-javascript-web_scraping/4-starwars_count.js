#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const result = JSON.parse(body).results;
    /* map return a new list */
    const listChar = result.map(listC => listC.characters);
    /* reduce flat list of lists in a flat list */
    const li = listChar.reduce((acc, it) => [...acc, ...it]);
    /* filter return an array with elements that match condition */
    /* includes validate if the value is present */
    /* https://www.tutorialrepublic.com/javascript-reference/javascript-array-object.php */
    /* https://www.freecodecamp.org/news/15-useful-javascript-examples-of-map-reduce-and-filter-74cbbb5e0a1f/ */
    const count = li.filter(ot => ot.includes('/18/')).length;
    console.log(count);
  }
});

#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const url = process.argv[2];
request(url, function (error, response, body) {
  if (error) console.log(error);
  fs.writeFile(process.argv[3], body, 'utf8', function (err) {
    if (err) {
      console.log(err);
    }
  });
});

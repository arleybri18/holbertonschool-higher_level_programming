#!/usr/bin/node
const fs = require('fs');
fs.readFile(process.argv[2], 'utf8', function (e, data) {
  if (e) return console.error(e);
  process.stdout.write(data);
});

#!/usr/bin/node
const fs = require('fs');
function Concat (a) {
  return (fs.readFileSync(a, 'utf8', function (e, data) {
    if (e) throw e;
    return data;
  }));
}
const first = Concat(process.argv[2]);
const second = Concat(process.argv[3]);
fs.appendFile(process.argv[4], first, function (e) {
  if (e) throw e;
});
fs.appendFile(process.argv[4], second, function (e) {
  if (e) throw e;
});

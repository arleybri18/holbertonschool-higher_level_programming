#!/usr/bin/node
exports.logMe = function (item) {
  function print () {
    count++;
    console.log(count + ': ' + item);
  }
  print(count);
};
let count = 0;

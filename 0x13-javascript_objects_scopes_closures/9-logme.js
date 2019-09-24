#!/usr/bin/node
let count = 0;
exports.logMe = function (item) {
  function print () {
    console.log(count + ': ' + item);
    count++;
  }
  print(count);
};

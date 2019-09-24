#!/usr/bin/node
const list = require('./100-data').list;
/*  var new_array = arr.map(function callback(currentValue[, index[, array]]) {
*      // Return element for new_array
*      }[, thisArg])
*  }) */
const map1 = list.map((x, index) => x * index);
console.log(list);
console.log(map1);

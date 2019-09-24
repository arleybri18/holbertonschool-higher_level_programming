#!/usr/bin/node
exports.converter = function (base) {
  /* return a new function, this function take
the argument sended and convert to base */
  return function (num) {
    /* take a number, use toString to convert
base */
    return num.toString(base);
  };
};
/*
let myConverter = converter(10);

console.log(myConverter(2));
myconverter return anonymous function (), but conserve
the value of base variable, the anonymous function take
the value of num and make the operation
console.log((2))
*/

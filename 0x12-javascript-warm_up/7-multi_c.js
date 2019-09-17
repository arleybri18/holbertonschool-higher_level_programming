#!/usr/bin/node
const arg = process.argv;
let i = 0;
const num = parseInt(Number(arg[2]));
if (num) {
  while (i < num) {
    console.log('C is fun');
    i++;
  }
} else {
  console.log('Missing number of occurrences');
}

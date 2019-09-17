#!/usr/bin/node
const argv = process.argv;
let num = Number(argv[2]);
if (num) {
  num = parseInt(num);
  console.log(`My number: ${num}`);
} else {
  console.log('Not a number');
}

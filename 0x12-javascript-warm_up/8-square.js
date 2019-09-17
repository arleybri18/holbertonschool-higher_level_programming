#!/usr/bin/node
const arg = process.argv;
let i = 0;
let j = 0;
let str = '';
const num = parseInt(Number(arg[2]));
if (num) {
  while (i < num) {
    while (j < num) {
      str = str + 'X';
      j++;
    }
    console.log(str);
    i++;
  }
} else {
  console.log('Missing size');
}

#!/usr/bin/node
const arg = process.argv;
const len = arg.length;
const arr = [];
let i, j;
if (len > 2) {
  /* create new array */
  j = 0;
  for (i = 2; i < len; i++) {
    arr[j] = arg[i];
    j++;
  }
  console.log(arr.sort()[j - 2]);
} else {
  console.log(0);
}

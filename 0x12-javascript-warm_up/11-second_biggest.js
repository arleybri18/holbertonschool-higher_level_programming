#!/usr/bin/node
const arg = process.argv;
const len = arg.length;
const arr = [];
let i, j;
if (len > 3) {
  /* create new array */
  j = 0;
  for (i = 2; i < len; i++) {
    arr[j] = arg[i];
    j++;
  }
  /* use sort function */
  console.log(arr.sort((a, b) => b - a)[1]);
} else {
  console.log(0);
}

#!/usr/bin/node
const arg = process.argv;
function fact (n) {
  let result;
  if (n) {
    if (n === 0) {
      result = 1;
    } else if (n > 0) {
      result = n * fact(n - 1);
    }
  } else {
    result = 1;
  }
  return result;
}

console.log(fact(parseInt(arg[2])));

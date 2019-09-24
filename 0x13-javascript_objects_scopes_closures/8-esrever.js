#!/usr/bin/node
exports.esrever = function (list) {
  const arr = [];
  let i = list.length - 1;
  for (i; i >= 0; i--) {
    arr.push(list[i]);
  }
  return arr;
};

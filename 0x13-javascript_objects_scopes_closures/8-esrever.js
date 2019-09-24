#!/usr/bin/node
exports.esrever = function (list) {
	let arr = [];
	let i = list.length - 1;
	for (i ; i > 0; i--) {
		arr.push(list[i]);
	}
	return arr;
}

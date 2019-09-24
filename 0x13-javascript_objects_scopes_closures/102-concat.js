#!/usr/bin/node
const fs = require('fs');
function Concat (a){
	return fs.readFile(a, 'utf8', function(err, data) {
		return data;
	});
};
console.log(process.argv[2]);
const first = Concat(process.argv[2]);
const second = Concat(process.argv[3]);
console.log(first);
console.log(second);
fs.writeFile(process.argv[4], ""+first + second+"", function(){});

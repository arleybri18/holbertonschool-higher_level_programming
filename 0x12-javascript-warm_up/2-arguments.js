#!/usr/bin/node
const arg = process.argv;
if (arg.length === 3) {
  console.log('Argument found');
} else if (arg.length > 3) {
  console.log('Arguments found');
} else {
  console.log('No argument');
}

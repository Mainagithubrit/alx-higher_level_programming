#!/usr/bin/node
// a script that searches the second biggest integer in the list of arguments.

const list = process.argv.slice(2);
if (list.length === 0 || list.length === 1) {
  console.log(0);
} else {
  list.sort((a, b) => a - b);
  console.log(list[list.length - 2]);
}

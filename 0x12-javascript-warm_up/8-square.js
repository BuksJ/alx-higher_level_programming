#!/usr/bin/node
'use strict';

const argument = process.argv[2];

if (isNaN(argument)) {
console.log('Missing size');
} else {
const size = parseInt(argument);
for (let i = 0; i < size; i++) {
console.log('X'.repeat(size));
}
}

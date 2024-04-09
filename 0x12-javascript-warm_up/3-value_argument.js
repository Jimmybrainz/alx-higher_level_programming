#!/usr/bin/node

const args = process.argv.slice(2);
const firstArgument = args[0];

if (typeof firstArgument === 'undefined') {
	console.log('No argument');
} else {
	console.log(firstArgument);
}

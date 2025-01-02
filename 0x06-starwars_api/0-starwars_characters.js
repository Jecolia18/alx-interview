#!/usr/bin/node
const request = require('request');
const API_URL = 'https://swapi-api.hbtn.io/api';

if (process.argv.length > 2) {
	request(`${API_URL}/films/${process.argv[2]}/`, (err, _, body) => {
		if (err) {

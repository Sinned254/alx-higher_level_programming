#!/usr/bin/node
const request = require('request');

const apiUrl = process.argv[2];

// Make a GET request to the specified API URL
request.get(apiUrl, { json: true }, (error, response, todos) => {
  if (error) {
    console.log(error);
  } else if (response.statusCode !== 200) {
    console.log(`Code: ${response.statusCode}`);
  } else {
    // Filter completed tasks and count them by user id
    const completedTasksByUser = todos.reduce((result, todo) => {
      if (todo.completed) {
        result[todo.userId] = (result[todo.userId] || 0) + 1;
      }
      return result;
    }, {});

    console.log(completedTasksByUser);
  }
});

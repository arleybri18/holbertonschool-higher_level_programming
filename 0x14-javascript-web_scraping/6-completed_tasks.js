#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    /* get JSON data */
    const data = JSON.parse(body);
    /* filter with task completed */
    const dataFilter = data.filter(it => it.completed === true);
    /* reduce count by UserId */
    const groupByTodo = dataFilter.reduce((acc, it) => {
      acc[it.userId] = acc[it.userId] + 1 || 1;
      return acc;
    }, {});
    console.log(groupByTodo);
  }
});

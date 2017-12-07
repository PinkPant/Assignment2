'use strict';

const express = require('express');

// Constants
const PORT = 9000;

// App
const app = express();
app.get('/', function (req, res) {
  res.send('NodeJS: Hello World\n');
});

app.listen(PORT);
console.log('Running on http://localhost:' + PORT);

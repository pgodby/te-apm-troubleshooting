// Use Express
const express = require('express');
const app = express();

// number of received requests
let count = 0;

// publish a /api endpoint for HTTP GET requests
app.get("/api", (req, res) => {
    console.log(`${++count} [GET] /api`);
    res.status(200).json({'count': count});
});

// All other GET requests
app.get("*", (req, res) => {
    res.sendStatus(404);
});

// start the server
app.listen(3000, () => {
    console.log('Server listening on 3000');
});
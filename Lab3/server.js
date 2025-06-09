const express = require('express');
const app = express();
const port = 8080;

//HTML route 1
app.get('/', (req, res) => {
  res.send('Hello World!');
});

//HTML route 2
app.get('/hello_there', (req, res) => {
  res.send('General Kenobi!');
});

//HTML route 3
app.get('/contact', (req, res) => {
  res.send('My email is trant44@wit.edu');
});

//HTML route 4
app.get('/crazy', (req, res) => {
  res.send('Crazy? I was crazy once. They locked me in a room, a rubber room. A rubber room with rats. Rats make me crazy. Crazy? I was crazy once.');
});

//HTML route 5
app.get('/about', (req, res) => {
    res.send('I do not know about this. Do you?');
});



app.listen(port, () => {
  console.log(`Server is running at http://localhost:${port}`);
});



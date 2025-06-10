const express = require('express');
const app = express();
const port = 8080;

app.use(express.json());

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

//Query 1
app.get('/search', (req, res) => {
    const {q} = req.query;
    if (q) {
        res.send(`You searched for: ${q}`);
    } else {
        res.send('No search query provided.');
    }
})

//Query 2
app.get('/heyo', (req, res) => {
    const {name} = req.query;
    if (name) {
        res.send(`Heyo, ${name}!`);
    } else {
        res.send('Heyo, stranger!');
    }
});

//Query 3
app.get('/sum', (req, res) => {
    const a = parseInt(req.query.a);
    const b = parseInt(req.query.b);
    if ( Number.isInteger(a) && Number.isInteger(b)) {
        const sum = a + b;
        res.send(`The sum of ${a} and ${b} is ${sum}.`);
    } else {
        res.send('Please provide valid integers for a and b.');
    }
})

//Query 4
app.get('/subtract', (req, res) => {
    const a = parseInt(req.query.a);
    const b = parseInt(req.query.b);
    if ( Number.isInteger(a) && Number.isInteger(b)) {
        const difference = a - b;
        res.send(`The difference between ${a} and ${b} is ${difference}.`);
    } else {
        res.send('Please provide valid integers for a and b.');
    }
})

//Query 5
app.get('/multiply', (req, res) => {
    const a = parseInt(req.query.a);
    const b = parseInt(req.query.b);
    if ( Number.isInteger(a) && Number.isInteger(b)) {
        const product = a * b;
        res.send(`The product of ${a} and ${b} is ${product}.`);
    } else {
        res.send('Please provide valid integers for a and b.');
    }
});

//Header
app.get('/header', (req, res) => {
    const token = req.headers['token'];
    if (token) {
        res.send(`Token received: ${token}`);
    }
    else {
        res.send('No token provided in the header.');
    }
});

//Body Input
app.post('/submit', (req, res) => {
    const {name, age} = req.body;
    res.send(`Name: ${name}, Age: ${age}`);
});

app.listen(port, () => {
  console.log(`Server is running at http://localhost:${port}`);
});



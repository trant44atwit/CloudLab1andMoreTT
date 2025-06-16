# Lab 3 Node.js Express Web Service

## Introduction

This project is a simple Node.js web service using **Express**. It includes a variety of routes that return HTML Content, have query parameters, header parameters, and body inputs.

---

## Description

This Express app features:

- **5 HTML routes** (return plain text content)
- **5 routes with query parameters** (perform simple logic based on query inputs)
- **1 route that uses a custom header**
- **1 route that accepts JSON body input via POST**

It serves as an example of handling different types of requests in the Node.js service.

---

## Design

### Packages
- Node.js
- Express.js

### Route Overview

| Route                    | Method | Type              | Description                                 |
|--------------------------|--------|-------------------|---------------------------------------------|
| `/`                      | GET    | HTML              | Returns "Hello World!"                      |
| `/hello_there`           | GET    | HTML              | Returns a Star Wars meme reference          |
| `/contact`               | GET    | HTML              | Returns email contact info                  |
| `/crazy`                 | GET    | HTML              | Returns a humorous quote                    |
| `/about`                 | GET    | HTML              | Returns a vague message                     |
| `/search?q=word`         | GET    | Query             | Echoes back the search term                 |
| `/heyo?name=Timmy`       | GET    | Query             | Personalized greeting using name            |
| `/sum?a=3&b=4`           | GET    | Query             | Returns the sum of two integers             |
| `/subtract?a=10&b=4`     | GET    | Query             | Returns the difference of two integers      |
| `/multiply?a=3&b=5`      | GET    | Query             | Returns the product of two integers         |
| `/header`                | GET    | Header            | Reads a `token` from the request header     |
| `/submit`                | POST   | JSON Body         | Accepts and returns a name and age JSON     |

---

## How to Run the Project

### Install Dependencies

Make sure Node.js is installed. Then run these commands in the terminal of the directory for Lab 3 if package.json and package-lock.json are not present:

"npm init -y"

"npm install express"

### Running the server

After, type in the terminal "node server.js" then click on the provided web link (http://localhost:8080/).

To test routes, type in the routes shown above. Try your own parameters too!

**Note:** For header and submit, use Postman to test the token for /header and POST for /submit.

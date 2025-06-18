# CloudLab1and2TT

## Introduction

This is a simple FastAPI service that displays the usage of different types of routes(simple route, query string route, and path route).

FastAPI: FastAPI is a modern web framework for building HTTP-based service APIs using Python.

Uvicorn: Uvicorn is a fast ASGI web server designed for running Python web applications. It works well and is compatible with FastAPI.

---

## Lab Description

The application is built using Python and the FastAPI framework. The various routes return greetings, perform simple math operations, return messages based on input, and display the current date/time.

The API supports both GET and POST requests and includes use of query parameters, path parameters, and request bodies.

Lab 2 Update:

HTTP headers and cookies have been implemented.

A Python Driver Line has also been added for ease of testing for the routes.

---

## Lab Design

The lab consists of the following main components:

- **GET Endpoints**:
  - `/` - Returns a welcome message.
  - `/greetings` - Accepts `name` and `age` as query parameters.
  - `/salutations/{name}/{age}` - Accepts `name` and `age` as path parameters.
  - `/time` and `/date` - Returns the current time and date.
  - `/addition` and `/subtraction` - Performs simple arithmetic using query parameters.
  ## Lab 2 Additions
  - `/headers` - Reads custom `user-email` and `my_val` headers from the request.
  - `readCookie` - Retrieves a cookie `username` inputted.

- **POST Endpoints**:
  - `/Yoda_personclass` - Accepts a `name` and `age` to return a Yoda-style sentence.
  - `/Arrow` - Accepts `range1` and `range2` to return a formatted arrow range string.
  - `/choice` - Accepts two string choices and returns a sentence offering a choice.
 
  **CLI (Command Line Interface)**
- A Python Driver Line that provides a menu of all implemented routes.

**Models used:**
- `PersonInput`: for Yoda-style greeting
- `Arrow`: for range options
- `Choice`: for choice message

---

## How to Run the Project

### Prerequisites

- Python 3.8 or higher
- `pip` package manager
- FastAPI and Uvicorn installed

### Install Dependencies

You can install the required libraries using:

pip install fastapi uvicorn fastapi pydantic or py -m pip install uvicorn fastapi pydantic

## Running the Server

Open up the terminal in the directory of main.py (Lab2) and type in: uvicorn main:app --port 8080 --reload

Terminal will confirm start-up of the server and provide a url to the page.

## Using the CLI (Lab 2 Addition)

Go to the cli.py file and run the file.

If an input is needed, the terminal will ask the user for input.

The CLI will run until told to stop.

The terminal will pop up and display a menu of the available routes. 

Choose a desired route and input items as needed.

Rinse and repeat for other routes and exit by stopping the program or enter 0 or 13 depending on if you are at the end of a route or in the menu.

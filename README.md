# CloudLab1TT

## Introduction

This is a simple FastAPI service that displays the usage of different types of routes(simple route, query string route, and path route).

---

## Project Description

The application is built using Python and the FastAPI framework. The various routes return greetings, perform simple math operations, return messages based on input, and display the current date/time.

The API supports both GET and POST requests and includes use of query parameters, path parameters, and request bodies.

---

## Project Design

The project consists of the following main components:

- **GET Endpoints**:
  - `/` - Returns a welcome message.
  - `/greetings` - Accepts `name` and `age` as query parameters.
  - `/salutations/{name}/{age}` - Accepts `name` and `age` as path parameters.
  - `/time` and `/date` - Returns the current time and date.
  - `/addition` and `/subtraction` - Performs simple arithmetic using query parameters.

- **POST Endpoints**:
  - `/Yoda_personclass` - Accepts a JSON object with `name` and `age` to return a Yoda-style sentence.
  - `/Arrow` - Accepts `range1` and `range2` to return a formatted arrow range string.
  - `/choice` - Accepts two string choices and returns a sentence joining them.

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

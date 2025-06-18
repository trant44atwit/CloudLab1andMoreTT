# FastAPI and Docker Lab

## Introduction

This lab containerizes the previously built **FastAPI** web service with **CLI**. It showcases a remote connection to routes with query parameters, path parameters, request bodies, headers, and cookies — all packaged in a Docker container.

---

## Description

This lab uses Docker to containerize the already built Python FastAPI web service.

**Features:**

- Multiple GET and POST routes for greetings, math operations, date/time, and more.
- CLI with an interactive menu to make HTTP requests to the FastAPI backend.
- Backend runs inside a Docker container with **Uvicorn** as the server.

**FastAPI Routes**
- **GET Endpoints**:
  - `/` - Returns a welcome message.
  - `/greetings` - Accepts `name` and `age` as query parameters.
  - `/salutations/{name}/{age}` - Accepts `name` and `age` as path parameters.
  - `/time` and `/date` - Returns the current time and date.
  - `/addition` and `/subtraction` - Performs simple arithmetic using query parameters.
  - `/headers` - Reads custom `user-email` and `my_val` headers from the request.
  - `readCookie` - Retrieves a cookie `username` inputted.

 - **POST Endpoints**:
  - `/Yoda_personclass` - Accepts a `name` and `age` to return a Yoda-style sentence.
  - `/Arrow` - Accepts `range1` and `range2` to return a formatted arrow range string.
  - `/choice` - Accepts two string choices and returns a sentence offering a choice.

---

## Design
Lab Structure:
Lab4/

├── main.py             # FastAPI application

├── cli.py              # Command-line interface 

├── requirements.txt    # Package installations for Docker

├── Dockerfile          # Docker configuration

├── .dockerignore       # Files to ignore during Docker build

└── README.md           # Project documentation

## Running the Project

Make sure Docker is open and running.

In the terminal of the directory of Lab 4, type: "docker build -t lab4 ."

Once all packages have been installed, type: "docker run -p 8080:8080 lab4"

This will run the Docker build and allow you to access the web service.

Go to Docker, then go to the "Containers" tab, and click on the "8080:8080" link under the ports section (will be highlighted in blue).

This will bring you to the web page.

Test the FastAPI mentioned in the description as needed.



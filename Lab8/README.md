# Lab 8: CLI Menu with FastAPI, Database Interaction, MinIO, Postfix, and Redis

## Introduction

This project is a command-line interface (CLI) that connects to a full stack of containerized services including:

- FastAPI
- MySQL (preloaded with `my_guitar_shop`)
- Redis (shared memory)
- MinIO (shared file system)
- Postfix (email server)

It provides a framework for testing communication, shared memory, storage, and API-driven development.

---

## Description

The project includes:

- A **FastAPI server** with multiple routes that demonstrate working with query strings, path parameters, headers, cookies, and JSON bodies.
- A **MySQL database** (`my_guitar_shop`) containing realistic shop data across tables such as `products`, `orders`, `customers`, and more.
- A **Python command-line interface (CLI)** that allows the user to interact with either API routes or database queries through a menu-driven terminal interface.
- A **Redis** service that allows for shared memory.
- A **Postfix** service for an email server.
- A **MinIO** service for a shared file system.
- A **unit testing suite** built with `unittest` to validate both the FastAPI routes and MySQL queries, ensuring outputs are as expected.

The CLI lets you interact with:
- **FastAPI routes** to demonstrate query parameters, headers, cookies, and more
- **MySQL** for executing prebuilt SQL queries against a guitar shop database
- **Redis** to test shared in-memory key-value access
- **MinIO** to simulate file sharing via object storage
- **Postfix** to send test emails through a local SMTP server

All services are Dockerized and designed to work together in a service-style environment.

---

## Design

Lab8/

├── cli.py # Command-line interface 

├── main.py # FastAPI app with 13 routes

├── test_L2.py # Unit tests for API endpoints and SQL queries

├── Dockerfile # FastAPI container build file

├── docker-compose.yml # Docker Compose config for FastAPI + MySQL + MinIO + Postfix + Redis

├── requirements.txt # Python dependencies for FastAPI container

├── createguitar.sql # SQL script to initialize the database

└── README.md 

### FastAPI Route Summary (`main.py`)

| Route                          | Method | Description                                         |
|-------------------------------|--------|-----------------------------------------------------|
| `/`                           | GET    | Returns a welcome message                          |
| `/greetings`                  | GET    | Uses query params for name and age                 |
| `/salutations/{name}/{age}`   | GET    | Accepts path parameters for greeting               |
| `/Yoda_personclass`           | POST   | Yoda-style reply from JSON body                    |
| `/time`                       | GET    | Returns current system time                        |
| `/date`                       | GET    | Returns current system date                        |
| `/addition`                   | GET    | Adds two numbers from query params                 |
| `/subtraction`                | GET    | Subtracts two numbers from query params            |
| `/Arrow`                      | POST   | Takes two range values via JSON                    |
| `/Choice`                     | POST   | Returns one of two choices from JSON               |
| `/headers/`                   | GET    | Reads custom headers                               |
| `/readCookie`                 | GET    | Returns username from cookie                       |

### Database: `my_guitar_shop`

The DB includes:

- `products`, `categories`
- `customers`, `addresses`
- `orders`, `order_items`
- `administrators`

### Query Capabilities

- Single-table queries
- `INNER JOIN` with multiple relations
- `GROUP BY` on state, city, category, customer

These are tested through both the CLI and `unittest`.

### Containers

This lab uses **Docker Compose** to define and run two fully containerized services:

### FastAPI Service

- **Built from a local `Dockerfile`**
- Based on a minimal `python:3.9-alpine` image
- Installs dependencies from `requirements.txt`
- Runs the `main.py` FastAPI app using **Uvicorn** on port `8080`
- Exposed on the host machine at: [http://localhost:8080](http://localhost:8080)

---

### MySQL Service 

- Uses the official `mysql:latest` image
- Configured with root password: `CCLab7`
- Exposes MySQL on port `3307` (mapped from internal `3306`)
- Persists all database data in a Docker volume named `lab7database`
- Automatically initializes with the `my_guitar_shop` schema using `createguitar.sql`

---

### Redis Service

- Uses the official `redis:latest` image
- Runs a default Redis server with no password (development only)
- Exposes Redis on port `6379`
- Mounts a Docker volume `redis_data` for persistence
- Accessible from the CLI via Python’s `redis` client

---

### MinIO Service

- Uses the official `minio` image
- Starts the MinIO server at [http://localhost:9000](http://localhost:9000)
- Web console available at: [http://localhost:9001](http://localhost:9001)
- Uses access key `miniolab8` and secret key `12345678`
- Stores uploaded files in the `minio-data` volume

---

### Postfix Service

- Uses the community's `boky/postfix` image for local mail relaying
- Accepts SMTP connections on port `1587`
- Simulates outbound email delivery for development and testing
- Emails sent using Python’s built-in `smtplib` library

## How to Run the Project

### Prerequisites

- Docker & Docker Compose installed
- Python 3.9+ (for CLI and unit tests)
- Dbeaver
- MySQL client 

### Container and Database Setup

- cd into the Lab8 directory and have Docker running.
- Open the terminal and run "docker compose up --build". Note: This should start up all the services.
- Navigate to Dbeaver and create a new connection with the port being 3311.
- Enter the password as "CCLab8".
- Test the connection. Note: If you receive an error of "Public Key Retrieval is not allowed", click on the "Driver properties" tab, look for "allowPublicKeyRetrieval" and change the value from "false" to "true".
- Click "OK" and connect to it.


#### 1. Create and Populate the Database

- Open `createguitar.sql` in DBeaver.
- Run the entire script to:
- Create the `my_guitar_shop` database
- Create tables and insert sample data

#### 2. Verify Database Setup

- Refresh the table list in your SQL tool.
- Ensure `my_guitar_shop` appears with all tables.

#### 3. Run the Queries

- Open `guitar_shop_queries.sql` in a new SQL editor.
- Execute each of the 15 queries (individually or all at once).
- Results will display in the query result pane.

### Running Query Script

#### 1. Creating Initial Script
- Right-click the local host in the connection list on the left.
- Hover over "SQL Editor" and click "New SQL script".
- Copy all of the content in the "queries.sql" file and paste it into the new script page.
- Double-check that the selected database is "my_guitar_shop" next to "localhost" in the hot bar at the top.

#### 2. Running script
- Click the "Execute SQL script" (or use ALT + X) to run the script.
- Allow some time for the script to run, and then all the queries will appear at the bottom in separate tabs.

## FastAPI

Go to Docker, then go to the "Containers" tab, expand the menu under Lab8, and click on the "8080:8080" link under the ports section (will be highlighted in blue).

This will bring you to the web page.

Test the FastAPI mentioned in the description as needed.

### Header Testing

Make sure the request is "GET".

Type into the URL section: http://localhost:8080/header

Navigate to the Headers Tab and under "Key", type in "Token" then a value next to it.

Hit "Send" and the terminal in Postman will display the Key and Value.

### Submit Testing

Make sure the request is "POST".

Type into the URL section: http://localhost:8080/submit

Navigate to the Body tab and click on "raw"

Copy and paste this into the body:

{

  "name": "",
  
  "age": 
  
}

Fill in your own parameters then click "Send".

The terminal in Postman will display the name and age just inputted.

## CLI (Uses containerized MySQL and FastAPI)

Running the CLI is simple. Navigate to the CLI file and run it. You will be prompted to choose a menu or exit.

### FAST Menu
- Uses the FastAPI service and allows testing of every route from the terminal
- Prompts user for input if needed
- Allows for termination of the program or return to the main menu

### Option Menu
- Uses MySQL container queries
- Retrieves data from the database within the containerized MySQL
- Allows for easy testing of grabbing specific queries from the guitar shop database within the terminal

### Redis Menu
- Connects to the Redis container from the CLI
- Demonstrates shared memory by writing and reading a key-value pair
- Simulates inter-process communication using Redis `set` and `get`
- Offers a simple way to validate in-memory data persistence and retrieval

### MinIO Menu
- Connects to the MinIO object storage from the CLI
- Lets users upload file content directly from the terminal into a specified bucket
- Lists all objects in a given bucket and prints the contents of each
- Demonstrates shared file system interaction

### Postfix Menu
- Sends a test email using Python’s built-in SMTP client and the Postfix container
- Prompts user for sender/recipient details and message body
- Validates email construction and delivery through a local unauthenticated SMTP server
- Helps simulate email dispatch functionality in development

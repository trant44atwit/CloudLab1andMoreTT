# Lab 7 – Containerization of Python FastAPI and MySQL Database with CLI

## Introduction

This project demonstrates the integration of a **FastAPI web service** with a **MySQL relational database**, alongside a custom-built **Python CLI** and comprehensive **unit testing suite**. It showcases how web APIs can interact with both dynamic HTTP routes and static SQL queries.

---

## Description

The project includes:

- A **FastAPI server** with multiple routes that demonstrate working with query strings, path parameters, headers, cookies, and JSON bodies.
- A **MySQL database** (`my_guitar_shop`) containing realistic e-commerce data across tables such as `products`, `orders`, `customers`, and more.
- A **Python command-line interface (CLI)** that allows the user to interact with either API routes or database queries through a menu-driven terminal interface.
- A **unit testing suite** built with `unittest` to validate both the FastAPI routes and MySQL queries, ensuring correctness and coverage.

---

## Design

Lab7/

├── cli.py # Command-line interface (API and SQL options)

├── main.py # FastAPI app with 13 routes

├── test_L2.py # Unit tests for API endpoints and SQL queries

├── Dockerfile # FastAPI container build file

├── docker-compose.yml # Docker Compose config for FastAPI + MySQL

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


## How to Run the Project

### Prerequisites

- Docker & Docker Compose installed
- Python 3.9+ (for CLI and unit tests)
- Dbeaver
- MySQL client 

### Container Setup

- cd into the Lab7 directory and have Docker running.
- Open the terminal and run "docker-compose up -d" (or "docker compose up -d"). Note: This should start up both the FastAPI and MySQL services.
- Navigate to Dbeaver and create a new connection with the port being 3307.
- Enter the password as "CCLab7".
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
Allow some time for the script to run, and then all the queries will appear at the bottom in separate tabs.






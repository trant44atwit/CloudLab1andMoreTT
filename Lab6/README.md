# Lab 6

## Introduction

This lab involves containerizing the simulated retail database for an online guitar store called **My Guitar Shop** which was created in lab 5. Lab 5 also included the use of SQL fundamentals including table creation, data manipulation, and writing a variety of queries using joins, functions, and groupings.

---

## Description

The project uses a pre-written SQL script to create and populate a database (`my_guitar_shop`) with several interrelated tables:

- `products`, `categories`
- `customers`, `addresses`
- `orders`, `order_items`
- `administrators`

After the database is created and populated, a set of **16 SQL queries** is developed to extract data from the database. These queries demonstrate:

- Simple single-table `SELECT` statements  
- `INNER JOIN`s across related tables  
- Use of functions like `SUM`, `COUNT`, and `AVG`  
- Grouping data using `GROUP BY`

---

## Design

The database follows the setup of an e-commerce application:

- Products belong to categories.
- Customers can have multiple addresses (shipping and billing).
- Orders are placed by customers and contain multiple order items.
- Administrators are managed separately.

### Tables Overview

| Table             | Purpose                                  |
|------------------|-------------------------------------------|
| `products`        | Guitar and accessory listings             |
| `categories`      | Product categories (guitars, basses, etc.)|
| `customers`       | User account information                  |
| `addresses`       | Shipping and billing addresses            |
| `orders`          | Purchase orders placed by customers       |
| `order_items`     | Line items for each order                 |
| `administrators`  | Admin users with login credentials        |

---

## How to Run This Project

### Prerequisites

- **MySQL Server** installed locally (via [MySQL Installer](https://dev.mysql.com/downloads/installer/))
- **MySQL Workbench** or **DBeaver**
- A MySQL user account (default: `root`)

---

### Setup Instructions

### Container Setup

- cd into the Lab6 directory and have Docker running.
- Open the terminal and run "docker-compose up -d" ("docker compose up -d" for Windows).
- Navigate to Dbeaver and create a new connection with the port being 3310.
- Enter the password as "CCLab6".
- Test the connection. Note: If you recieve an error of "Public Key Retrieval is not allowed", click on the "Driver properties" tab, look for "allowPublicKeyRetrieval" and change the value from "false" to "true".
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


import requests
import mysql.connector
import os

PORT = "http://localhost:8080"

db = mysql.connector.connect(
    host="localhost",
    port=3307,
    user="root",
    password="CCLab7",
    database="my_guitar_shop"
)
cursor = db.cursor()

def run_sql_query(query):
    cursor.execute(query)
    results = cursor.fetchall()
    for row in results:
        print(row)
    input("Press Enter to return to the DB query menu")


def menu():
    print("\nChoose a route:")
    print("1. Root")
    print("2. Greetings")
    print("3. Salutations/{name}/{age}")
    print("4. Yoda")
    print("5. Time")
    print("6. Date")
    print("7. Addition")
    print("8. Subtraction")
    print("9. Arrow Range")
    print("10. Choice")
    print("11. Headers")
    print("12. readCookie")
    print("13. Terminate CLI")
    print("14. Main Menu")


def call_root():
    response = requests.get(f"{PORT}/")
    print(response.json())
    choice = input("Enter anything to return to menu or 0 to exit: ")
    if choice == "0":
        exit()


def call_greetings():
    name = input("Enter name: ")
    age = input("Enter age: ")
    response = requests.get(f"{PORT}/greetings", params={"name": name, "age": age})
    print(response.text)
    choice = input("Enter anything to return to menu or 0 to exit: ")
    if choice == "0":
        exit()

def call_salutations():
    name = input("Enter name: ")
    age = input("Enter age: ")
    response = requests.get(f"{PORT}/salutations/{name}/{age}")
    print(response.json())
    choice = input("Enter anything to return to menu or 0 to exit: ")
    if choice == "0":
        exit()

def call_Yoda():
    name = input("Enter name: ")
    age = input("Enter age: ")
    info1 = {"name": name, "age": age}
    response = requests.post(f"{PORT}/Yoda_personclass", json=info1)
    print(response.json())
    choice = input("Enter anything to return to menu or 0 to exit: ")
    if choice == "0":
        exit()

def call_time():
    response = requests.get(f"{PORT}/time")
    print(response.json())
    choice = input("Enter anything to return to menu or 0 to exit: ")
    if choice == "0":
        exit()

def call_date():
    response = requests.get(f"{PORT}/date")
    print(response.json())
    choice = input("Enter anything to return to menu or 0 to exit: ")
    if choice == "0":
        exit()

def call_addition():
    int1 = input("Enter first integer: ")
    int2 = input("Enter second integer: ")
    response = requests.get(f"{PORT}/addition", params={"int1": int1, "int2": int2})
    print(response.json())
    choice = input("Enter anything to return to menu or 0 to exit: ")
    if choice == "0":
        exit()

def call_subtraction():
    int1 = input("Enter first integer: ")
    int2 = input("Enter second integer: ")
    response = requests.get(f"{PORT}/subtraction", params={"int1": int1, "int2": int2})
    print(response.json())
    choice = input("Enter anything to return to menu or 0 to exit: ")
    if choice == "0":
        exit()

def call_arrow():
    int1 = input("Enter first integer: ")
    int2 = input("Enter second integer (preferably larger than first integer): ")
    info = {"range1": int1, "range2": int2}
    response = requests.post(f"{PORT}/Arrow", json=info)
    print(response.json())
    choice = input("Enter anything to return to menu or 0 to exit: ")
    if choice == "0":
        exit()

def call_choice():
    c1 = input("Enter first choice: ")
    c2 = input("Enter second choice: ")
    info2 = {"c1": c1, "c2": c2}
    response = requests.post(f"{PORT}/Choice", json=info2)
    print(response.json())
    choice = input("Enter anything to return to menu or 0 to exit: ")
    if choice == "0":
        exit()

def call_headers():
    url = "http://localhost:8080/headers/"
    email = input("Enter email: ")
    val = input("Enter your value: ")
    headers = {
        "user-email": email,
        "my-val": val
    }
    response = requests.get(url=url, headers=headers)
    print(response.json())
    choice = input("Enter anything to return to menu or 0 to exit: ")
    if choice == "0":
        exit()

def call_cookie():
    username = input("Enter username: ")
    cookies = {"username": username}
    response = requests.get(f"{PORT}/readCookie", cookies=cookies)
    print(response.json())
    choice = input("Enter anything to return to menu or 0 to exit: ")
    if choice == "0":
        exit()

def main():
    while True:
        print("\nFast = FastAPI routes (like before)")
        print("Options = Run SQL database queries")
        print("Exit = Exit the CLI")
        initialchoice = input("\nChoose initial path:")
        if initialchoice.lower() == "fast":
            fast_menu()
        elif initialchoice.lower() == "options":
            db_query_menu()
        elif initialchoice.lower() == "exit":
            exit()
        else:
            print("Invalid choice. Please try again.")



def fast_menu():
    while True:
        menu()
        choice = input("Enter route number (1-14): ")

        if choice == "1":
            call_root()
        elif choice == "2":
            call_greetings()
        elif choice == "3":
            call_salutations()
        elif choice == "4":
            call_Yoda()
        elif choice == "5":
            call_time()
        elif choice == "6":
            call_date()
        elif choice == "7":
            call_addition()
        elif choice == "8":
            call_subtraction()
        elif choice == "9":
            call_arrow()
        elif choice == "10":
            call_choice()
        elif choice == "11":
            call_headers()
        elif choice == "12":
            call_cookie()
        elif choice == "13":
            exit()
        elif choice == "14":
            main()
        else:
            print("Invalid choice, please try again.")

def db_query_menu():
    while True:
        print("\nDatabase Query Menu")
        print("1. Show all products")
        print("2. Show all categories")
        print("3. Show all addresses in CA")
        print("4. Show products > $700")
        print("5. Show admin email addresses")
        print("6. Product names with category names")
        print("7. Orders with customer names")
        print("8. Order items with product names")
        print("9. Orders with shipping address details")
        print("10. Customer orders and total quantity")
        print("11. Count of addresses per state")
        print("12. Average product price per category")
        print("13. Total number of orders per customer")
        print("14. Total revenue (price - discount)")
        print("15. Orders with full name + shipping cost")
        print("16. Count of addresses per city")
        print("17. Terminate CLI")
        print("18. Return to Main Menu")

        qchoice = input("Enter your query number (1-17): ")

        if qchoice in queries:
            run_sql_query(queries[qchoice])
        elif qchoice == "17":
            exit()
        elif qchoice == "18":
            break
        else:
            print("Invalid choice. Please try again.")

queries = {
            "1": "SELECT * FROM products;",
            "2": "SELECT * FROM categories;",
            "3": "SELECT * FROM addresses WHERE state = 'CA';",
            "4": "SELECT product_name, list_price FROM products WHERE list_price > 700;",
            "5": "SELECT email_address FROM administrators;",
            "6": """SELECT products.product_name, categories.category_name
                    FROM products
                    INNER JOIN categories ON products.category_id = categories.category_id;""",
            "7": """SELECT orders.order_id, orders.order_date, customers.first_name, customers.last_name
                    FROM orders
                    INNER JOIN customers ON orders.customer_id = customers.customer_id;""",
            "8": """SELECT order_items.order_id, products.product_name, order_items.quantity
                    FROM order_items
                    INNER JOIN products ON order_items.product_id = products.product_id;""",
            "9": """SELECT orders.order_id, addresses.line1, addresses.city, addresses.state
                    FROM orders
                    INNER JOIN addresses ON orders.ship_address_id = addresses.address_id;""",
            "10": """SELECT customers.first_name, customers.last_name, orders.order_id,
                            SUM(order_items.quantity) AS total_items
                     FROM customers
                     INNER JOIN orders ON customers.customer_id = orders.customer_id
                     INNER JOIN order_items ON orders.order_id = order_items.order_id
                     GROUP BY orders.order_id, customers.first_name, customers.last_name;""",
            "11": "SELECT state, COUNT(*) AS num_addresses FROM addresses GROUP BY state;",
            "12": """SELECT categories.category_name, AVG(products.list_price) AS avg_price
                     FROM products
                     INNER JOIN categories ON products.category_id = categories.category_id
                     GROUP BY categories.category_name;""",
            "13": """SELECT customers.first_name, customers.last_name, COUNT(orders.order_id) AS num_orders
                     FROM customers
                     INNER JOIN orders ON customers.customer_id = orders.customer_id
                     GROUP BY customers.customer_id;""",
            "14": "SELECT SUM(item_price - discount_amount) AS total_revenue FROM order_items;",
            "15": """SELECT orders.order_id, customers.first_name, customers.last_name, orders.ship_amount
                     FROM orders
                     INNER JOIN customers ON orders.customer_id = customers.customer_id;""",
            "16": "SELECT city, COUNT(*) AS num_addresses FROM addresses GROUP BY city;"
        }

if __name__ == "__main__":
    main()
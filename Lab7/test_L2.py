import unittest
import requests
import mysql.connector

PORT = "http://localhost:8080"

db = mysql.connector.connect(
    host="localhost",
    port=3307,
    user="root",
    password="CCLab7",
    database="my_guitar_shop"
)
cursor = db.cursor()

class TestL2(unittest.TestCase):
    cursor = db.cursor()


    def test_root_route(self):
        response = requests.get(f"{PORT}/")
        expected_key = "message"
        expected_message = "Hello from the Cloud!"
        print(f"[ROOT] Expected: '{expected_key}': {expected_message}', Actual response: {response.json()}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["message"], expected_message)

    def test_greetings(self):
        response = requests.get(f"{PORT}/greetings?name=Alice&age=25")
        expected = "Greetings Alice, good to know you are 25 years old."
        print(f"[GREETINGS] Expected: '{expected}', Actual: '{response.text}'")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Greetings Alice", response.text)

    def test_salutations_path(self):
        response = requests.get(f"{PORT}/salutations/Bob/40")
        expected = "Salutations Bob, you are 40 years old."
        print(f"[SALUTATIONS] Expected: '{expected}', Actual: '{response.text}'")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Salutations Bob", response.text)

    def test_yoda_personclass(self):
        info1 = {"name": "Luke", "age": 21}
        response = requests.post(f"{PORT}/Yoda_personclass", json=info1)
        expected = "21 years you are, young Luke"
        print(f"[YODA] Expected: '{expected}', Actual: '{response.text}'")
        self.assertEqual(response.status_code, 200)
        self.assertIn(expected, response.text)

    def test_time(self):
        response = requests.get(f"{PORT}/time")
        print(f"[TIME] Expected key: 'time', Actual response: {response.json()}")
        self.assertEqual(response.status_code, 200)
        self.assertIn("time", response.json())

    def test_date(self):
        response = requests.get(f"{PORT}/date")
        print(f"[DATE] Expected key: 'date', Actual response: {response.json()}")
        self.assertEqual(response.status_code, 200)
        self.assertIn("date", response.json())

    def test_addition(self):
        response = requests.get(f"{PORT}/addition?int1=5&int2=7")
        expected_total = 12
        actual_total = response.json()["total"]
        print(f"[ADDITION] Expected total: {expected_total}, Actual total: {actual_total}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(actual_total, expected_total)

    def test_subtraction(self):
        response = requests.get(f"{PORT}/subtraction?int1=10&int2=4")
        expected_total = 6
        actual_total = response.json()["total"]
        print(f"[SUBTRACTION] Expected total: {expected_total}, Actual total: {actual_total}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(actual_total, expected_total)

    def test_arrow(self):
        info = {"range1": 100, "range2": 200}
        response = requests.post(f"{PORT}/Arrow", json=info)
        expected = "The arrow's range is 100 or 200 meters."
        print(f"[ARROW] Expected: '{expected}', Actual: '{response.text}'")
        self.assertEqual(response.status_code, 200)
        self.assertIn("range is 100 or 200 meters", response.text)

    def test_choice(self):
        info2 = {"c1": "cats", "c2": "dogs"}
        response = requests.post(f"{PORT}/Choice", json=info2)
        expected = "It is either cats or dogs."
        print(f"[CHOICE] Expected: '{expected}', Actual: '{response.text}'")
        self.assertEqual(response.status_code, 200)
        self.assertIn("It is either cats or dogs", response.text)

    def test_getHeaders(self):
        url = "http://localhost:8080/headers/"
        headers = {
            "Content-Type": "application/json",
            "Y-Custom-Header": "CustomValue",
            "user-email": "TTran",
            "my-val": "my-value"
        }

        response = requests.get(url=url, headers=headers)

        print("Status code: ", response.status_code)
        print("[HEADERS] Response body: ", response.json())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["user_email"], "TTran")
        self.assertEqual(response.json()["my_val"], "my-value")

    def test_read_cookie(self):
        cookies = {"username": "Anakin"}
        response = requests.get(f"{PORT}/readCookie", cookies=cookies)
        expected = {"username": "Anakin"}
        print(f"[COOKIE] Sent: {cookies}, Received: {response.json()}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), expected)


    def test_products(self):
        cursor.execute("SELECT * FROM products;")
        rows = cursor.fetchall()
        expected = 10
        actual = len(rows)
        print(f"[PRODUCTS] Expected {expected}, got {actual}")
        self.assertEqual(actual, expected)

    def test_categories(self):
        cursor.execute("SELECT * FROM categories;")
        rows = cursor.fetchall()
        expected = 4
        actual = len(rows)
        print(f"[CATEGORIES] Expected {expected}, got {actual}")
        self.assertEqual(actual, expected)

    def test_addresses_ca(self):
        cursor.execute("SELECT * FROM addresses WHERE state = 'CA';")
        rows = cursor.fetchall()
        expected = 5
        actual = len(rows)
        print(f"[ADDRESSES CA] Expected {expected}, got {actual}")
        self.assertEqual(actual, expected)

    def test_products_over_700(self):
        cursor.execute("SELECT product_name, list_price FROM products WHERE list_price > 700;")
        rows = cursor.fetchall()
        expected = 4
        actual = len(rows)
        print(f"[PRODUCTS > $700] Expected {expected}, got {actual}")
        self.assertEqual(actual, expected)

    def test_admin_emails(self):
        self.cursor.execute("SELECT email_address FROM administrators;")
        rows = self.cursor.fetchall()
        expected = 3
        actual = len(rows)
        print(f"[ADMIN EMAILS] Expected {expected}, got {actual}")
        self.assertEqual(actual, expected)

    def test_products_with_category(self):
        cursor.execute("""
                            SELECT products.product_name, categories.category_name
                            FROM products
                                     INNER JOIN categories ON products.category_id = categories.category_id;
                            """)
        rows = cursor.fetchall()
        expected = 10
        actual = len(rows)
        print(f"[PRODUCTS + CATEGORIES] Expected {expected}, got {actual}")
        self.assertEqual(actual, expected)

    def test_orders_with_customer_names(self):
        cursor.execute("""
                            SELECT orders.order_id, orders.order_date, customers.first_name, customers.last_name
                            FROM orders
                                     INNER JOIN customers ON orders.customer_id = customers.customer_id;
                            """)
        rows = cursor.fetchall()
        expected = 9
        actual = len(rows)
        print(f"[ORDERS + CUSTOMERS] Expected {expected}, got {actual}")
        self.assertEqual(actual, expected)

    def test_order_items_with_products(self):
        cursor.execute("""
                            SELECT order_items.order_id, products.product_name, order_items.quantity
                            FROM order_items
                                     INNER JOIN products ON order_items.product_id = products.product_id;
                            """)
        rows = cursor.fetchall()
        expected = 12
        actual = len(rows)
        print(f"[ORDER ITEMS + PRODUCTS] Expected {expected}, got {actual}")
        self.assertEqual(actual, expected)

    def test_orders_with_shipping_addresses(self):
        cursor.execute("""
                            SELECT orders.order_id, addresses.line1, addresses.city, addresses.state
                            FROM orders
                                     INNER JOIN addresses ON orders.ship_address_id = addresses.address_id;
                            """)
        rows = cursor.fetchall()
        expected = 9
        actual = len(rows)
        print(f"[ORDERS + ADDRESSES] Expected {expected}, got {actual}")
        self.assertEqual(actual, expected)

    def test_customer_order_totals(self):
        cursor.execute("""
                            SELECT customers.first_name,
                                   customers.last_name,
                                   orders.order_id,
                                   SUM(order_items.quantity) AS total_items
                            FROM customers
                                     INNER JOIN orders ON customers.customer_id = orders.customer_id
                                     INNER JOIN order_items ON orders.order_id = order_items.order_id
                            GROUP BY orders.order_id, customers.first_name, customers.last_name;
                            """)
        rows = cursor.fetchall()
        expected = 9
        actual = len(rows)
        print(f"[ORDER TOTALS] Expected {expected}, got {actual}")
        self.assertEqual(actual, expected)

    def test_address_count_by_state(self):
        cursor.execute("""
                            SELECT state, COUNT(*) AS num_addresses
                            FROM addresses
                            GROUP BY state;
                            """)
        rows = cursor.fetchall()
        expected = 6
        actual = len(rows)
        print(f"[ADDRESS COUNT BY STATE] Expected {expected}, got {actual}")
        self.assertEqual(actual, expected)

    def test_avg_price_per_category(self):
        cursor.execute("""
                            SELECT categories.category_name, AVG(products.list_price) AS avg_price
                            FROM products
                                     INNER JOIN categories ON products.category_id = categories.category_id
                            GROUP BY categories.category_name;
                            """)
        rows = cursor.fetchall()
        expected = 3
        actual = len(rows)
        print(f"[AVG PRICE PER CATEGORY] Expected {expected}, got {actual}")
        self.assertEqual(actual, expected)

    def test_order_count_by_customer(self):
        self.cursor.execute("""
                            SELECT customers.first_name, customers.last_name, COUNT(orders.order_id) AS num_orders
                            FROM customers
                                     INNER JOIN orders ON customers.customer_id = orders.customer_id
                            GROUP BY customers.customer_id;
                            """)
        rows = self.cursor.fetchall()
        expected = 7
        actual = len(rows)
        print(f"[ORDER COUNT BY CUSTOMER] Expected {expected}, got {actual}")
        self.assertEqual(actual, expected)

    def test_total_revenue_value(self):
        cursor.execute("""
                            SELECT SUM(item_price - discount_amount) AS total_revenue
                            FROM order_items;
                            """)
        row = cursor.fetchone()
        expected_row_count = 1
        expected_total_revenue = 6750.27

        actual_row_count = 1
        actual_total_revenue = float(row[0])

        print(f"[TOTAL REVENUE] Expected rows: {expected_row_count}, got: {actual_row_count}")
        print(f"[TOTAL REVENUE] Expected value: {expected_total_revenue}, got: {actual_total_revenue}")

        self.assertEqual(actual_row_count, expected_row_count)
        self.assertAlmostEqual(actual_total_revenue, expected_total_revenue, places=2)

    def test_orders_with_shipping_costs(self):
        cursor.execute("""
                            SELECT orders.order_id, customers.first_name, customers.last_name, orders.ship_amount
                            FROM orders
                                     INNER JOIN customers ON orders.customer_id = customers.customer_id;
                            """)
        rows = cursor.fetchall()
        expected = 9
        actual = len(rows)
        print(f"[ORDERS + SHIP AMOUNTS] Expected {expected}, got {actual}")
        self.assertEqual(actual, expected)

    def test_address_count_by_city(self):
        cursor.execute("""
                            SELECT city, COUNT(*) AS num_addresses
                            FROM addresses
                            GROUP BY city;
                            """)
        rows = cursor.fetchall()
        expected = 9
        actual = len(rows)
        print(f"[ADDRESS COUNT BY CITY] Expected {expected}, got {actual}")
        self.assertEqual(actual, expected)

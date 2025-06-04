import requests

PORT = "http://localhost:8080"


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
    print("13. Exit")


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


def main():
    while True:
        menu()
        choice = input("Enter route number: ")

        if choice == "1":
            call_root()
        elif choice == "2":
            call_greetings()
        elif choice == "7":
            call_addition()
        elif choice == "8":
            call_subtraction()
        elif choice == "13":
            print("Exiting CLI.")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
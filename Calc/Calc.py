def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Error: Division by zero is not allowed.")
    return a / b

def add_three(a, b, c):
    return a + b + c

def calculator():
    operations = {
        '1': ('+', add),
        '2': ('-', subtract),
        '3': ('*', multiply),
        '4': ('/', divide),
    }

    print("=" * 30)
    print("       Basic Calculator")
    print("=" * 30)

    while True:
        print("\nSelect an operation:")
        print("  1. Addition       (+)")
        print("  2. Subtraction    (-)")
        print("  3. Multiplication (*)")
        print("  4. Division       (/)")
        print("  5. Exit")
        print("  6. Add three numbers")
        print("-" * 30)

        choice = input("Enter choice (1/2/3/4/5/6): ").strip()

        if choice == '5':
            print("Goodbye!")
            break

        if choice not in operations and choice != '6':
            print("Invalid choice. Please select a valid option.")
            continue

        if choice == '6':
            try:
                a = float(input("Enter first number:  "))
                b = float(input("Enter second number: "))
                c = float(input("Enter third number: "))
            except ValueError:
                print("Invalid input. Please enter numeric values.")
                continue
            result = add_three(a, b, c)
            display_result = int(result) if result == int(result) else result
            print(f"\n  {a} + {b} + {c} = {display_result}")
            continue

        try:
            a = float(input("Enter first number:  "))
            b = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

        symbol, func = operations[choice]

        try:
            result = func(a, b)
            # Display as int if result is a whole number
            display_result = int(result) if result == int(result) else result
            print(f"\n  {a} {symbol} {b} = {display_result}")
        except ValueError as e:
            print(f"\n  {e}")

if __name__ == "__main__":
    calculator()
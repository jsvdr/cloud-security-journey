ALLOWED_OPERATORS = {"+", "-", "*", "/"}


def calculate(a: int, b: int, operator: str) -> int | float | str:
    """Return result or error string for allowlisted operator."""
    if operator == "+":
        return a + b
    if operator == "-":
        return a - b
    if operator == "*":
        return a * b
    if operator == "/":
        if b == 0:
            return "Cannot divide by zero"
        return a / b
    return "Invalid operator"


def main() -> None:
    """Read stdin, validate, print result. No secrets, no eval."""
    try:
        a = int(input("Enter a number: "))
        b = int(input("Enter a number: "))
    except ValueError:
        print("Must be an int")
        return
    
    operator = input("Enter a operator (e.g. + - * or /): ")
    if operator not in ALLOWED_OPERATORS:
        print("Invalid operator.")
        return

    print(calculate(a, b, operator))

if __name__ == "__main__":
    main()

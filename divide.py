import sys


def divide(a, b):
    if b == 0:
        print("Error: division by zero")
        sys.exit(1)
    return a / b


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <numerator> <denominator>")
        sys.exit(1)

    try:
        numerator = float(sys.argv[1])
        denominator = float(sys.argv[2])
    except ValueError:
        print("Error: both arguments must be numbers")
        sys.exit(1)

    result = divide(numerator, denominator)
    print(result)

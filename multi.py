import sys

def multiply(args):
    result = 1
    for num in args:
        result *= num
    return result

def main():
    if len(sys.argv) < 3:
        print("Usage: python multi.py <num1> <num2> [num3 ...]")
        sys.exit(1)
    numbers = [float(arg) for arg in sys.argv[1:]]
    print(multiply(numbers))

if __name__ == "__main__":
    main()

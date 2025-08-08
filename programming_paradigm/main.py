
#Take numerator and denominator from the command line and run the safe_divide function.

import sys
from robust_division_calculator import safe_divide

def main():
    # Check if exactly 2 extra arguments are given
    if len(sys.argv) != 3:
        print("Usage: python main.py <numerator> <denominator>")
        sys.exit(1)

    # Get numerator and denominator from the command line
    numerator = sys.argv[1]
    denominator = sys.argv[2]

    # Call our division function
    result = safe_divide(numerator, denominator)

    # Show the result or error message
    print(result)

if __name__ == "__main__":
    main()

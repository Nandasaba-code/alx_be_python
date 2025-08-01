# pattern_drawing.py

# Prompt user for pattern size
size = int(input("Enter the size of the pattern: "))

# Initialize row counter for while loop
row = 0

# Use while loop to handle rows
while row < size:
    # Use for loop to print asterisks on the same line
    for column in range(size):
        print("*", end="")
    # After each row, print a newline
    print()
    # Move to the next row
    row += 1

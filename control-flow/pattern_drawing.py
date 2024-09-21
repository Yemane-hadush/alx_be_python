# Prompt the user for the pattern size
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Use a while loop to draw the square pattern
while row < size:
    # Use a for loop to print asterisks on the same line
    for col in range(size):
        print("*", end="")
    # Move to the next line after each row
    print()
    # Increment the row counter
    row += 1

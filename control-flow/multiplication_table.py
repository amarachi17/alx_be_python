# Ask the user for a number
number = int(input("Enter a number to see its multiplication table: "))

# Generate the print and multiplication table
for i in range(1, 11):
    product = number * i
    print(f"{number} * {i} = {product}")
    
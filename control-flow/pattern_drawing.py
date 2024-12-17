# Drawing patterns with asterisks
size = int(input("Enter the size of the pattern: "))

# Using while loop to iterate through each row
row = 1
while row <= size:
    # Using a for loop to print asterisks side by side
    for _ in range(size):
        print("*", end="")
    print()
    row +=1


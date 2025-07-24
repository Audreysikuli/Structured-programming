# This program calculates the sum of all even numbers from 1 to n

# Step 1: Ask the user for a positive number
n = int(input("Enter a number: "))

# Step 2: Calculate the sum of even numbers using a loop
sum_even = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        sum_even += i

# Step 3: Display the result
print("Sum of even numbers:", sum_even)
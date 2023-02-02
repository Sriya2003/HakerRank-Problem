from collections import Counter

# Get the number of shoes and the list of shoe sizes
n_shoes = int(input())
shoe_sizes = list(map(int, input().split()))

# Count the occurrences of each shoe size
shoe_counts = Counter(shoe_sizes)

# Get the number of customers
n_customers = int(input())

# Initialize the total amount of money earned
total_money = 0

# Process each customer
for i in range(n_customers):
    # Get the desired shoe size and price
    size, price = map(int, input().split())
    # Check if the desired shoe size is available
    if shoe_counts[size] > 0:
        # Decrement the count of the shoe size
        shoe_counts[size] -= 1
        # Add the price of the shoe to the total amount of money earned
        total_money += price

# Print the total amount of money earned
print(total_money)

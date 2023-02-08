from collections import defaultdict

# Get the number of words in group A and group B
n, m = map(int, input().split())

# Create a defaultdict that stores the list of indices of each word in group A
groupA = defaultdict(list)

# Read the words in group A and store their indices
for i in range(n):
    word = input()
    groupA[word].append(i+1)

# Process each word in group B
for i in range(m):
    word = input()
    # Check if the word has appeared in group A
    if word in groupA:
        # Print the list of indices
        print(" ".join(map(str, groupA[word])))
    else:
        # Print -1
        print(-1)
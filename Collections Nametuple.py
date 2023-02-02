from collections import namedtuple

# Get the number of students
n = int(input())

# Get the column names
columns = input().split()

# Create a named tuple for the student's data
Student = namedtuple('Student', columns)

# Read the student's data and calculate the average marks
marks = [int(Student(*input().split()).MARKS) for _ in range(n)]
average = sum(marks) / n

# Print the average marks
print("{:.2f}".format(average))

n = int(input())
students = {}
for i in range(n):
    name, *marks = input().split()
    students[name] = list(map(float, marks))

query_name = input()
query_marks = students[query_name]
average = sum(query_marks) / len(query_marks)
print("{:.2f}".format(average))
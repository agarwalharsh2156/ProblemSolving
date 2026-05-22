# 1        1
# 12      21
# 123    321
# 1234  4321
# 1234554321

n = int(input("Number: "))

for i in range(1, n+1):
    spaces = (n - i)
    for j in range(1, i+1):
        print(j, end = "")
    print(" " * spaces, end = "")
    print(" " * spaces, end = "")
    for j in range(1, i+1):
        print(j, end = "")
    print()
1
12
123
1234
12345

n = int(input("Please enter the number of stairs you want in the pattern: "))
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end = "")
    print()


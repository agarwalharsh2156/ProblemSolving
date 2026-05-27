# Let's say for N = 5, the pattern should look like as below:

# 5 5 5 5 5 5 5 5 5 
# 5 4 4 4 4 4 4 4 5 
# 5 4 3 3 3 3 3 4 5 
# 5 4 3 2 2 2 3 4 5 
# 5 4 3 2 1 2 3 4 5 
# 5 4 3 2 2 2 3 4 5 
# 5 4 3 3 3 3 3 4 5 
# 5 4 4 4 4 4 4 4 5 
# 5 5 5 5 5 5 5 5 5

n = int(input("Number: "))
for i in range(n-1):
    last = 0
    for j in range(n, n-i-1, -1):
        print(str(j), end = " ")
        last = j
    a = last * 2 - 3
    print((str(last) + " " )* a, end= "")
    for j in range(n-i, n+1):
        print(str(j), end = " ")
    print()

mid = False
i = n
while(i <= n):
    print(i, end = " ")
    if i == 1 or mid == True:
        i += 1
        mid = True
    else:
        i -= 1

print()

for i in range(n-2, -1, -1):
    last = 0
    for j in range(n, n-i-1, -1):
        print(str(j), end = " ")
        last = j
    a = last * 2 - 3
    print((str(last) + " ") * a, end= "")
    for j in range(n-i, n+1):
        print(str(j), end = " ")
    print()
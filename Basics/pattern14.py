# A
# AB
# ABC
# ABCD
# ABCDE

n = int(input("Number:"))
for i in range(n):
    for j in range(65, 65+i + 1):
        print(chr(j), end= "")
    print()


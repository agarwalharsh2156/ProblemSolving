# A
# BB
# CCC
# DDDD
# EEEEE

n = int(input("Number: "))

for i in range(n):
    for j in range(0, i+1):
        print(chr(65+i), end = "")
    print()
# E 
# D E 
# C D E 
# B C D E 
# A B C D E


n = int(input("Number: "))
alph = 65 + n - 1
for i in range(n, 0, -1):
    for j in range((64 + i), alph + 1):
        print(chr(j), end = "")
    print()
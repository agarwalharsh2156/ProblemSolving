#     A
#    ABA
#   ABCBA
#  ABCDCBA
# ABCDEDCBA

n = int(input("Number:"))

for i in range(n):
    spaces = n - i - 1
    itr = 2 * i + 1
    a = 0
    j = 65
    mid = False
    print(" "*spaces, end = "")
    while a < itr:
        print(chr(j), end = "")
        if (j == 65 + i) or (mid == True):
            j -= 1
            mid = True
        else :
            j += 1
        a += 1
    print()        

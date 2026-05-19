#      *
#     ***
#    *****
#   *******
#  *********


n = int(input("Number of stairs you want: "))
for i in range(0,n):
    for j in range(0, n+i):
        if j > n - i:
            print("*", end = "")
        else:
            print(" ", end = "")
    print()    



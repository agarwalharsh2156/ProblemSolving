# *********
#  *******
#   *****
#    ***
#     *
# inverted triangle

n = int(input("No. of Stairs: "))
for i in range(n, 0, -1):
    for j in range(0, n + i):
        if j > (n-i):
            print("*", end = "")
        else:
            print(" ", end = "")
    print()
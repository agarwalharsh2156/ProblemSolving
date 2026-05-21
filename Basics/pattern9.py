#     * 
#    ***
#   *****
#  *******
# *********
# *********
#  *******
#   *****
#    ***
#     *


n = int(input("Number of stairs: "))
for i in range(0, n*2):
    if i < n:
        spaces = n - i - 1
        stars = 2 * i + 1
    else:
        spaces = i - n
        stars = 2 * (2 * n - i - 1) + 1
    
    print(" " * spaces + "*" * stars)
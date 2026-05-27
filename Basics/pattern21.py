# Given an integer n. You need to recreate the pattern given below for any value of N. 
# Let's say for N = 5, the pattern should look like as below:
# *****
# *   *
# *   *
# *   *
# *****

n = int(input("number: "))
spaces = n - 2
for i in range(n):
    if i == 0 or i == n-1:
        print("*" * n)
    else:
        print("*", " "* spaces, "*", sep = "")

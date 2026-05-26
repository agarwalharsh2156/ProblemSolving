# *        *
# **      **
# ***    ***
# ****  ****
# **********
# ****  ****
# ***    ***
# **      **
# *        *

n = int(input("Number: "))

for i in range(n):
    spaces = (n - i - 1)
    stars = n - spaces
    spaces *= 2
    print("*" * stars, " "* spaces, "*"*stars, sep = "")

for i in range(n-1):
    stars = n - i - 1
    spaces = (n - stars)*2
    print("*"* stars, " "* spaces, "*"* stars, sep = "")


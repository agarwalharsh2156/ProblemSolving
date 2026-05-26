# **********
# ****  ****
# ***    ***
# **      **
# *        *
# *        *
# **      **
# ***    ***
# ****  ****
# **********

n = int(input("Number: "))
spaces = 0

for i in range(n):
    stars = n - spaces//2 
    print("*" * stars, " "* spaces, "*" * stars, sep= "")
    spaces += 2
    
spaces = (n*2) - 2
for i in range(n):
    stars = n - spaces//2
    print("*" * stars, " "* spaces, "*" * stars, sep= "")
    spaces -= 2
   

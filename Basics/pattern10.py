# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *

n = int(input("Number of stairs: "))
i = 1
mid = False
while i > 0:
    print("*" * i)
    if i == n or mid == True:
        mid = True
        i -= 1
    else:
        i += 1
    
    
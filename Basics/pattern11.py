# 1 
# 0 1 
# 1 0 1 
# 0 1 0 1 
# 1 0 1 0 1


n = int(input("Number of stairs: "))
i = 0
string = ""
while i < n:
    if i % 2 == 0:
        string = "1" + string
        print(string)
    else:
        string = "0" + string
        print(string)
    i += 1
num = input() #passed and submitted
num = num.split(",")

m = num[0]
n = num[1]
f=int(num[0])
e=int(num[1])

items = []
for i in range(f, e+1):
    s = str(i)
    if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0) and (int(s[3])%2==0 ):
        items.append(s)
print( ",".join(items),end="")
    

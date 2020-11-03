i = 1 
  
lst = [int(i) for i in input().split()]
res = []

for j in lst:
  if j in res:
    continue
  else:
    res.append(j)
  

for k in res:
  if(res.index(k)==len(res)-1):
    print(k,end="")
  else:
    print (k,end = " ")

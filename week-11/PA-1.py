import math #third private case not passed
dnum = input()
dnum = dnum.split(",")
res=[]


for d in dnum:
  d = int(d)
  q = round(math.sqrt((2*50*d)/30))
  res.append(q)
  
for x in res:
  if(x==res[-1]):
    print(x,end="")
  else:
    print(x,end=",")

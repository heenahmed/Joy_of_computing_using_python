import math #passed and submitted
dnum = input()
dnum = dnum.split(",")
res=[]


for d in dnum:
  d = int(d)
  q = round(math.sqrt((2*50*d)/30))
  q=str(q)
  res.append(q)
  
print(",".join(res),end="")
    

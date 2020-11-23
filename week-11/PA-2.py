word = input() #passed and submitted
word = word.split(",")

res = []

for w in word:
  res.append(w)
  
x = sorted(res)
l = len(x)

for m in x:
  if(m==x[l-1]):
    print(m,end="")
  else:
    print(m,end=",")

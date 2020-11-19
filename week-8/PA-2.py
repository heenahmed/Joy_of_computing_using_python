inp = list(map(int,input().split())) 
n = len(inp)

for i in range(n):
  for j in range(0,n-i-1):
    if inp[j]==0:
      inp[j], inp[j+1] = inp [j+1], inp[j]
      
for i in range(n):
  if i == n-1:
    print(inp[i],end="")
  else:
    print(inp[i], end =" ")

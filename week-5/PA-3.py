def printDict():
  n = int(input())
  sq = {}
  for i in range(1,n+1):
    sq[i] = i*i
    
  print(sq , end="")
  
printDict()

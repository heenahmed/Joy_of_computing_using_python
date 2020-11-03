def powerTwo(n):
  if n==2:
    return True 
  elif (n%2 == 0):
    return powerTwo(n/2)
  elif (n%2 !=0):
    return False
  

n = int(input())
if(powerTwo(n)):
  print('YES',end="")
else:
  print('NO',end="")

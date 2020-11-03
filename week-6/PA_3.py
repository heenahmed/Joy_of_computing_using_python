size = int(input()) 

array_input = []

for x in range(size):
    array_input.append([int(y) for y in input().split()])
    
for i in range(size):
  for j in range(len(array_input[i])):
    if(j>i):
      array_input[i][j] = 0
      

    
for i in range(size) :  
    for j in range(len(array_input[i])) : 
      if(j==size-1):
        if(i==size-1 and j==size-1):
          print(array_input[i][j],end="")
        else:
          print(array_input[i][j]) 
      else:
        print(array_input[i][j],end=" ") 

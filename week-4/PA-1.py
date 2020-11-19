row , col = input().split()
row = int(row)
col = int(col)

matrix = []
num =1

for i in range(row):
  l = []
  for j in range(col):
    l.append(num)
    num = num + 1
  matrix.append(l)
    
    
for i in range (row):
  for j in range(col): 
    if(i==row-1 and j == col-1):
      print(matrix[i][j] , end = " ") 
    else:
      if(j== col-1):
        print(matrix[i][j])
      else:
        print(matrix[i][j] , end = " ")

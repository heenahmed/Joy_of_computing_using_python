def spiral(n,a):   # passed all pubic cases and passed all private cases
  r=0 #row start
  c=0 #col start
  m=n #col end
  n=n#row end
  
  while(r<n and c<m):
    for i in range(r,n):#first col
      if(r==n-1 and c==m-1):
        print(a[i][c],end="")
      else:
        print(a[i][c],end=" ")
    c += 1
    
    for i in range(c,m):
      print(a[n-1][i],end=" ")
    n -= 1
    
    for i in range(n-1, r-1, -1):
      print(a[i][m-1],end=" ")
    m -= 1
    
    for i in range(m-1 , c-1 , -1):
      print(a[r][i],end=" ") 
    r += 1
    
  

n = int(input())

matrix = [] 

for i in range(n):      
    x= input()
    x = [int(i) for i in x.split()] #creates a 1D array of integers from input string of numbers separated by space
    matrix.append(x) 
    
spiral(n,matrix)

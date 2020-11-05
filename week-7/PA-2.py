'''
Question:
Given a square matrix with n rows and n columns, you have to write a program to rotate this matrix such that each element is shifted by one place in a clockwise manner.
For example, given the following matrix

1 2 3
4 5 6
7 8 9

The output should be

4 1 2
7 5 3
8 9 6

Input Format:
The first line of the input contains a number n representing the number of rows and columns.
After this, there are n rows with each row containing n elements separated by a space

Output Format:
Print the elements of the modified matrix with each row in a new line and all the elements in each row is separated by a space.
'''


def rotate(n,a):  #passed all private and public test cases
  top = 0
  bottom =n-1
  
  left = 0
  right = n-1

  while left < right and top < bottom: 

    # Store the first element of next row, 
    # this element will replace first element of 
    # current row 
    prev = a[top+1][left] 

    # Move elements of top row one step right 
    for i in range(left, right+1): 
      curr = a[top][i] 
      a[top][i] = prev 
      prev = curr 

    top += 1

      # Move elements of rightmost column one step downwards 
    for i in range(top, bottom+1): 
      curr = a[i][right] 
      a[i][right] = prev
      prev = curr 

    right -= 1

        # Move elements of bottom row one step left 
    for i in range(right, left-1, -1):
      curr = a[bottom][i] 
      a[bottom][i] = prev 
      prev = curr 
    bottom -= 1

          # Move elements of leftmost column one step upwards 
    for i in range(bottom, top-1, -1): 
      
      curr = a[i][left] 
      a[i][left] = prev 
      prev = curr 

    left += 1
  
  for i in range(n):
    for j in range(n):
      if(j==n-1 and i==n-1):
        print(a[i][j],end="")
      elif(j==n-1):
        print(a[i][j])
      else:
        print(a[i][j],end=" ")
    
    
  

n = int(input())

matrix = [] 

for i in range(n):      
    x= input()
    x = [int(i) for i in x.split()] #creates a 1D array of integers from input string of numbers separated by space
    matrix.append(x) 
    
rotate(n,matrix)

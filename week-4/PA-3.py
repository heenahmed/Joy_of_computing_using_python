import random

n = int(input())
arr = []
for i in range(0,n):
  ele = int(input())
  arr.append(ele)
  
def isSorted(arr):
  flag = 1
  for i in range(0,len(arr)):
    if(i<len(arr)-1 and arr[i]>arr[i+1]):
       flag = 0
  return flag
       
def swap(arr,i,j):
  arr[i],arr[j] = arr[j],arr[i]
  return arr
     
list1 = list(range(0,n))
list2 =list(range(0,n))
while( isSorted(arr) != 1):
  i = random.randint(0,len(list1)-1)
  j = random.randint(0,len(list2)-1)
  if(i>j and arr[i] < arr[j]):
     arr = swap(arr,i,j)
  elif(j > i and arr[j] < arr[i]):
     arr = swap(arr,i,j)
       
for i in range(0,n):
  if(i != n-1):
     print(arr[i],end=" ")
  else:
     print(arr[i],end="")
       

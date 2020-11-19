start,end = input().split()
start = int(start)
end = int(end)
list_1 = []

for i in range(1,51):
  list_1.append(i)
  
list_2 = list_1[start:end]
n = len(list_2)

for j in range(0,n):
  if(j==n-1):
     print(list_2[j],end="")
  else:
     print(list_2[j])

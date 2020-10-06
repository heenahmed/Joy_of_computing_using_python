# divisibility
a = int(input())
count=0
list_1 = []

for i in range(1,51):
  list_1.append(i)

for num in list_1:
  if(num==a):
    continue
  else:
    if(num%a == 0):
      count = count +1


print(count,end="")

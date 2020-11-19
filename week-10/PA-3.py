num = input() #passed and submitted
num = num.split(" ")
modify = []

count = '0'

for i in range(len(num)):
  if count in num:
    modify.append(count)
  else:
    modify.append(-1)
  count = int(count)
  count += 1
  count = str(count)

for x in modify:
  if(x == modify[-1]):
     print(x,end="")
  else:
     print(x,end=" ")

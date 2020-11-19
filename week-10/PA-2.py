num = (input()) #third private test case not passed
num = num.split(" ")
num = sorted(num)


missnum = 0
count = 1

for n in num:
  n= int(n)
  if(n != count):
    missnum = count
    break
  count += 1

print(missnum,end="")

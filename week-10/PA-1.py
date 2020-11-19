num = list(input()) #passed and submitted
zero = 0
one = 0

for n in num:
  if n=='0':
    zero+=1
  else:
    one+=1
    
if(zero == 1 or one == 1):
  print('YES',end="")
else:
  print('NO',end="")

s = input() #second test case not passed
u=0
l=0
sp =  '`~!@#$%^&*()_-+=|\}]{[":;?/>.<,'
for i in s:
  #print('i is'+str(i))
  if(i == i.upper() and i != " " and i not in sp  and i !="'"):
    u+=1
    #print('u is '+str(u))
  elif(i !=" " and i not in sp and i !="'"):
    l+=1
    #print('l is '+str(l))
print(str(u)+' '+str(l),end="")

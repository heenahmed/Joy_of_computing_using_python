s = input() # passed and submitted
u=0
l=0

for i in s:
  if(i==i.upper() and i.isalpha()==True):
    u+=1
  elif(i==i.lower() and i.isalpha()==True):
    l+=1
  
print(str(u)+' '+str(l),end="")

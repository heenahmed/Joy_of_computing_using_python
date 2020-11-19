n = input()
s=0
for i in n:
    s+=int(i)
    
newsum = 0

while(int(s/10)!=0):
  s = str(s)
  for i in s:
    newsum+=int(i)
  s = newsum
    
print(s,end="")

word = input() #passed and submitted
flag = 0

for i in range(int(len(word)/2)):
  if(word[i] != word[len(word)-i-1]):
     flag = 1
  
if(flag == 1):
     print("NO",end="")
else:
     print("YES",end="")

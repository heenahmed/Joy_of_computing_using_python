count = 0 #passed and submitted
word = input()
li = list(word)

one = ['A','Q','R','O','P','D','A']
two = ["B"]
zero = ['W','E','T','Y','I','U','L','K','J','H','G','F','S','Z','X','C','V','N','M']

for i in li:
  if (i in one):
    count += 1
  elif (i in two):
    count += 2
  else :
    count += 0
 
print(count,end="")

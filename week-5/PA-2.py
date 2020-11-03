import math #third private case failed

n = int(input())

move = { 'x':0 , 'y':0 }

for i in range(n):
  ch = input()
  lch =len(ch)
  if (ch[0:1] == 'U'):
    move['y'] += int(ch[2:])

  elif(ch[0:1] == 'L'):
    move['x'] -= int(ch[4:])

  elif(ch[0:1] =='D'):
    move['y'] -= int(ch[4:])

  elif(ch[0:1] == 'R'):
    move['x'] += int(ch[5:])

    
x = move['x']
y = move['y']

dis = math.sqrt((x*x) + (y*y))
dis = int(round(dis))

print(dis,end='')

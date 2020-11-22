num = (input()) #passed and submitted
num = num.split(" ")
num = sorted(num)

n=len(num)
sum_of_A =0
total = (n + 1)*(n + 2)/2

for n in num:
  sum_of_A +=int(n)

print(int(total - sum_of_A),end="")


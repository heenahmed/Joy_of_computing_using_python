word = input() #passed and submitted
length = len(word)
def SmallestPalindrome(word, length):
  i = 0
  j = length - 1
  word = list(word)  #creating a list from the input word
  while (i <= j):  
    if (word[i] == word[j] == '.'):
      word[i] = word[j] = 'a'  
    elif (word[i] != word[j]):  
      if (word[i] == '.'):
        word[i] = word[j]
      elif (word[j] == '.'):
        word[j] = word[i]
      else:# worst case situation when palindrome condition is not met
        return -1
    i = i + 1  
    j = j - 1 
  return "".join(word)  # to turn the list back to a string
print(SmallestPalindrome(word, length),end="") #Print the output of your function

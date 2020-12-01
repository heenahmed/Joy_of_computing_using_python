email = input()#passed and submitted
email = email.rstrip('.com')
email = email.split("@")
print(email[1],end = '')

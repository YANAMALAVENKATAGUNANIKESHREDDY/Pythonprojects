import random

#A function do shuffle all the characters of a string
def shuffling(string):
  tempList = list(string)
  random.shuffle(tempList)
  return ''.join(tempList)

#Generate a random Uppercase letter (based on ASCII code)
uppercaseLetter1=chr(random.randint(65,90)) 
uppercaseLetter2=chr(random.randint(65,90))
lowercaseLetter1=chr(random.randint(92,127))
lowercaseLetter2=chr(random.randint(92,127))
symbol=chr(random.randint(33,64))
number1=random.randrange(100)
number2=random.randrange(10)


#Generate password using all the characters, in random order
password = uppercaseLetter1 + uppercaseLetter2 + lowercaseLetter1 + lowercaseLetter2 + str(number1) + str(number2)
password = shuffling(password)

#Ouput
print(password)
import string 
import random

#getting password length
length = int(input('Enter password length:'))

print('''Choose character set from these
        1. Digits
        2. Letters
        3. Special Characters
        4. Exit''')
characterList = '' #create an empty variable

#getting character set for password
while(True):
    choice = int(input('Pick a number'))
    if(choice == 1):
        characterList += string.ascii_letters
        #adding letters to possible Characters
    elif(choice == 2):
        #add digits to the password
        characterList += string.digits
    elif(choice == 3):
        #add special characters
        characterList += string.punctuation
    elif(choice == 4):
            break
    else:
            print('Please pick a valid option!')

password = []

for i in range(length):
    randomchar = random.choice(characterList)
    password.append(randomchar)
    
print('The random password is' + ''.join(password))
    
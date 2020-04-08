import re
strong=False
def function():
    password=input('Please enter the Password: ')
    lengthregex=re.compile(r'\w{8,}')
    smallregex=re.compile(r'[a-z]+')
    capsregex=re.compile(r'[A-Z]+')
    numregex=re.compile(r'\d{1,}')
    if lengthregex.findall(password)==[]:
        print('The password must have 8 characters')
    elif smallregex.findall(password)==[]:
        print('The password must contain a small letter')
    elif capsregex.findall(password)==[]:
        print('The password must contain a capital letter')
    elif numregex.findall(password)==[]:
        print('The password must contain a number')
    else:
        print('Strong password')
        global strong
        strong=True       
    return
while not strong:
    function()


    
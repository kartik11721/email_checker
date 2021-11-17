import re
#
email = input('Enter A Email : ')
pattern = re.compile(r'(^[a-zA-Z0-9_.!$&]+@[a-zA-Z]+\.[a-zA-Z]+$)')
check = pattern.search(email)

if check == None:
    print('invalid email')
else:
    print('valid email')

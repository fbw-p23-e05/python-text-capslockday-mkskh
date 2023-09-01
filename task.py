text = input('Enter string: ')

if text.isupper():
    print(text.lower().capitalize() + '!')
else:
    print(text)
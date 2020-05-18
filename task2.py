s = input('Enter phone number (10 digits):')
if s.isalnum() and s.isalpha() == False and len(s) == 10:
    print('valid phone number')
else:
    print('invalid number')

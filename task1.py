str = input('enter string:')
if len(str) >= 2:
    print(f'{str[0:2]} {str[-2:]}')
else:
    print('foo')

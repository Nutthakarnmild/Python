s = input('Enter number : ')

if s.isnumeric() :
    print('Your string is numeric. ')
    print('Mumeric value is %d' % int(s))
else:
    print('Your string is string. ')

print('1. Convert inches -> cm')
print('2. Convert cm -> inches')
selection = input('Make your selection (1,2): ')

if selection == '1':
    inches = int(input('Enter inches: '))
    print('Number of cm: ' + str(inches * 2.54))
elif selection == '2':
    cm = int(input('Enter cm: '))
    print('Number of inches: ' + str(cm / 2.54))
else:
    print('Invalid entry')

user_input = ''
while user_input is not int:
    try:
        user_input = int(input('Enter a number: '))
        break
    except ValueError:
        print('Please enter a valid number: ')

print('You entered {}'.format(user_input))
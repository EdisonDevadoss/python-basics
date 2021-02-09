birthdays = {'Edison': 'June 21', 'Gibson': 'Aug 12', 'Benny': 'Aug 12', 'Puspha': 'Dec 08'}

while True:
    print('Enter a name: (blank to quit)')
    name = input()
    if name == '':
        break

    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print('I do not have birthday information of ' + name)
        print('What is your birthday?')
        bday = input()
        birthdays[name] = bday
        print('Birthday database updated.')

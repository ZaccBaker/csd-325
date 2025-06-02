#Written by Zac Baker on 04/26/2025 for Module 7.2 Assignment

#Gets string of user's name
def name():
    name = input('Enter your full name '
                 '\nFormat: First, Middle, Last name\n\t').strip()
    return  name

#Gets user initials and determines seperator used
def initial(name):
    if ',' in name:
        return initialFormat(name, ',')
    elif '.' in name:
        return initialFormat(name, '.')
    elif ' ' in name:
        return initialFormat(name, ' ')

#Formats user initials
def initialFormat(name, seperator):
    initial = []

    for word in name.split(seperator):
        initial.append(word.strip()[0])

    initial = '.'.join(initial)
    return initial
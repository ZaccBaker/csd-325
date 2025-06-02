#Written by Zac Baker on 04/26/2025 for Module 7.2 Assignment

import user

#Main section of program
if __name__ == "__main__":
    name = user.name()
    initial = user.initial(name)

    print(f'\nInitials: {initial}')
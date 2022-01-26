import random
from termcolor import colored

print(colored("Welcome to Dan's Random Password Generator\n", 'green'))

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?.1234567890'
num_passwd = int(input("Enter The Number of Passwords to Generate (Integer): "))
lt_passwd = int(input("How many characters long should the passwords be: "))
print(colored('\nYour passwords are below:\n', 'green'))
pwlist = []
for pw in range(num_passwd):
    passwd = ''
    for C in range(lt_passwd):
        char = random.choice(chars)
        passwd += char
    pwlist += passwd
    print(passwd)
k=input(colored("\n\nPress Enter to exit", 'yellow'))
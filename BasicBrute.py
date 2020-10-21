#lol

#Brute-Force-Test


import string, itertools

password = input('Password:')

characters = string.printable

def iter_all_strings():
    length = 1
    while True:
        for s in itertools.product(characters, repeat=length):
            yield "".join(s)
        length +=1

for s in iter_all_strings():
    print(s)
    if s == password:
        print('Password is {}'.format(s))
        break

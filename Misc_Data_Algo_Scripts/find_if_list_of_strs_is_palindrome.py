list_of_strings = [
    'asddfdsfds',
    'aassddbbbbddssaa',
    'asddsa',
    'helloolleh'
]

#Edge cases (upper and lowercase)

def find_palindromes():
    for i in list_of_strings:
        if i == i[::-1]:
            print ( i + "  its a palind")

find_palindromes()

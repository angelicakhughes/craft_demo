
# Reverse a string

def reverse_string(string):
    reversedstring = ''
    for i in string:
        reversedstring = i + reversedstring


    if string == reversedstring:
        print('palindrome')
    else:
        print ('it is not')

    return reversedstring
print(reverse_string('Angelica'))

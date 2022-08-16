# Is every character unique in a string?

def is_unique_character(str):
    chars_seen = []
    for char in str:
        if char in chars_seen:
            return False
        chars_seen.append(char)
    return True

str='ansjhsshsk'

print(is_unique_character(str))

# Is a second string a permutation of another string? (first string)

def is_permutation(s1,s2):
    if len(s1) != len(s2):
        return False
    #sort the lists
    s1, s2 = sorted(s1), sorted(s2)

    for i in range(len(s1)):
        if s1[i] != s2[i]:
            return False
    return True

s1='godess'
s2='godsse'

print(is_permutation(s1,s2))

#replace spaces with %20

def replace_spaces(char_list):
    return char_list.replace(" ","%20")

char_list = "Hello My Name Is Jelly"

print(replace_spaces(char_list))

#determine if an input has been appended a single char, replaced a single char, or removed a single char

def one_edit(s1,s2):
    if len(s1) == len(s2):
        return "replaced"
    if len(s1) + 1 == len(s2):
        return "appeneded"
    if len(s1) -1 == len(s2):
        return "removed"
    return False

s1 = 'apple'
s2 = 'apples'

print(one_edit(s1,s2))



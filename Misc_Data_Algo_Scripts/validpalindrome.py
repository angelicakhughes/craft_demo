## ## https://leetcode.com/problems/valid-palindrome/

## talk about the steps like to a toddler
## remove all spaces, chars
## make everything lowercase
## use pencil / white board
## Is the newstring the same forward and back
## does the new string equal the new string reversed?

string = "A man, a plan, a canal: Panama"

def isPalindrome():
    newstring=''
    for i in string:
        if i.isalnum():
            # += "add on"
            # -= "subtract/take away"
            newstring+=i.lower()
    if newstring==newstring[::-1]:
        print "True"
    else:
        print "False"

isPalindrome()

#def is_palindrome:
#    newstring = string.replace( , )("")

#    if newstring = newstring[::-1]
#        then print ("True: This is a palendrome")
#    else
#        print ("False:Not a palindrome")

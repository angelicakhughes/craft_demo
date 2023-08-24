
##
## https://leetcode.com/problems/valid-anagram/
## talk about the steps like to a toddler
## What is an anagram?
## What is a palindrome?
## Think about length of the string
## Think about case sensitive
## Talk about counting, sorting (How can a computer help us here? Think programmatically)
## sorted()
## counter()


a = "anagram"
b = "nagaram"

def isAnagram():
    if(sorted(a)== sorted(b)):
        print ("True")
    else:
        print ("False")

isAnagram()

##Time Complexity: O(nlogn)
##Auxiliary Space: O(1)

#a = "anagram"
#b = "nagaram"

#def isAnagram():
#    if(Counter(a)== Counter(b)):
#        print ("True")
#    else:
#        print ("False")

#isAnagram()

##Time Complexity: O(n)
##Auxiliary Space: O(1)

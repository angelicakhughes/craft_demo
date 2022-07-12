#find dups in a list

def find_dups(list):
    newlist = []
    for i in list:
        if i not in newlist:
            newlist.append(i)
        else:
            print (i)

list = [1,1,4,5,656,66,77,77,8]

find_dups(list)

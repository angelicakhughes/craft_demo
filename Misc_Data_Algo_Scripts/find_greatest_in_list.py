#find greatest num in a list

def findgreatest (list):
    list.sort()   
# list[-1] is the last element/point in the list
    print("largest element is:", list[-1])

list = [1,5,7,84,2,54,7]

print (findgreatest(list))

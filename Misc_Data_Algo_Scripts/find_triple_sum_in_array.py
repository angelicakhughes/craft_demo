# Find three numbers that add up to the sum of 22 in the given array


def find3Numbers(A, arr_size, sum):
  
    # Sort the elements 
    A.sort()
  
    # Now fix the first element 
    # one by one and find the
    # other two elements 
    for i in range(0, arr_size-2):
        l = i + 1 
        r = arr_size-1 

        while (l < r):         
            if( A[i] + A[l] + A[r] == sum):
                print("Triplet is", A[i], A[l], A[r])
                return True             
            elif (A[i] + A[l] + A[r] < sum):
                l += 1
            else: 
                r -= 1
  
    # If we reach here, then
    # no triplet was found
    return False
  
# Driver program to test above function 
A = [1, 4, 45, 6, 10, 8]
sum = 22
arr_size = len(A)
  
find3Numbers(A, arr_size, sum)

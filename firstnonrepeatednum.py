#A program to get the first non repeated element in the list of integers:
#Initialize the list 
 
def firstNonRepeating(arr, n):
 
    # Loop for checking each element
    for i in range(n):
        j = 0
        # Checking if ith element is present in array
        while(j < n):
            if (i != j and arr[i] == arr[j]):
                break
            j += 1
        # if ith element is not present in array
        # except at ith index then return element
        if (j == n):
            return arr[i]
 
    return -1

arr = [1,2,3,2,43,34,33,3,1]
n = len(arr)
print(firstNonRepeating(arr, n))
 
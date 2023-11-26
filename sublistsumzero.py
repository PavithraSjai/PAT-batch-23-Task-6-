#A Program to return sum zero from given list 
def subArray(arr, l):
    #Outer loop from index 0 to l-1
    for i in range(l - 1):
        s = arr[i]
        #Inner loop from index i+1 to l
        for j in range(i + 1, l):
            s += arr[j]
            #If sum equals Zero then sub array exists so return true 
            if s == 0:
                return True
    #Else return false
    return False
#Initialising the list
array = [4, 2, -3, 1, 6]
print(subArray(array, len(array)))
    
# A program to Find total number for all triplets given in a set to get tota 59 
 
def findTriplets(list, k):
    triplet = 0
    final_temp_list =[]
     
    for i in range(0, len(list)-1): 
         
        s = set() 
        temp_list = []
 
        # Appending first element
        temp_list.append(list[i])
 
        curr_k = k - list[i] 
         
        for j in range(i + 1, len(list)): 
             
            if (curr_k - list[j]) in s: 
                triplet += 1
                 
                # Appending second element
                temp_list.append(list[j])
 
                # Appending third element
                temp_list.append(curr_k - list[j])
                 
                # Appending tuple to the final list
                final_temp_list.append(tuple(temp_list))
                temp_list.pop(2)
                temp_list.pop(1)
            s.add(list[j])
             
    return final_temp_list
     
list = [10,20,30,9]
k = 59
print(findTriplets(list, k))
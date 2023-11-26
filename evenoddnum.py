#A Program to find the even nubers and odd numbers in the given list [10,501,22,37,100,999,87,351]
#Initializing the list 
num = [10,501,22,37,100,999,87,351]
#Initialize two empty list 
even=[]
odd=[]
#Iterating through num list using for loop
for i in num:
    #if num reminder is zero once divided by 2 then its an even number 
    if (i%2 == 0):
        #Append the even value to even list
        even.append(i)    
    else:
        #Append the odd value to odd list 
        odd.append(i)
#Print the two seperate even and odd list numbers         
print("Even numbers :",even)
print("Odd numbers :",odd)

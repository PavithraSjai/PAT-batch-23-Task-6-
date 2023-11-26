#A program to find the duplicate in the given 3 list 
#Initialise 3 list 
a = [10,20,30]
b = [20,30,40]
c = [20,50,30]
#using intersection of set using & operator to get the duplicate value 
d=set(a)&set(b)&set(c)
#Print the duplicate value 
print("The duplicate values from a , b and c :",list(d))
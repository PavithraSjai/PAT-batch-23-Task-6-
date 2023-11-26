#A Program to take list of numbers and count all the prime numbers in it and create a new python list containing prime numbers alone
#Initializing the list 
num =[10,501,22,37,100,999,87,351]
primenum =[]
#Iterating through list 
for i in num :
    a=0
    for j in range(1,i):
        #Divide by itself and if reminder is zero then its not prime 
        if i%j ==0:
            a+=1
    #If a is incremented the append the i value to prime num list 
    if a==1:
        primenum.append(i)
#Print the prime numbers
print("Prime number list :",primenum)


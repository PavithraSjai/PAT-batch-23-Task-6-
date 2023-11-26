#Program to get the sum of first and last digit if given number 
#get the number input from user 
num= int(input("Enter the number: "))
#Converting the integer to string and restoring it in num
num = str(num)
#Using indexing to get the first and last digit of the number
firstdigit=int(num[0])
lastdigit=int(num[-1])
#adding bboth digits
sumofnum=firstdigit+lastdigit
#Printing the output of sum of first and last digit of given number
print("Sum of first and last digit :",sumofnum)
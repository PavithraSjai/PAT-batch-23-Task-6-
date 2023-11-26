#A program to find the happy number from the given list , given list [10,501,22,37,100,999,87,351]
#Initialize the list 
num = [10,501,22,37,100,999,87,351]
happynum = []
def is_happy(num):
    for i in range (len(num)):
        sum = num[i]
        while sum!=1 and sum !=4:
            tempsum = 0
            for digit in str(sum):
                tempsum += int(digit) ** 2   
            sum = tempsum
        if sum == 1:
            happynum.append(num[i])
    return happynum
print(is_happy(num))


    


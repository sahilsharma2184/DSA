n=int(input("Enter the number \n")) # n =123 as example case
num = n #don't change input, instead just make another variable and store it there
reverse = 0
while num > 0:
    last_digit = num % 10 #gives last digit
    reverse = (reverse * 10) + last_digit # 3 is extracted first => 0*10 + 3 = 3, next time 3*10+2 = 32, next time 32*10+1 = 321 == reverse
    num = num // 10 #updation of the number, if the input n = 123, in this step the it will be updated to 12, and after multiple updations num = 0, and the loop will exit
print("Reversed is",reverse)
print("Original input was",n)

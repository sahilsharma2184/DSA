n=int(input("Enter the number \n"))
num = n #don't change input, instead just make another variable and store it there
while num > 0:
    last_digit = num % 10 #gives last digit
    print(last_digit)
    num = num // 10 #updation of the number, if the input n = 123, in this step the it will be updated to 12, and after multiple updations num = 0, and the loop will exit
print("All the digits got printed \n")
print("Original input was",n)

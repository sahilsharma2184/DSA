n=int(input("Enter the number \n"))
num = n #don't change input, instead just make another variable and store it there
counter = 0
while num > 0:
    last_digit = num % 10 #gives last digit
    counter = counter+1
    num = num // 10 #updation of the number, if the input n = 123, in this step the it will be updated to 12, and after multiple updations num = 0, and the loop will exit
print("Number of digits are", counter)

"""
The time complexity here --->
Line 4: All the operations are performed inside the while loop
        Inside the loop the number is getting divided by 10
        So in anycase where division is done, so see that what is the divisor
        Whatever will be the divisor, according to that the TC will be calculated
        Here TC = O(log10 (n)) , where n is the number
        If the divisor is 2 let's say, then TC = O(log2 (n)) , where n is the number
"""
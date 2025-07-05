n = int(input("Enter the number \n"))
num = n
armstrong = 0
power = len(str(n))
while num>0:
    last_digit = num % 10
    armstrong = armstrong + (last_digit ** power)
    num = num // 10
print("Original Input is", n)
print("Conversion to armstrong gives", armstrong)
if armstrong == n:
    print("Input given is armstrong number")
else:
    print("Input given is not armstrong number")

"""
TC = O(log10 (n)), where n is number. Refer to Count_Digits.py comment
SC = O(1)
"""
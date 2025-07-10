#Type Conversion is done automatically by the python interpretor
#Type casting is done manually where the user itself does the conversion explicitly

#TYPE CONVERSION
print("TYPE CONVERSION")
a=1
b=1.5
sum =a+b #here the int is converted to float => 1 -> 1.0 since float is superior ==> 1.0+1.5=2.5
print(sum)
print(sum, ", Type of sum = ", type(sum)) #2.5 , Type of sum =  <class 'float'>

print("---------------")

#TYPE CASTING
print("TYPE CASTING")
x="2"
y=4.87
add = int(x) + y
print(add, ", Type of add = ", type(add)) #6.87 , Type of add =  <class 'float'>

s=str('2.54')
print("Type of s = ", type(s)) #<class 'str'>


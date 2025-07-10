a=2
b=1
print("Values of a and b before any computation", a,",",b)
a,b = b,a
print("Normal method", a,",",b)

a=2
b=1
a = a+b #2+1=3
b = a-b #3-1=2, hence b got a's value
a = a-b #3-2=1, hence a got b's value
print("Addition, Subtraction Method", a,",",b)

a=2 #Binary = 10
b=1 #Binary = 01
a = a^b # 10^01 = 11(since both the bits are different) => 3 in decimal
"""
10
01
--
11
"""
b = a^b # 11^01 = 10(since the last bit is same '1') => 2 in decimal, here the value of a is swapped with b
"""
11
01
--
10
"""
a = a^b # 11^10 = 01(since the first bit is same '1') => 1 in decimal, here the value of b is swapped with a
"""
11
10
--
01
"""
print("XOR Method", a,",",b)


list_num = [5,6,7,7,1,9,1,11,5,1,11,1]
dict_num = {}

key_having_value=[]

x=1
for i in range(0, len(list_num)): #TC:- O(N)
    if list_num[i] in dict_num: #incase the key is already present, then update the value.
        dict_num[list_num[i]] +=1 #TC:- O(1)
    else: #incase the key is not present then add the key in dictionary and update it's value as 1
        dict_num[list_num[i]] = 1 #TC:- O(1)
print(dict_num) #prints entire dictionary
print(dict_num[x]) #prints the value / occurence of x i.e. 1

"""
For above code the TC = O(N), where N is the number of items in list
SC = O(N) if every key is unique
"""

for key, value in dict_num.items(): #finding the key which has a certain value
    if value is 2:
        key_having_value.append(key)
print(key_having_value)
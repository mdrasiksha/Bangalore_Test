num = [1,4,6,43,78,9,54,11,9]
#adding value in end of the list
num.append(12)
print(num)

#counting the value in list
print(num.count(9))

#extending the list
num2 = [45,32,21]
num.extend(num2)
print(num)

#indexing the list
print(num.index(32))

#inserting the list
num.insert(1,100)
print(num)

#remove from the list by index
num.pop(2)
print(num)

#remove form the list by value
num.remove(100)
print(num)

#reverse the list
num.reverse()
print(num)

#sort function, acending order
num.sort()
print(num)
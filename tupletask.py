
# you can refer tuples by use of indexing 

thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

# Negative indexing means you start from the end

thistuple = ("apple","banana","cherry")
print(thistuple[-1])

# difference between list and a tuple is that a tuple is immutable or cannot be added or changed
#while a list is mmutable or can be changed
list1=[1,2,3,4]
tuple1=(1,2,3,4)
list1.append(5)
print(list1)

# Range in tuples
thistuple = ("apple","banana","cherry","kiwi","melon","soap")
print(thistuple[2:5])


# I have learnt that in range the index of the tuple or list is always left out 
# for example thistuple =("apple","banana","cherry","kiwi","melon","soap")
#if you happen to print the tuple using this code print(thistuple[:2])
#when you run the python code you`ll notice that the range starts from 0 index to 1 the 2 index is ignored
# this is a tuple range`
thistuple = ("apple","banana","cherry","kiwi","melon","soap")
print(thistuple[:2])
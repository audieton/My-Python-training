#  change tuple value a tuple cannot be changed or removed in other words immutable
# But they is a workaround a tuple can be changed into a list and 
# the list can be changed back into a tuple


x = ("apples","banana","cherry")
y = list(x)
y[1] ="kiwi"
x = tuple(y)



print(x)

# Add Item

thistuple= ("apple","banana","cherry")
y =list(thistuple)
y.append("orange")
thistuple = tuple(y)















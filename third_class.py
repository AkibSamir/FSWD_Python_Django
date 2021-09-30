# Set
# declaration
data_set = set()
print(type(data_set))
data_set2 = {1, 2, 3, 4, 5}
print(data_set2, type(data_set2))

# access item
# print(data_set2[1])
# Python set does not maintain indexing that's why we can't able to access any item

# update item 
# data_set2.update(9) # typeerror: int object is not iterable
# print(data_set2)
data_set3 = {"apple", "mango", "orange"}
print(data_set3)
data_set3.add("pineapple")    # it takes only one item otherwise it gives an typeerror message that set.add() takes exactly one argument (2 given)
print(data_set3)
data_set3.update("guava", "ginger")
print(data_set3)

data_set3.remove("v")
print(data_set3)

data_set3.discard("r")
print(data_set3)

data_set3.pop()
print(data_set3)

data_set3.clear()
print(data_set3)

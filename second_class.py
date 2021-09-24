# Loop
# While loop
print("While loop: ")
i = 0
while i <= 10:
    print(i, end=" ")
    i += 1
print()

i = 0
while i <= 100:
    if i % 2 == 0:
        print(i, end=" ")
    else:
        pass
    i += 1
print()    
# For loop
print("For loop: ")
for i in range(10):
    print(i)

for i in range(1, 20):
    if i % 2 == 0:
        print(i)
    else:
        pass

# Collection (List, Tuple)
print("List: ")
num_list = [1, 2, 3, 4, 5, 6, 7]
print(num_list, type(num_list))

fruits_list = ["apple", "orange", "pineapple", "mango"]
print(fruits_list, type(fruits_list))

mixed_list = [10, 20, 50.5, "apple", True]
print(mixed_list, type(mixed_list))

num_list.append(9)
print("After appending: ", num_list)

num_list.insert(2, 12)
print("After inserting: ", num_list)

num_list.extend([90, 80, 70, 50, 30])
print("After extending: ",num_list)

num_list.sort()
print("After sorting: ", num_list)

num_list.reverse()
print("After reversing: ", num_list)

num_list.pop()
print("After pop: ", num_list)

counting = num_list.count(2)
print("Count: ", counting)

num_list.clear()
print("After clear: ", num_list)

# Tuple
t1 = ()
print(type(t1))

t2 = (1, 2, 3, 4, 5, 6, 3)
print(t2)

counting = t2.count(3)
print(counting)

indexing = t2.index(3)
print(indexing)

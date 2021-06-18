array = [1, 2, 4]
print("array:")
print(array)
# index(number) gibt den index von einer
# Zahl zurück falls diese Zahl in der List
# steht. Diese Funktion gilt lieder nur
# ein dimensional array
print("array[4]:")
print(array.index(4))
# reverse a list and return no type
array.reverse()
print("Reversed array:")
print(array)
array = [[1, 3, 6], [9, 0, 65], [1, 3, 6]]
print("array:")
print(array)
array.reverse()
print("Reversed array:")
print(array)
# zählt wie oft ein Element
# (in unserem Fall repräsentiert ein Element
# eine Liste hier) in einer
# Liste befindet und die Anzahl zurück.
print("Number of occurences of ", end=" ")
print(array[0], end="")
print(":")
print(array.count(array[0]))
print("array:")
array = 3*[3*[[1, 34, 76]]]
print(array)


def isCountainsList(list0):
    if type(list0[0]) == list:
        return True


value = isCountainsList(array)

print(value)
isCountainsList(array)

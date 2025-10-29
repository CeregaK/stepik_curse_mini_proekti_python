# Найдите общие элементы списков.

lst1 = [1, 2, 3, 2, 0]
lst2 = [5, 1, 2, 7, 3, 2]
lst3 =[]

for i in lst1:
    for k in lst2:
        if i == k and i not in lst3:
            lst3.append(i)
            break

lst3.sort()
print(*lst3)

#----------------множества---------------

lst1 = [1, 2, 3, 2, 0]
lst2 = [5, 1, 2, 7, 3, 2]

lst3 = set(lst1) & set(lst2)
print(*sorted(lst3))
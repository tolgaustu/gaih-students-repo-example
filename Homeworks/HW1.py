list1 = []
list2 = []

for i in range(10):
    if i % 2:
        list1.append(i)
    else:
        list2.append(i)

print(list1)
print(list2)
mergedList = list1 + list2
mergedList.sort()
for i in mergedList:
    mergedList[i] = i * 2
    print("{}. index: {}".format(i, type(mergedList[i])))

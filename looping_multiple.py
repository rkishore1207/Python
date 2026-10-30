list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]

length1 = len(list1)
length2 = len(list2)

if length1 != length2:
    print("Both the lists are not in same length")
else:
    # for i in range(0, length1):
    #     print("%s is %s" % (list1[i], list2[i]))
    for i, j in zip(list1, list2):
        print("%s is %s" % (i, j))
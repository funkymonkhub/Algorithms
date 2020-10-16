def Sequential_Search(items, item):

    pos = 0
    flag = False
    while pos < len(items) and not flag:
        if items[pos] == item:
            flag = True
        else:
            pos = pos + 1
    
    return flag, pos
print(Sequential_Search([8,4,5,21,5,9,32,23,6,9],55))
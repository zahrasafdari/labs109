def count_dominators(items):
    count=0
    bool=[]
    for i in range(0,len(items)):
        for itm in items[i+1:]:
            if items[i]>itm:
                bool.append(True)
            else:
                bool.append(False)
                break
        if all(bool)==True:
            count+=1
        bool.clear()
    return count




# searching for an item in an ordered list adopted form LinkedIn Learning
# this technique uses a binary search
import time
now= time.time()
items = [6, 8, 19, 20, 23, 41, 49, 53, 56, 87]

def binarysearch(item, itemlist):
    # get the list size
    listsize = len(itemlist) - 1
    # start at the two ends of the list
    lowerIdx = 0
    upperIdx = listsize
    if lowerIdx== item or upperIdx== item: # TODO : when that if statement is put here it makes the program faster. 
        return str(item),str(now)          # TODO : because before the edit the index finders are not looking for themselves 
    while lowerIdx <= upperIdx:
        # calculate the middle point
        midPt = (lowerIdx + upperIdx)// 2

        # if item is found, return the index
        if itemlist[midPt] == item:
             return str(midPt),str(now) 
        # otherwise get the next midpoint
        if item > itemlist[midPt]:
            lowerIdx = midPt + 1
        else:
            upperIdx = midPt - 1

    if lowerIdx > upperIdx:
        return None


print(binarysearch(23, items))
print(binarysearch(87, items))
print(binarysearch(250, items))

numlist1 = [1,2,23,21]
numlist2 = [2,33,125]
numlist3 = numlist1 + numlist2
# numlist3 = list(dict.fromkeys(numlist3))
# numlist3.sort()
# print(numlist3)

def minElement(numlist,x):
    if(numlist):
        if(numlist[0]<x):
            return False
        else:
            return minElement(numlist[1:],x)
    else:
        return True

print(minElement(numlist3,1))
#Advent of Code day 2
fname = 'AoC2.txt'  #input data
inData = []
with open(fname) as f:
    for line in f:
        repList = []
        for v in line.split():
            repList.append(int(v))
        inData.append(repList)


def isSafe(repLst):
    #check unique
    if len(set(repLst)) != len(repLst):
        return False
    #check sorted
    if sorted(repLst) != repLst and sorted(repLst, reverse=True) != repLst:
        return False
    #check each increment is less than 4
    for i in range(1, len(repLst)):
        if abs(repLst[i] - repLst[i-1]) > 3:
            return False
    return True
    

#Part 1
p1safe_cnt = 0
for rep in inData:
    if isSafe(rep):
        p1safe_cnt += 1
        
print(p1safe_cnt) #411


#Part 2
p2safe_cnt = 0
for rep in inData:
    if isSafe(rep):
        p2safe_cnt += 1
    else:
        for i in range(len(rep)):
            tmpLst = rep[:]
            del tmpLst[i]
            if isSafe(tmpLst):
                p2safe_cnt += 1
                break

print(p2safe_cnt) #465

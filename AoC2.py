#Advent of Code day 1
fname = 'AoC2.txt'  #input data
inData = []
with open(fname) as f:
    for line in f:
        repList = []
        for v in line.split():
            repList.append(int(v))
        inData.append(repList)
        
#Part 1
p1safe_cnt = 0
for rep in inData:
    unsafe = 0
    #check unique
    if len(set(rep)) != len(rep):
        continue
    #check sorted
    if sorted(rep) != rep and sorted(rep, reverse=True) != rep:
        continue
    #check each increment is less than 4
    for i in range(1, len(rep)):
        if abs(rep[i] - rep[i-1]) > 3:
            unsafe += 1
            break
    if not unsafe:
        p1safe_cnt += 1
        
        
print(p1safe_cnt) #411

#Part 2
p2safe_cnt = 0
for rep in inData:
    remFlag = 0
    unsafe = 0
    #check unique
    unqDif = len(rep) - len(set(rep))
    if unqDif > 1:  #too many to remove
        continue
    elif unqDif == 1:   #check the rest with a removed val
        rep = list(set(rep))
        remFlag += 1
        
        
        
    #working from here    
    #check sorted
    if sorted(rep) != rep and sorted(rep, reverse=True) != rep:
        continue
    #check each increment is less than 4
    for i in range(1, len(rep)):
        if abs(rep[i] - rep[i-1]) > 3:
            unsafe += 1
            break
    if not unsafe:
        p1safe_cnt += 1

print(p2safe_cnt) #481 too high

import re

#Advent of Code day 2
def calcRes(inStr):
    rgx = re.compile(r'mul\(\d+,\d+\)')
    mLst = rgx.findall(inStr)
    res = 0
    n = re.compile(r'\d+')
    for m in mLst:
        vals = n.findall(m)
        res += int(vals[0]) * int(vals[1])
    return res


fname = 'AoC3.txt'  #input data
inData = ''
with open(fname) as f:
    inData = f.read().replace('\n', ' ')

#Part 1
print(calcRes(inData))   #174103751

#Part 2
r_rem = re.compile(r'(don\'t\(\)).*?(do\(\))')
p2Data = re.sub(r_rem, '', inData)     #this would need a little help if the data ended after a 'don't()' statement without any succeeding 'do()' statement; not the case in my data though

print(calcRes(p2Data)) #100411201

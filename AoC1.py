#Advent of Code day 1
from collections import Counter     #only used in part 2

fname = 'AoC1.txt'  #input data
col1 = []
col2 = []
with open(fname) as f:
    for line in f:
        line = line.split()
        col1.append(int(line[0]))
        col2.append(int(line[1]))

#Part 1
s_col1 = sorted(col1)   #using new arrays to maintain original lists for part 2
s_col2 = sorted(col2)

p1_res = 0
for i in range(0, len(s_col1)):
    p1_res += abs(s_col1[i] - s_col2[i])

print(p1_res)    #936063

#Part 2
col2_cnt = Counter(col2)
p2_res = 0
for v in col1:
    p2_res += v * col2_cnt[v]

print(p2_res)   #23150395

import re

#Advent of Code day 4
fname = 'AoC4.txt'  #input data
inData = ''
with open(fname) as f:
    inData = f.read()#.replace('\n', '.')

#Part 1
res1 = 0
hf_rgx = re.compile(r'XMAS')
hr_rgx = re.compile(r'SAMX')
vf_rgx = re.compile(r'(?=(X.{140}M.{140}A.{140}S))', re.DOTALL)
vr_rgx = re.compile(r'(?=(S.{140}A.{140}M.{140}X))', re.DOTALL)
drf_rgx = re.compile(r'(?=(X.{141}M.{141}A.{141}S))', re.DOTALL)   #diagnol right forward \
drr_rgx = re.compile(r'(?=(S.{141}A.{141}M.{141}X))', re.DOTALL)   #diagnol right reverse \
dlf_rgx = re.compile(r'(?=(X.{139}M.{139}A.{139}S))', re.DOTALL)   #diagnol left reverse /
dlr_rgx = re.compile(r'(?=(S.{139}A.{139}M.{139}X))', re.DOTALL)   #diagnol left reverse /

#horizontal fwd & rev
res1 += len(hf_rgx.findall(inData))
res1 += len(hr_rgx.findall(inData))
#vertical fwd & rev
res1 += len(vf_rgx.findall(inData))
res1 += len(vr_rgx.findall(inData))
#horizontal right fwd & rev \
res1 += len(drf_rgx.findall(inData))
res1 += len(drr_rgx.findall(inData))
#horizontal left fwd & rev /
res1 += len(dlf_rgx.findall(inData))
res1 += len(dlr_rgx.findall(inData))

print(res1)  #2599

#Part 2
res2 = 0
mm_ss = re.compile(r'(?=(M.M.{139}A.{139}S.S))', re.DOTALL)
ms_ms = re.compile(r'(?=(M.S.{139}A.{139}M.S))', re.DOTALL)
sm_sm = re.compile(r'(?=(S.M.{139}A.{139}S.M))', re.DOTALL)
ss_mm = re.compile(r'(?=(S.S.{139}A.{139}M.M))', re.DOTALL)

res2 += len(mm_ss.findall(inData))
res2 += len(ms_ms.findall(inData))
res2 += len(sm_sm.findall(inData))
res2 += len(ss_mm.findall(inData))

print(res2) #1948

import re

#Advent of Code day 4
fname = 'AoC4.txt'  #input data
inData = ''
with open(fname) as f:
    inData = f.read()#.replace('\n', '.')

#Part 1
res = 0
hf_rgx = re.compile(r'XMAS')
hr_rgx = re.compile(r'SAMX')
vf_rgx = re.compile(r'(?=(X.{140}M.{140}A.{140}S))', re.DOTALL)
vr_rgx = re.compile(r'(?=(S.{140}A.{140}M.{140}X))', re.DOTALL)
drf_rgx = re.compile(r'(?=(X.{141}M.{141}A.{141}S))', re.DOTALL)   #diagnol right forward \
drr_rgx = re.compile(r'(?=(S.{141}A.{141}M.{141}X))', re.DOTALL)   #diagnol right reverse \
dlf_rgx = re.compile(r'(?=(X.{139}M.{139}A.{139}S))', re.DOTALL)   #diagnol left reverse /
dlr_rgx = re.compile(r'(?=(S.{139}A.{139}M.{139}X))', re.DOTALL)   #diagnol left reverse /

#horizontal fwd & rev
res += len(hf_rgx.findall(inData))
res += len(hr_rgx.findall(inData))
#vertical fwd & rev
res += len(vf_rgx.findall(inData))
res += len(vr_rgx.findall(inData))
#horizontal right fwd & rev \
res += len(drf_rgx.findall(inData))
res += len(drr_rgx.findall(inData))
#horizontal left fwd & rev /
res += len(dlf_rgx.findall(inData))
res += len(dlr_rgx.findall(inData))

print(res)  #2599

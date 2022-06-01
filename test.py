# import math
# k_partitions=int(input())
# R=12
# peaks=[]
# for i in range(k_partitions):
#     peaks.append(round(R*math.cos(math.radians((i+1)*360/k_partitions)),3))
#     peaks.append(round(R*math.sin(math.radians((i+1)*360/k_partitions)),3))
# print(peaks[:(k_partitions)])
p=[11.413,3.708,9.708,7.053,7.053,9.708,3.708,11.413,0.0,12.0,-3.708,11.413,-7.053,9.708,-9.708,7.053,-11.413,3.708,-12.0,0.0,-4,-12,6,-12]
for i in range(len(p)):
    p[i]*=2
    print(p[i],end=',')
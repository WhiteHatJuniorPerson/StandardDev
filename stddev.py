import csv
import statistics as stat
f  = open("data.csv")
csvobj = csv.reader(f)
data = list(csvobj)
nums = data[0]
finaldata = []
for i in range(0,len(nums)):
    finaldata.append(int(nums[i]))
std = stat.stdev(finaldata)
print(std)
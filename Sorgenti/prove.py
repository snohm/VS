#import pandas as pd

f = open("/workspace/VS/DataSet/Carbon dioxide (CO2) Emissions.csv", "r")
line = f.readline()
stati = []
prev = ""
i = 0
while line != "":
    elments = line.split(",")
    if elments[0] == prev:
        line = f.readline()
        continue
    stati.append(elments[0])
    prev = elments[0]
    line = f.readline()
f.close()
#print(stati)

f = open("/workspace/VS/DataSet/Life expectancy at birth.csv", "r")
line = f.readline()
data = []
while line != "":
    elments = line.split(",")
    if elments[0] in stati:
        #print(type(elments[2]))
        if elments[2] == "Both sexes":
            statesData = [elments[1], elments[0], elments[3]]
            print(statesData)
            data.append(statesData)
    line = f.readline()
f.close()
print(data)

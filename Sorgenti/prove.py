import matplotlib.pyplot as plt
import pandas as pd

f = open("/workspace/VS/DataSet/Carbon dioxide (CO2) Emissions.csv", "r")
line = f.readline()
stati = []
while line != "":
    elments = line.split(",")
    if elments[0] not in stati:
        stati.append(elments[0])
    line = f.readline()
f.close()

f = open("/workspace/VS/DataSet/Life expectancy at birth.csv", "r")
line = f.readline()
nations = []
while line != "":
    elments = line.split(",")
    if elments[0] in stati and elments[2] == "Both sexes":    
        if elments[0] not in nations:
            nations.append(elments[0])
    line = f.readline()
f.close()

years = []
for i in range (1990, 2021, 1): 
    years.append(i)
f = open("/workspace/VS/DataSet/Carbon dioxide (CO2) Emissions.csv", "r")
prev = ""
val = []
i=0
label = ""
line = f.readline()
elments = line.split(",")
while line != "" :
    #prev = elments[0] 
    #input()
    if elments[0] in nations:
       # print(line)
        #print(elments[0])
        if elments[0] == "Australia":
            i = 30
        else:
            i = 31    
        for j in range (0, 31, 1):
        #while prev == elments[0]:   
            val.append(int(float(elments[2])/1000))
            #print(elments[1])
            label = elments[0]
            line = f.readline()
            elments = line.split(",")
        #print(len(years))
        #print(len(val))
        plt.plot(years, val, label = label)
        val = []
        #i=i+1
    else:
        line = f.readline()
        elments = line.split(",")    
f.close()
#print(i)
plt.axes()
plt.legend()
plt.show() 

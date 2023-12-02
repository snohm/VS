import pandas as pd
import seaborn as sns

f = open("/workspace/VS/DataSet/Carbon dioxide (CO2) Emissions.csv", "r")
line = f.readline()
stati = []
while line != "":
    elments = line.split(",")
    if elments[0] not in stati:
        stati.append(elments[0])
    line = f.readline()
f.close()
#print(stati)

f = open("/workspace/VS/DataSet/Life expectancy at birth.csv", "r")
line = f.readline()
nations = []
y1990 = []
y2000 = []
y2012 = []
prev = ""
while line != "":
    elments = line.split(",")
    if elments[0] in stati and elments[2] == "Both sexes":    
        if elments[0] not in nations:
            nations.append(elments[0])
        match elments[1]:
            case "1990":
                y1990.append(int(elments[3]))
            case "2000":
                y2000.append(int(elments[3]))
            case "2012":
                y2012.append(int(elments[3]))
    line = f.readline()
f.close()

print(len(stati))
print(y1990)
print(y2000)
print(y2012)
print(len(y2000))
print(len(nations))


df = pd.DataFrame({'1990': y1990, '2000': y2000, '2012': y2012}, index = nations )
ax = df.plot.barh()
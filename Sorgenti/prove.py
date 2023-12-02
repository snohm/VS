import matplotlib.pyplot as plt

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
line = f.readline()
elments = line.split(",")
while line != "":
    prev = elments[0]
    if elments[0] in nations:
        while elments[0] == prev:
            val.append(int(float(elments[2])/1000))
            prev = elments[0]
            line = f.readline()
            elments = line.split(",")
        plt.plot(years, val, label = elments[0])
        val = []
        i=i+1
    else:
        line = f.readline()
        elments = line.split(",")
f.close()
print(i)
plt.legend()
plt.show() # BUG: manca australia
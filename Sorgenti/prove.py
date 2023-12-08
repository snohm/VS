import matplotlib.pyplot as plt

f = open("/workspace/VS/DataSet/StatesOfEurope", "r")
line = f.readline()
europe = []
while line != "":
    europe.append(line[:len(line)-1])
    line = f.readline()
f.close()

f = open("/workspace/VS/DataSet/StatesOfAfrica", "r")
line = f.readline()
africa = []
while line != "":
    africa.append(line[:len(line)-1])
    line = f.readline()
f.close()

f = open("/workspace/VS/DataSet/Life expectancy at birth.csv", "r")
line = f.readline()
stati = []
while line != "":
    elments = line.split(",")
    if elments[0] not in stati:
        stati.append(elments[0])
    line = f.readline()
f.close()

fGdp = open("/workspace/VS/DataSet/GDP pro capita.csv", "r")
fLe = open("/workspace/VS/DataSet/LifeExpGrosso.csv", "r")
graphColor = "#f0f0f0"
plt.figure(facecolor = graphColor)
plt.axes(facecolor = graphColor)
lGdp = fGdp.readline()
elemGdp = lGdp.split(",")
lLe = fLe.readline()
elemLe = lLe.split(",")
while lGdp != "" and lLe != "":
    #print(elemLe[1] + " 2021 " + elemLe[0])
    if elemLe[1] == "2021" and elemLe[0] in stati:
        #print("a")
        while True:
            if elemGdp[1] == "2021" and elemLe[0] == elemGdp[0] :
                #print("c")
                break
            lGdp = fGdp.readline()
            elemGdp = lGdp.split(",")
            #print("b")
        # selezione colore e se e quali label mettere a legenda, suddiviso per aspettativa di vita
        #if  int(float(elemLe[3])) < 50:
        #    plt.scatter(int(float(elemLe[3])), int(float(elemGdp[3])), label = elemGdp[0], color = "#f03b20")
        #elif  50 <= int(float(elemLe[3])) < 60:
        #    plt.scatter(int(float(elemLe[3])), int(float(elemGdp[3])), label = elemGdp[0], color = "#fe9929")
        #elif  60 <= int(float(elemLe[3])) < 70:
        #    plt.scatter(int(float(elemLe[3])), int(float(elemGdp[3])), label = elemGdp[0], color = "#d9f0a3")
        #elif  70 <= int(float(elemLe[3])) < 80:
        #    plt.scatter(int(float(elemLe[3])), int(float(elemGdp[3])), label = elemGdp[0], color = "#78c679")
        #elif  80 <= int(float(elemLe[3])):
        #    plt.scatter(int(float(elemLe[3])), int(float(elemGdp[3])), label = elemGdp[0], color = "#006837")
        #
        #print("d")
        if elemLe[0] in europe:
            plt.scatter(int(float(elemLe[3])), int(float(elemGdp[3])), color = 'blue')
        elif elemLe[0] in africa:
            plt.scatter(int(float(elemLe[3])), int(float(elemGdp[3])), color = 'green')
        else:
            plt.scatter(int(float(elemLe[3])), int(float(elemGdp[3])), color = 'gray')
        lLe = fLe.readline()
        elemle = lLe.split(",")
        #print(lLe)
    else:
        lLe = fLe.readline()
        elemLe = lLe.split(",")
        #print("e")
fGdp.close()
fLe.close() 

plt.legend(ncol = 3, bbox_to_anchor=(1.02, 1), loc='upper left', facecolor = graphColor)
plt.title("Life expectancy Vs GDP (2021)")
plt.xlabel("years", loc='right')
plt.ylabel("GDP pro capita", rotation='horizontal', loc = 'top')
plt.show()
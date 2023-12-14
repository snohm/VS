# 0 - 21 -> CAR, 22 - 43 -> Chad, 44 - 65 -> Nigeria, 66 - 87 -> South Sudan
def CoutnCasesPercentage():
    fM = open("/workspace/VS/DataSet/MalariaAfricaCases.csv", "r")
    fH = open("/workspace/VS/DataSet/HivAfricaCases.csv", "r")
    fT = open("/workspace/VS/DataSet/TuberculosiAfricaCases.csv", "r")
    fP = open("/workspace/VS/DataSet/AfricanPopulation.csv", "r")
    val = []
    for i in range(0, 4, 1):
        LM = fM.readline()
        LH = fH.readline()
        elemM = LM.split(",")
        elemH = LH.split(",")
        if elemH[0] == "Nigeria":
            for j in range(1, len(elemH), 1):
                LT = fT.readline()
                elemT = LT.split(",")
                valT = elemT[2].split(" ")
                LP = fP.readline()
                elemP = LP.split(",")
                valP = int(float(elemP[2])*10)
                valM = elemM[j].split("[")
                val.append(int((int(valM[0]) + int(valT[0]))/valP))
        elif elemH[0] == "South Sudan":
            k = 0
            for j in range(1, len(elemH), 1):
                if k < 11:    
                    LT = fT.readline()
                    elemT = LT.split(",")
                    valT = elemT[2].split(" ")
                    LP = fP.readline()
                    elemP = LP.split(",")
                    valP = int(float(elemP[2])*10)
                    valM = elemM[j].split("[")
                    valH = elemH[j].split("[")
                    val.append(int((int(valH[0]) + int(valM[0]) + int(valT[0]))/valP))
                else:
                    LP = fP.readline()
                    elemP = LP.split(",")
                    valP = int(float(elemP[2])*10)
                    valM = elemM[j].split("[")
                    valH = elemH[j].split("[")
                    val.append(int((int(valH[0]) + int(valM[0]))/valP))
                k = k + 1         
        else:
            for j in range(1, len(elemH), 1):
                LT = fT.readline()
                elemT = LT.split(",")
                valT = elemT[2].split(" ")
                LP = fP.readline()
                elemP = LP.split(",")
                valP = int(float(elemP[2])*10)
                valM = elemM[j].split("[")
                valH = elemH[j].split("[")
                val.append(int((int(valH[0]) + int(valM[0]) + int(valT[0]))/valP))
    fM.close()
    fH.close()
    fT.close()
    fP.close()
    return val
# 0 - 21 -> CAR, 22 - 43 -> Chad, 44 - 65 -> Nigeria, 66 - 87 -> South Sudan
def CoutnDeathPercentage():
    fM = open("/workspace/VS/DataSet/MalariaAfrica.csv", "r")
    fH = open("/workspace/VS/DataSet/HivAfrica.csv", "r")
    fT = open("/workspace/VS/DataSet/TuberculosiAfrica.csv", "r")
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
                val.append(int(elemM[j]) + int(valT[0]))
        elif elemH[0] == "South Sudan":
            k = 0
            for j in range(1, len(elemH), 1):
                if k < 11:    
                    LT = fT.readline()
                    elemT = LT.split(",")
                    valT = elemT[2].split(" ")
                    val.append(int(elemH[j]) + int(elemM[j]) + int(valT[0]))
                else:
                    val.append(int(elemH[j]) + int(elemM[j]))
                k = k + 1         
        else:
            for j in range(1, len(elemH), 1):
                LT = fT.readline()
                elemT = LT.split(",")
                valT = elemT[2].split(" ")
                val.append(int(elemH[j]) + int(elemM[j]) + int(valT[0]))
        #print(elemH[0])
        #print(val)
        #val = []
    fM.close()
    fH.close()
    fT.close()
    fP.close()
    return val
CoutnDeath()    
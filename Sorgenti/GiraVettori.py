def rotate(vett):
    mirroredVett = []
    for i in range(len(vett)-1, -1, -1):
        mirroredVett.append(vett[i])
    return mirroredVett


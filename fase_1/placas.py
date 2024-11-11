# pontuação: 100/100

placa = input()

t1 = False
t2 = False

if len(placa) == 8:
    t1 = True
    for i in range(8):
        if i <= 2 and (ord(placa[i]) > 90 or ord(placa[i]) < 65):
            t1 = False
            break
        elif i == 3 and placa[i] != "-":
            t1 = False
            break
        elif i > 3 and i <= 7 and (ord(placa[i]) > 57 or ord(placa[i]) < 48):
            t1 = False
            break

elif len(placa) == 7:
    t2 = True

    for i in range(7):
        if i < 3 and (ord(placa[i]) > 90 or ord(placa[i]) < 65):
            t2 = False
            break
        elif i == 3 and (ord(placa[i]) > 57 or ord(placa[i]) < 48):
            t2 = False
            break
        elif i == 4 and (ord(placa[i]) > 90 or ord(placa[i]) < 65):
            t2 = False
            break
        elif  i > 4 and i < 7 and (ord(placa[i]) > 57 or ord(placa[i]) < 48):
            t2 = False
            break

if t1 == True:
    print(1)
elif t2 == True:
    print(2)
else:
    print(0)
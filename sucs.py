# Programa para Clasificación de suelos mediante SUCS.

gravas, arenas, finos = 29, 67, 4
gruesos = gravas + arenas
pesoMuestra = gravas + arenas + finos
cu, cc = 3.4, 2.6
ll, lp = 52, 24
ip = ll - lp
pi = 0.73 * (ll - 20)
sueloOrganico = True 

if (gruesos / pesoMuestra) > 0.5:
    if (gravas / gruesos) > 0.5:
        if (finos / pesoMuestra) < 0.05:
            if (cu > 4 and cc > 1 and cc < 3):
                print("GW")
            else:
                print("GP")
        elif (finos / pesoMuestra) < 0.12:
            print("Caso de doble Frontera")
        else:
            if ip < pi or ip < 4:
                print("GM")
            elif ip > pi and ip > 4 and ip < 7:
                print("GM-GC")
            elif ip > pi and ip > 7:
                print("GC")
            else:
                print("Error, checar datos de entrada")
    else:
        if (finos / pesoMuestra) < 0.05:
            if (cu > 4 and cc > 1 and cc < 3):
                print("SW")
            else:
                print("SP")
        elif (finos / pesoMuestra) < 0.12:
            print("Caso de doble Frontera")
        else:
            if ip < pi or ip < 4:
                print("SM")
            elif ip > pi and ip > 4 and ip < 7:
                print("SM-SC")
            elif ip > pi and ip > 7:
                print("SC")
            else:
                print("Error, checar datos de entrada")
else:
    if ll < 50:
        if ip < pi or ip < 4:
                if sueloOrganico == True:
                    print("OL")
                else:
                    print("ML")
        elif ip > pi and ip > 4 and ip < 7:
            print("ML-CL")
        elif ip > pi and ip > 7:
            print("CL")
        else:
            print("Error, checar datos de entrada")
    else:
        if ip < pi:
            if sueloOrganico == True:
                    print("OH")
            else:
                print("MH")
        else:
            print("CH")

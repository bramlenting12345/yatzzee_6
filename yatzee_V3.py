
import random
import os 

dobbelstenen_op_tafel=[]
hand = []

# =====================================[-class display-]================================

class player:
    def __init__(dis,naam,rondes,enen,tween,drieen,vieren,vijven,zessen):
        dis.naam   = naam
        dis.rondes = rondes 
        dis.enen   = enen
        dis.tweeen = tween
        dis.drieen = drieen
        dis.vieren = vieren
        dis.vijven = vijven
        dis.zessen = zessen
        
# ======================================[-display yatzee kaart-]================================

    def display(dis):  
        print("=========================[-invul kaart-]=========================================")
        print("naam van de speler " + str(dis.naam) + "ronde  " + str(dis.rondes))
        print("enen   |" + str(dis.enen )) 
        print("tweeen |" + str(dis.tweeen))
        print("drieen |" + str(dis.drieen))
        print("vieren |" + str(dis.vieren))
        print("vijven |" + str(dis.vijven))
        print("zessen |" + str(dis.zessen))
        print("===============================================================")

# ========================================[-eerste worp dobbel stenen -]===================================

def eerste_worp():
    for i in range(0,5):
        dobbelstenen_op_tafel.append(random.randint(1,6))
    print(dobbelstenen_op_tafel)    

#==========================================[-tweede worp dobbel stenen-]====================================
def tweede_worp():
    for i in range(0,5):
        vraag_dobbelstenen=input("wilt u dobbelsteen " + str(i + 1) + "opnieuw gooien : ? ")
        if vraag_dobbelstenen == "j":
            dobbelstenen_op_tafel[i] = random.randint(1,6)


    print (dobbelstenen_op_tafel)        
        




def restart_spel():
    global p1
    p1 = player(0,1,0,0,0,0,0,0)


# ===============================================[-aanroep-]=================================    

restart_spel()
p1.display()
eerste_worp()

tweede_worp()

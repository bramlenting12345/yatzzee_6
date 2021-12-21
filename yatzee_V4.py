
import random
import os 
import time

#=====================================[-list-]========================================

dobbelstenen_op_tafel=[]
hand = []

#======================================[-variable-]====================================
beurt = 0 
rondes = 1 
dobbelsteen = 0 



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
        print("naam van de speler " + str(dis.naam) + "ronde  " + str(rondes))
        print("enen   |" + str(dis.enen )) 
        print("tweeen |" + str(dis.tweeen))
        print("drieen |" + str(dis.drieen))
        print("vieren |" + str(dis.vieren))
        print("vijven |" + str(dis.vijven))
        print("zessen |" + str(dis.zessen))
        print("===============================================================")
        time.sleep(4)
        os.system("cls")

# ========================================[-eerste worp dobbel stenen -]===================================

def eerste_worp():
    print("===============================[-gerolde dobbelstenen-]=========================================")
    
    for i in range(0,5):
        dobbelstenen_op_tafel.append(random.randint(1,6))
    print(dobbelstenen_op_tafel)  

    print("===============================================================================================")  

#==========================================[-tweede worp dobbel stenen-]====================================

def tweede_worp():
   
    for i in range(0,5):
        vraag_dobbelstenen=input("wilt u dobbelsteen " + str(i + 1) + " opnieuw gooien (j / n) ?  " )
        
        if vraag_dobbelstenen == "j":
            dobbelstenen_op_tafel[i] = random.randint(1,6)
            
    print(dobbelstenen_op_tafel)
    ronde_check()
    

#==========================================[-ronde check-]===============================================

def ronde_check():                                       # | check beurt een beurt betaat uit 3 keer gooien 
    global rondes                                        # | een ronde bestaat uit een gooi van 5 dobbelstenen 
    rondes = rondes + 1                                  # | als er 3 keer is gegooid moet je daar cominatie mee maken            
    print("ronde nummer " + str(rondes))

    if rondes <= 3:
        print(str(rondes)) 
        tweede_worp()

    else:
        punten_aantal_boven()                  

# ==========================================[-vul formelier in-]============================
def punten_aantal_boven():                                                  # | voorbeeld 
    p1.display()

# ==========================================[-retsart spel-]=================================        

def restart_spel():                                # | deze fuctie geef de class een variable 
    global p1                                      # | en geeft de cordinaten een waarde
    p1 = player(0,1,0,0,0,0,0,0)


# ==========================================[-aanroep-]=======================================   

restart_spel()
p1.naam = input ("wat is u naam : ? ")
p1.display()
eerste_worp()
tweede_worp()
# =============================================================================================

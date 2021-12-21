
import random
import os 
import time

# =====================================[-list-]========================================

dobbelstenen_op_tafel=[]
hand = []



# ======================================[-variable-]====================================
beurt = 0 
rondes = 1 
dobbelsteen = 0 



# =====================================[-class display-]================================

class player:
    def __init__(dis,naam,rondes,enen,tween,drieen,vieren,vijven,zessen,three_of_a_kind,four_of_a_kind,kleine_straat,grote_straat,yatzee):
        dis.naam   = naam
        dis.rondes = rondes 
        dis.enen   = enen
        dis.tweeen = tween
        dis.drieen = drieen
        dis.vieren = vieren
        dis.vijven = vijven
        dis.zessen = zessen

        dis.three_of_a_kind = three_of_a_kind
        dis.four_of_a_kind = four_of_a_kind
        dis.kleine_straat = kleine_straat
        dis.grote_straat = grote_straat
        dis.yazee = yatzee
        
# ======================================[-display yatzee kaart-]======================================

    def display(dis):  
        print("=========================[-invul kaart-]===============================================")
        print("naam van de speler " + str(dis.naam) + "ronde  " + str(rondes))
        print("enen   |" + str(dis.enen ) + "   |    |    |    |    |") 
        print("tweeen |" + str(dis.tweeen) +"   |    |    |    |    |")
        print("drieen |" + str(dis.drieen) +"   |    |    |    |    |")
        print("vieren |" + str(dis.vieren)+ "   |    |    |    |    |")
        print("vijven |" + str(dis.vijven) +"   |    |    |    |    |")
        print("zessen |" + str(dis.zessen) +"   |    |    |    |    |")
        print("========================================================================================")
        print("three of a kind |"+str(dis.three_of_a_kind)+"   |    |    |    |    |")
        print("four of a kind  |"+str(dis.four_of_a_kind)+ "   |    |    |    |    |")
        print("kleine straat   |"+str(dis.kleine_straat)+  "   |    |    |    |    |")
        print("grote straat    |"+str(dis.grote_straat)+   "   |    |    |    |    |")
        print("yazee           |"+str(dis.yazee)+  "   |    |    |    |    |")        
        print("===========================================================================================")
        time.sleep(4)
        os.system("cls")

# ========================================[-eerste worp dobbel stenen-]====================================

def eerste_worp():
    print("==============================[-gerolde dobbelstenen-]==========================================")
    
    for i in range(0,5):
        dobbelstenen_op_tafel.append(random.randint(1,6))
    print("ronde nummmer  " + str(rondes))    
    print(dobbelstenen_op_tafel)  
 
    print("================================================================================================")  

# ==========================================[-tweede worp dobbel stenen-]==================================

def tweede_worp():
    global rondes
    for i in range(0,5):
        vraag_dobbelstenen=input("wilt u dobbelsteen " + str(i + 1) + " opnieuw gooien (j / n) ?  " )
        
        if vraag_dobbelstenen == "j":
            dobbelstenen_op_tafel[i] = random.randint(1,6)

    rondes = rondes + 1                                  # | als er 3 keer is gegooid moet je daar cominatie mee maken   |         
    print("ronde nummer : " + str(rondes))           
    print(dobbelstenen_op_tafel)
    ronde_check()
    

# ==========================================[-ronde check-]===============================================

def ronde_check():                 
    if rondes < 3:
        tweede_worp()

    else:
        punten()
    
# ==========================================[-retsart spel-]==============================================      

def restart_spel():                                # | deze fuctie geef de class een waarde.
    global p1                                      # | en geeft de cordinaten een waarde.
    p1 = player(0,1,0,0,0,0,0,0,0,0,0,0,0)



# ==========================================[-telling gegooiden punten -]===================================
def punten():
    p1.display
    x1 = dobbelstenen_op_tafel.count(1)
    print("aantal gegooide enen zijn    : " + str(x1))
    x2 = dobbelstenen_op_tafel.count(2)
    print("aantal gegooide tweeen zijn  : " + str(x2))
    x3 = dobbelstenen_op_tafel.count(3)
    print("aantal gegooiden drieen zijn : " + str(x3))
    x4 = dobbelstenen_op_tafel.count(4)
    print("aantal gegooiden vieren zijn : " + str(x4))
    x5 = dobbelstenen_op_tafel.count(5)
    print("aantal gegooide vijven zijn  : " + str(x5))
    x6 =dobbelstenen_op_tafel.count(6)
    print("aantal gegooide zessen zijn  : " + str(x6))

        


# ==========================================[-aanroep-]====================================================   
restart_spel()
p1.naam = input ("wat is u naam : ? ")
p1.display()
eerste_worp()
tweede_worp()
# =========================================================================================================
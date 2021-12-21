
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

def delete():
    global dobbelstenen_op_tafel
    print(len(dobbelstenen_op_tafel))
    print(dobbelstenen_op_tafel)
    if len(dobbelstenen_op_tafel) > 0 :
        for i in range(4,-1,-1):
            print(dobbelstenen_op_tafel)

            print(i)
            dobbelstenen_op_tafel.pop(i)

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
        
        eerste_worp()
        tweede_worp()
        keuzen_maken()    
    
    # enen toevoegen aan diplay 
    def enen_toevoegen(dis):
        dis.enen = dobbelstenen_op_tafel.count(1)
        p1.display()

    # tweeen toevegen aan diplay 
    def tweeen_toevoegen(dis):
        dis.tweeen = dobbelstenen_op_tafel.count(2) *2
        p1.display()

    # drieen toevoegen display 
    def drieen_toevoegen(dis):
        dis.drieen = dobbelstenen_op_tafel.count(3) *3
        p1.display()

    # vieren toevoegen aan diplay 
    def vieren_toevoegen(dis):
        dis.vieren = dobbelstenen_op_tafel.count(4) * 4
        p1.display()   

    # vijven toevoegen aan display
    def vijven_toevoegen(dis):
        dis.vijven = dobbelstenen_op_tafel.count(5) * 5
        p1.display()  

    # zessen toevegen aan display      
    def zessen_toevoegen(dis):
        dis.zessen = dobbelstenen_op_tafel.count(6) * 6
        p1.display()
        
                   

# ========================================[-eerste worp dobbel stenen-]====================================

def eerste_worp():
    print("==============================[-gerolde dobbelstenen-]==========================================")
    global rondes,dobbelstenen_op_tafel
    
    
    rondes = 1  
    
    delete()
    for i in range(0,5):
       
        dobbelstenen_op_tafel.append (random.randint(1,6))
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



# ==========================================[-telling gegooiden punten-]===================================
def punten():
    global y,x
    p1.display
    for x in range(1,7):
        y = dobbelstenen_op_tafel.count(x)
        if y > 0:
            print("aantal " + str(x) + " : " + str(y))
   
    

# ==========================================[-invullen punten-]===========================================
def keuzen_maken():
    # enen tellen 
    if dobbelstenen_op_tafel.count(1)>0:
        print("kies 1 om : " + str(dobbelstenen_op_tafel.count(1)) + " enen toe te voegen ")
    # tweeen tellen     
    if dobbelstenen_op_tafel.count(2)>0:
        print("kies 2 om : " + str(dobbelstenen_op_tafel.count(2)) + " tweeen toe te voegen " )   
    # drieen tellen 
    if dobbelstenen_op_tafel.count(3)>0:
        print("kies 3 om : " + str(dobbelstenen_op_tafel.count(3)) + " drieen toe te voegen ")
    # vieren tellen 
    if dobbelstenen_op_tafel.count(4)>0:
        print("kies 4 om : " + str(dobbelstenen_op_tafel.count(4))+ " vieren toe te voegen ")
    # vijven tellen    
    if dobbelstenen_op_tafel.count(5)>0:
        print("kies 5 om : " + str(dobbelstenen_op_tafel.count(5)) + " vijven toe te voegen")  
    # zessen toevoegen
    if dobbelstenen_op_tafel.count(6)>0:
        print("kies 6 om : " + str(dobbelstenen_op_tafel.count(6)) + " zessen toe te voegen ")

#========================================================================================================
    # enen invullen 
    vraag_keuze = input("wat wilt u toe voegen ")
    if vraag_keuze ==  "1":
        p1.enen_toevoegen()
    # tweeen invullen
    if vraag_keuze == "2":
        p1.tweeen_toevoegen()    
    # drieen invullen 
    if vraag_keuze =="3":
        p1.drieen_toevoegen()
    # vieren in vullen 
    if vraag_keuze == "4":
        p1.vieren_toevoegen()
    # vijven invullen 
    if vraag_keuze == "5":
        p1.vijven_toevoegen
    # zeesen invullen 
    if vraag_keuze == "6":
        p1.zessen_toevoegen





# ==========================================[-aanroep-]====================================================   
restart_spel()
p1.naam = input ("wat is u naam : ? ")
p1.display()
#eerste_worp()
#tweede_worp()
#keuzen_maken()
# =========================================================================================================
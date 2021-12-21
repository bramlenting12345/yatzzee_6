
import random
import os 
import time


# =====================================[-list-]==========================================================

dobbelstenen_op_tafel=[0,0,0,0,0]
hand = []
aantallen = [0,0,0,0,0,0]




# ======================================[-variable-]=====================================================
beurt = 0 
rondes = 1 
dobbelsteen = 0 

# =====================================[-class display-]=================================================

class player:
    def __init__(dis,naam,rondes,enen,tween,drieen,vieren,vijven,zessen,ful_house,three_of_a_kind,four_of_a_kind,kleine_straat,grote_straat,yatzee):
        dis.naam   = naam
        dis.rondes = rondes 
        dis.enen   = enen
        dis.tweeen = tween
        dis.drieen = drieen
        dis.vieren = vieren
        dis.vijven = vijven
        dis.zessen = zessen

        dis.ful_house = ful_house
        dis.three_of_a_kind = three_of_a_kind
        dis.four_of_a_kind = four_of_a_kind
        dis.kleine_straat = kleine_straat
        dis.grote_straat = grote_straat
        dis.yatzee = yatzee
        
# ======================================[-display yatzee kaart-]=========================================

    def display(dis):  
        print("=========================[-invul kaart-]==================================================")
        print("naam van de speler " + str(dis.naam) + "ronde  " + str(rondes))
        print("enen   |" + str(dis.enen ) + "   |    |    |    |    |") 
        print("tweeen |" + str(dis.tweeen) +"   |    |    |    |    |")
        print("drieen |" + str(dis.drieen) +"   |    |    |    |    |")
        print("vieren |" + str(dis.vieren)+ "   |    |    |    |    |")
        print("vijven |" + str(dis.vijven) +"   |    |    |    |    |")
        print("zessen |" + str(dis.zessen) +"   |    |    |    |    |")
        print("===========================================================================================")
        print("ful house       |"+str(dis.ful_house)+"   |    |    |    |    |")
        print("three of a kind |"+str(dis.three_of_a_kind)+"   |    |    |    |    |")
        print("four of a kind  |"+str(dis.four_of_a_kind)+ "   |    |    |    |    |")
        print("kleine straat   |"+str(dis.kleine_straat)+  "   |    |    |    |    |")
        print("grote straat    |"+str(dis.grote_straat)+   "   |    |    |    |    |")
        print("yazee           |"+str(dis.yatzee)+  "   |    |    |    |    |")        
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

    # three of a kind  toevoegen aan display 
    def three_of_kind(dis):
        for i in range(1,7):
            if dobbelstenen_op_tafel.count(i) == 3:
                dis.three_of_a_kind = i * 3
        p1.display()
    
    # four of a kind toevoegen aan display 
    def four_of_kind(dis): 
        for x in range(1,7):
            if dobbelstenen_op_tafel.count(x) == 4:
                dis.four_of_a_kind = x * 4
        p1.display()  

    # yatzee toevoegen aan display
    def yatzeee(dis):
        for y in range(1,7):
            if dobbelstenen_op_tafel.count(y) == 5:
                dis.yatzee = 50   
        p1.display()              
    
    # ful house toevoegen aan display 
    def ful_housee(dis):
        for h in range(1,7):
            if dobbelstenen_op_tafel.count(h) == 3 and dobbelstenen_op_tafel.count(h) == 2:
                dis.ful_house = 25
        p1.display()        

    # grote straat toevoegen aan display 
    def grote_straatt(dis):
        for g in range(1,7):
            if dobbelstenen_op_tafel.count(g) == 1 :
                dis.grote_straat = 40 
        p1.display()          
        
                   

# ========================================[-eerste worp dobbel stenen-]==========================================

def eerste_worp():
    print("==============================[-gerolde dobbelstenen-]================================================")
    global rondes,dobbelstenen_op_tafel
    rondes = 1  

    #delete()
    for i in range(0,5):
       
        dobbelstenen_op_tafel[i] = random.randint(1,6)
    print("ronde nummmer  " + str(rondes))    
    print(dobbelstenen_op_tafel)  
    
 
    print("======================================================================================================")  

# ==========================================[-tweede worp dobbel stenen-]=========================================

def tweede_worp():
    global rondes
    for i in range(0,5):
        vraag_dobbelstenen=input("wilt u dobbelsteen " + str(i + 1) + " opnieuw gooien (j / n) ?  " )
        
        if vraag_dobbelstenen == "j":
            dobbelstenen_op_tafel[i] = random.randint(1,6)

    rondes = rondes + 1                                          
    print("ronde nummer : " + str(rondes))           
    print(dobbelstenen_op_tafel)
    ronde_check()
  
    

# ==========================================[-ronde check-]=========================================================

def ronde_check():                 
    if rondes < 100:
        tweede_worp()

    else:
        punten()
    
# ==========================================[-retsart spel-]=========================================================     

def restart_spel():                                # | deze fuctie geef de class een waarde.
    global p1                                      # | en geeft de cordinaten een waarde.
    p1 = player(0,1,0,0,0,0,0,0,0,0,0,0,0,0)



# ==========================================[-telling gegooiden punten-]=============================================
def punten():
    global y,x
    p1.display
    for x in range(1,7):
        y = dobbelstenen_op_tafel.count(x)
        if y > 0:
            print("aantal " + str(x) + " : " + str(y))


   
    

# ==========================================[-onder yatzee-]===========================================
def keuzen_maken():
    # kleine straat 
    

    # grote straat 
    for g in range(1,7):
        if dobbelstenen_op_tafel.count(g) == 1:
            print("kies g om : grote straat toe te voegen voor 40 punten  ")


    # three of a kind 
    for i in range(1,7):
        if dobbelstenen_op_tafel.count(i) == 3:
            print("kies t om : three of a kind toe te voegen met 3 x " + str(i))
    
    # four of a kind 
    for x in range(1,7):
        if dobbelstenen_op_tafel.count(x) == 4:
            print("kies f om : four of a kind toe te voegen met 4 x " + str(x))

    # yatzee 
    for y in range(1,7):  
        if dobbelstenen_op_tafel.count(y) == 5:
            print("kies y om : yatzee toe te voegen voor 50 punten met " +str(y) + "en") 

    # ful house 
    for f in range(1,7):
        if dobbelstenen_op_tafel.count(f) == 3 and dobbelstenen_op_tafel.count(f)== 2:
           print("kies h om ful house toe te voegen voor 25 punten met  " + str(f) + "en")        
       
#================================[-boven yatzee-]=============================================
#            
    if dobbelstenen_op_tafel.count(1)>0 and p1.enen == 0:
        print("kies 1 om : " + str(dobbelstenen_op_tafel.count(1)) + " enen toe te voegen ")
                
    # tweeen tellen     
    if dobbelstenen_op_tafel.count(2)>0 and p1.tweeen == 0:
        print("kies 2 om : " + str(dobbelstenen_op_tafel.count(2)) + " tweeen toe te voegen " )


    # drieen tellen 
    if dobbelstenen_op_tafel.count(3)>0 and p1.drieen == 0:
        print("kies 3 om : " + str(dobbelstenen_op_tafel.count(3)) + " drieen toe te voegen ")

    # vieren tellen 
    if dobbelstenen_op_tafel.count(4)>0 and p1.vieren == 0:
        print("kies 4 om : " + str(dobbelstenen_op_tafel.count(4))+ " vieren toe te voegen ")

    # vijven tellen    
    if dobbelstenen_op_tafel.count(5)>0 and p1.vijven == 0:
        print("kies 5 om : " + str(dobbelstenen_op_tafel.count(5)) + " vijven toe te voegen")  

    # zessen toevoegen
    if dobbelstenen_op_tafel.count(6)>0 and p1.zessen == 0:
        print("kies 6 om : " + str(dobbelstenen_op_tafel.count(6)) + " zessen toe te voegen ")
        

      

#==============================================[-dobbelstenen punten toe voegen-]=========================================
    # enen invullen 

    vraag_keuze = input("wat wilt u toe voegen ")
    print(aantallen)

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
        p1.vijven_toevoegen()

    # zessen invullen 
    if vraag_keuze == "6":
        p1.zessen_toevoegen()

    # three of a kind invullen 
    if vraag_keuze == "t":
        p1.three_of_kind()   

    # four of a kind invullen     
    if vraag_keuze == "f":
        p1.four_of_kind()

    # yatzee invullen 
    if vraag_keuze == "y":
        p1.yatzeee()

    # ful house invullen werkt nog niet ...
    if vraag_keuze == "h":
        p1.ful_housee() 

    # grote straat 
    if vraag_keuze== "g":
        p1.grote_straatt()       

    else:
        print("keuze staat niet in de lijst kies bog een keer ")
        keuzen_maken()




# ==========================================[-aanroep-]===================================================================   
restart_spel()
p1.naam = input ("wat is u naam : ? ")
p1.display()

 
# ========================================================================================================================
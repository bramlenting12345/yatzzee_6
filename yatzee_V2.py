import random
from warnings import showwarning
import os 

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

# ========================================[-dobbel stenen weergaven-]===================================
class dobbelstenen:
    def __init__(dobbelsteen,ds1,ds2,ds3,ds4,ds5):
        dobbelsteen.ds1 = ds1
        dobbelsteen.ds2 = ds2
        dobbelsteen.ds3 = ds3 
        dobbelsteen.ds4 = ds4 
        dobbelsteen.ds5 = ds5

# ==========================================[-weergave dobbelstenen-]=================================

    def ds_weergave(dobbelstenen):
        print("dobbelsteen 1 : " + str(dobbelstenen.ds1))
        print("dobbelsteen 2 : " + str(dobbelstenen.ds2))
        print("dobbelsteen 3 : " + str(dobbelstenen.ds3))
        print("dobbelsteen 4 : " + str(dobbelstenen.ds4))
        print("dobbelsteen 5 : " + str(dobbelstenen.ds5))

# ============================================[-schudden dobbelsten-]===================================

def schudden_ds():
    ds.ds1 = random.randint(1,6)   
    ds.ds2 = random.randint(1,6)     
    ds.ds3 = random.randint(1,6)     
    ds.ds4 = random.randint(1,6)     
    ds.ds5 = random.randint(1,6)   

#==============================================[-selectie dobbel stenen-]==============================
def selecteer_ds(ds):
    vraag_dobbelstenen = input("welke dobbel stenen wilt u op nieuw gooien ")   
    for i in range (ds):
        vraag_dobbelstenen = input ("wilt u dobbelsteen " + dobbelstenen + "opnieuw gooien true / false ")
        if vraag_dobbelstenen == True:
            print 
         
        
        
        
        

# =========================================[-cordinaten en waardes class-]==============================================  

def restart_spel():
    global p1,ds
    p1 = player(0,1,0,0,0,0,0,0)
    ds = dobbelstenen(0,0,0,0,0)


    

# ===========================================[-aanroep programma-]========================================
        
restart_spel()
p1.naam = input("wat is u naam : ")  
p1.display()  
schudden_ds()
ds.ds_weergave() 
selecteer_ds()  



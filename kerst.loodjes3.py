import random 
import os 


namen = []
lootjes = []
trekking = {}

# ===================================(-def clear screen-)=========================================
def clear_screen():
    os.system("cls")


# ====================================(-input namen-)==============================================

def input_namen():
    vraag_doorgaan="ja"    
    while vraag_doorgaan == "ja":
        vraag_naam = input("welke naam wilt u toevoegen : ? ")
        
        if namen.count(vraag_naam) > 0:
            print("deze naam staat al in de lijst met lootjes : ")
        else: 
            namen.append(vraag_naam)    
        
        vraag_doorgaan = input("wilt u nog een naam aan de lootjes toevoegen : ? ")
        if len(namen) < 2:
            print("u moet minimaal twee namen aan de lootjes toevoegen : ")
            vraag_doorgaan = "ja"        
    return namen



# ======================================(-maak lootjes-)========================================

def maak_lootjes(namen):
    for i in (namen):
        lootjes.append(i)    
    return lootjes
    
    
# ======================================(-maak trekking-)========================================
       
def maak_trekking(namen,lootjes):
    random.shuffle(lootjes)
    
    for i in range(0,len(namen)):
        if namen[i] == lootjes[i]:
            maak_trekking(namen,lootjes)
        else:    
            trekking.update({namen[i] : lootjes[i] })
    return trekking    

        
# =======================================(-weergaven trekking-)====================================

def weergave_trekking(trekking):
    print("trekking lijst : ")

    for i in trekking:
        y = trekking.get(i)
        print(i + " -> " + y )


# ***************************************(-hoofd programma-)*****************************************     
input_namen()
maak_lootjes(namen)
clear_screen()
maak_trekking(namen,lootjes)
weergave_trekking(trekking)










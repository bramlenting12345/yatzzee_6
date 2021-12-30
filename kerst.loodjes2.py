import random 

namen = []
lootjes = []
trekking = {}



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



# ======================================(-lootjes schudden-)==========================================
def maak_lootjes(namen):
    for i in (namen):
        lootjes.append(i)    
    return lootjes
    
    
        
def maak_trekking(namen,lootjes):
    random.shuffle(lootjes)
    
    for i in range(0,len(namen)):
        if namen[i] == lootjes[i]:
            maak_trekking(namen,lootjes)
        else:    
            trekking.update({namen[i] : lootjes[i] })
    return trekking    

        



# ***************************************(-hoofd programma-)*****************************************     
input_namen()
maak_lootjes(namen)

maak_trekking(namen,lootjes)
print(trekking)










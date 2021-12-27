import random 

namen = []
lootjes = []
vraag_doorgaan = "ja"


# ====================================(-input namen-)===============================================
def input_namen():
    global vraag_doorgaan    
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

# ====================================(-lootjes maken-)=============================================
def lootjes_maken():
    global lootjes
    lootjes = namen.copy()
    

# ======================================(-lootjes trekken-)==========================================
def lootjes_trekken():
    global lootjes
    random.shuffle(lootjes)
    for x in range(0,len(namen)):
        print(namen[x] +" heeft lootje van : " + lootjes[x]) 
        
# ***************************************(-hoofd programma-)*******************************************     
input_namen()
lootjes_maken()
lootjes_trekken()




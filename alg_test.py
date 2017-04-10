import random
from operator import itemgetter

            


wort = input("Bitte ein nicht zu langen Testsatz eingeben: ")
Poolgroesse = int(input("Wie groß soll der Pool an Wörtern sein für die suche?: "))
Mutation = int(input("Wie hoch soll die Mutationsrate sein(in Prozent)?: "))


Alphabet = ['a', 'b', 'c','d', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ', '.', '!', '?']
wort = wort.lower()


#der pool an zeichen welche verwendet werden

wortlist = list(wort)
#Wörterpool bilden
 
wortzahl = Poolgroesse
wordrange = len(wortlist)
zahler = 0
generation = 0
wortliste = []
newcounter = Poolgroesse
while wortzahl > 0:
    
    wortzahl -= 1
    testwort = []
    
    counter = wordrange
        
    while counter > 0:        #erstellt zufällige wörter die genauso lang sind wie das eingegebene        
            
        counter -= 1
        buchstabe = random.choice(Alphabet)
        testwort.extend(buchstabe)
            
    zahler += 1
    wortstr = "".join(testwort)
    print(wortstr)              #packt alle in eine liste
    wortliste.insert(0, wortstr)

print(wortliste)

ScoreList = []
stopper = 0
innereliste = []
runde = 0
while 1 == 1:
    fufzisch = newcounter
    if stopper == 1: break
    
    print("next")
    if runde == 0:                  #legt fest aus welcher liste die 'elternwörter' kommen sollen
        variable1 = wortliste       #und leert die andere
        variable2 = innereliste
        innereliste = []
        print("1")
    else:
        variable1 = innereliste
        variable2 = wortliste
        wortliste = [] 
        print("2")
        
    #wörter testen
    
    generation += 1
    listcounter = 0
    counter2 = wordrange
    wordlistcount = len(variable1)
    
    timer = 0
    newList = []
    wlc2 = fufzisch
    while timer <= fufzisch:
        
        timer += 1
        
        
        wordtotest = list(itemgetter(wlc2 - 1)(variable1))
        wlc2 -= 1
        
        innercounter = wordrange
        
        wortscore = len([i for i, j in zip(wordtotest, wortlist) if i == j])#vergleicht das ursprungswort
                                                                            # die aus der liste und
                                                                            #gibt ihnen eine score
                                                                            #jeh nachdem wie nah sie am richtigen                                                       #sind
        if wortscore == 0: continue
        
        string = ''.join(wordtotest)
        werner = (10 + (5 * wortscore))
        
        while werner > 0:
            werner -= 1
            newList.insert(0, string)
            

        
    
    
    listcount = 0

    while listcount != fufzisch:
                                                # erstellt das paar der 'eltern'
        Wort1 = list(random.choice(newList))
        Wort2 = list(random.choice(newList))
        zahler1 = 0
        nachsteswort = []
        
        while zahler1 < wordrange:
            
            ifnumber = random.randint(0, 100)
                                                #nimmt die einzelnen buchstaben aus beiden 'eltern'
            letter1 = itemgetter(zahler1)(Wort1)
            letter2 = itemgetter(zahler1)(Wort2)
    
    
            if ifnumber >= 50:                  #suchtzufällig aus von welchem elternteil
                                                #der buchstabe kommt und sorgt für eine
                                                #1% 'mutationsrate'
                nachsteswort.extend(letter1)
            elif ifnumber <= Mutation:
                
                nachsteswort.extend(random.choice(Alphabet))
                
            else:
                nachsteswort.extend(letter2)
                
            zahler1 += 1
            
        einfugewort = ''.join(nachsteswort)
        
        print(einfugewort)
        
        if einfugewort == wort: # setzt die stopper variable auf 1 wenn das richtige
                                # wort vorkommt was dann das ganze beendet
            print("------------------------------------------------------------------")

            stopper = 1
            
        variable2.insert(0, einfugewort)
        
        if runde == 0:
            innereliste.insert(0, einfugewort)
            
        else:
           wortliste.insert(0, einfugewort) #setzt die neuen wörter in die jeweilige liste
           
        listcount += 1
        
    if runde == 0:
        runde += 1
    
    else:
        runde = 0
        

print("Geschafft")
print(generation, ". Generation")


    
    

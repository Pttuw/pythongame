from random import randint
import time
import datetime

#Deze functie is de loop voor het spel. Om uit deze loop te kunnen komen en niet de score/randomint te resetten heb ik een aparte functie gebouwd om op starten.
#Hierdoor blijft dus de score bestaan. Ook hoef je niet de namen opnieuw in te voeren op deze manier. Vanuit spelb() val je weer in de loop van spela(). 

def spela():
    global keuze1, keuze2, goed1, goed2, speler1, speler2, J, randomnummer, tijd, tijdgespeeld, tijdvoorbij
    while keuze1+keuze2 != randomnummer:
        keuze1=(int)(input(speler1+", kies een getal tussen de 1 en 100: "))
        if keuze1==randomnummer:
            print("Nicela!")
            goed1=goed1+1
            print("Huidige score",speler1,": ", goed1,". ",speler2,": ", goed2)
            nogeenkeer=input(str("Wilt u nog een keer spelen? J/N "))
            if nogeenkeer=="J":
                spelb()
                break
            else:
                print("Bedankt voor het spelen. De eindscore is", speler1, "heeft: ",goed1,"! ",speler2," heeft: ",goed2,"!")
                tijdvoorbij=time.time()
                tijdgespeeld=tijd-tijdvoorbij
                print("U heeft gespeeld: ",time.strftime("%H:%M:%S", time.gmtime(tijdgespeeld)))
                break
        elif keuze1<=randomnummer:
            print("Het getal is hoger")
            keuze2=(int)(input(speler2+", kies een getal tussen de 1 en 100: "))
            if keuze2==randomnummer:
                print("Goedzo!")
                goed2=goed2+1
                nogeenkeer=input(str("Wilt u nog een keer spelen? J/N "))
                if nogeenkeer=="J":
                    spelb()
                    break
                else:
                    print("Bedankt voor het spelen. De eindscore is", speler1, "heeft: ",goed1,"! ",speler2," heeft: ",goed2,"!")
                    tijdvoorbij=time.time()
                    tijdgespeeld=tijd-tijdvoorbij
                    print("U heeft gespeeld: ",time.strftime("%H:%M:%S", time.gmtime(tijdgespeeld)))
                    break
                print("Huidige score",speler1,": ", goed1,". ",speler2,": ", goed2)
            elif keuze2 <= randomnummer:
                print("Het getal is hoger")
            elif keuze2 >= randomnummer:
                print("Het getal is lager")         
        elif keuze1>=randomnummer:
            print("Het getal is lager")
            keuze2=(int)(input(speler2+", kies een getal tussen de 1 en 100: "))
            if keuze2==randomnummer:
                print("Wooooot!")
                goed2=goed2+1
                print("Huidige score",speler1,": ", goed1,". ",speler2,": ", goed2)
                nogeenkeer=input(str("Wilt u nog een keer spelen? J/N "))
                if nogeenkeer=="J":
                    spelb()
                    break
                else:
                    print("Bedankt voor het spelen. De eindscore is", speler1, "heeft: ",goed1,"! ",speler2," heeft: ",goed2,"!")
                    tijdvoorbij=time.time()
                    tijdgespeeld=tijd-tijdvoorbij
                    print("U heeft gespeeld: ",time.strftime("%H:%M:%S", time.gmtime(tijdgespeeld)))
                    break
                print("Huidige score",speler1,": ", goed1,". ",speler2,": ", goed2)
            elif keuze2 <= randomnummer:
                print("Het getal is hoger")
            elif keuze2 >= randomnummer:
                print("Het getal is lager")
    else:
        print("Bedankt voor het spelen. De eindscore!", speler1, "heeft: ",goed1,"! ",speler2," heeft: ",goed2,"!")
        print("U heeft gespeeld: ",tijdgespeeld)

#Een aparte functie om de scoreteller en het randomint nummer niet te resetten.
def spelb():
    global goed1, goed2, keuze1, keuze2, speler1, speler2, J, randomnummer, tijd, tijdgespeeld, tijdvoorbij
    randomnummer=randint(1,100)
    keuze1=(int)(input(speler1+", kies een getal tussen de 1 en 100: "))
    if keuze1==randomnummer:
        print("goedzo")
        goed1=goed1+1
        nogeenkeer=(str)(input("Wilt u nog een keer spelen? J/N "))
        if nogeenkeer==J:
            spelb()
        else:
            quit()
    elif keuze1 <= randomnummer:
        print("Het getal is hoger")
        keuze2=(int)(input(speler2+", kies een getal tussen de 1 en 100: "))
        if keuze2 <= randomnummer:
            print("Het getal is hoger")
            spela()
        elif keuze2 >= randomnummer:
            print("Het getal is lager")
            spela()
        elif keuze2==randomnummer:
            print("Goedzo!")
            goed2=goed2+1
    elif keuze1 >= randomnummer:
        print("Het getal is lager")
        keuze2=(int)(input(speler2+", kies een getal tussen de 1 en 100: "))
        if keuze2 >= randomnummer:
            print("Het getal is lager")
            spela()
        elif keuze2 <= randomnummer:
            print("Het getal is hoger")
            spela()
        elif keuze2 == randomnummer:
            print("Goedzo")
            goed2=goed2+1
    
                

goed1=0
goed2=0
speler1=input("Speler 1, wat is uw naam?:")
speler2=input("Speler 2, wat is uw naam?:")
tijd=time.time()


spelb()    

#Vključimo 'datetime', kar bomo potrebovali da vemo katero je trenutno leto
import datetime

#Dobimo informacije osebe skozi metodo input() in jo zapišemo vsako v svojo spremenljivko.
ime = input("Ime:")
#dobijemo letnico rojstva kot string(tekst) in ga spremenimo v število:
rojstvo_letnica = int(input("Letnica rojstva:"))
spol = input("Spol(ž/m):")
imel_rojstni_dan = input("Ali si to leto imel rojstni dan?(da/ne)")

#Izračunamo starost (od trenutnega leta odštejemo leto rojstva)..
starost = datetime.datetime.now().year - rojstvo_letnica

#če to leto še ni imel/a rojstnega dneva, odštejemo še 1 leto
if str.upper(imel_rojstni_dan) == "NE":
    starost = starost - 1

#spremenljivko spremenimo v string (tekst), da jo lahko potem izpišemo (drugače dobimo napako).
starost = str(starost)

#Če je oseba starejša od 18 (ali stara 18), je vrednost spremenljivke 'polnoleten' True, kar pomeni da je oseba polnoletna, če pa je mlajša od 18, je vrednost variable False, kar pomeni da ni polnoletna
polnoleten = int(starost) >= 18

#preverimo če je oseba moškega spola...
if str.upper(spol) == "M":
    #če je, preverimo če je oseba polnoletna:
    if polnoleten:
        print("Dragi " + ime + " ti si star " + starost + " let in si polnoletna oseba.")
    #če ni polnoletna...
    else:
        print("Dragi " + ime + " ti si star " + starost + " let in nisi polnoletna oseba.")
#če ni moškega spola...
else:
    # če je, preverimo če je oseba polnoletna:
    if polnoleten:
        print("Draga " + ime + " ti si stara " + starost + " let in si polnoletna oseba.")
    # če ni polnoletna...
    else:
        print("Draga " + ime + " ti si stara " + starost + " let in nisi polnoletna oseba.")
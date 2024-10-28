import json

try:
    f = open("osallistujat.json", "r")
    participants = json.load(f)
    f.close()
except IOError:
    # makes the file if it does not exist
    participants = {}
    
osalMaara = len(participants.keys())

languages = ["englanti", "ruotsi", "saksa", "espanja"]

# save the dictionary made from uusiOsallistuja() to the osallistujat file
def tallennaOsallistujat(participant):
    f = open("osallistujat.json", "w")
    json.dump(participant, f)
    f.close()

def kysyKieli(kielenNimi):
    kieli = 6
    # check that the int is a valid number between 0 and 5
    while kieli > 5 or kieli < 0:
        try:
            kieli = int(input("Kielitaitosi kielessa " + kielenNimi + " (0-5): "))
        except ValueError:
            print("Kielitaito ei ollut luku 0-5 välillä.")
            continue
    return kieli

# take the test subjects name, age, living place and language skills
def uusiOsallistuja():
    # maybe doesn't need a check whether it is valid
    name = input("Etu- ja sukunimesi: ")
    while True:
        try:
            age = int(input("Ikasi?: "))
        except ValueError:
            print("Ikä ei ollut luku. Yritä uudelleen.")
            continue

        # Insert test that checks that the age is a valid number, not too small (-) or too big
        if age <= 0 or age > 120:
            print("Ikä ei ollut sopiva luku. Yritä uudelleen.")
            continue
        break
    asuinPaikka = input("Asuinpaikkasi?: ")
    kieliTaito = [(i, kysyKieli(i)) for i in languages]
    global osalMaara # TODO tässä muutetaan muuttujaa toisessa tiedostossa koska se on global
    osalMaara += 1
    khTiedot = {"Nimi" : name, "Ika" : age, "Asuinpaikka" : asuinPaikka, "Kielitaito" : kieliTaito}
    return khTiedot

def lisaaOsallistuja(osalLista, osalMaara):
    osalLista["KH" + str(osalMaara)] = uusiOsallistuja()
    tallennaOsallistujat(osalLista)

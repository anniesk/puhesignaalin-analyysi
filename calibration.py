import trainingStructure as ts
import taustaTiedot as tau
import json
import os


def kalibrointi():

    try:
        f = open("osallistujat.json", "r")
        participants = json.load(f)
        f.close()


    # if file does not exist previously
    except IOError:
        participants = {}

    osalMaara = 0
    # if no previous subjects -> only one participant (the one doing it currently)
    if len(participants.keys()) == 0:
        osalMaara = 1
    else:
        # if previous add + 1
        osalMaara = len(participants.keys()) + 1

    # KH = koehenkilö
    participants["KH" + str(osalMaara)] = tau.uusiOsallistuja()
    koehenkilo = "KH" + str(osalMaara)

    tiedostot = [koehenkilo + "_kalib1", koehenkilo + "_kalib2", koehenkilo + "_kalib3"] # why do we set up 3 files? to make the calibration I guess
    os.makedirs(koehenkilo) # make directory for the participant

    tau.tallennaOsallistujat(participants)

    ts.kalibraatio(tiedostot, koehenkilo, "uusi") # koehenkilo = string of the KH + number, tiedostot are the filenames

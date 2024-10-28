import audioRecorder as ar
import parselmouth as pm
import listaMetodit as lm
import json
import os.path

vokaalien_formantit = {}


def kalibraatio(tiedostoLista, polku, teksti):
    print("Seuraavaksi äänität jokaisen vokaalin kolmeen kertaan, jotta vokaaliavaruutesi voidaan kalibroida oikein. \n")

    # ask whether they want to do the calibration again fully or only do the missing ones
    if teksti == "vanha":
        while True:
            try:
                check = int(input("Haluatko: \n 1. tehdä kalibraation kokonaan uudelleen \n vai \n 2. tehdä vain puuttuvat kalibroinnit \n"))
            except ValueError:
                print("Syöte ei ollut numero. Yritä uudelleen.")
                continue
            if check not in [1,2]: 
                print("Syöte ei ollut yksi vaihtoehdoista. Yritä uudelleen")
                continue
            else:
                break
    else:
        # initialize so that the code below works :p
        check = 0

    # because we make 3 files to the list in taustatiedot we do the recording three times
    for vokaali in ["a", "e", "i", "o", "u", "y", "ä", "ö"]:
        for tiedosto in tiedostoLista:

            # if only want to do the calibration for missing files
            if check == 2:
                # check whether the file already exists
                tiedostonimi = polku + "/" + tiedosto+vokaali + ".wav"
                if os.path.exists(tiedostonimi):
                    # if file exists skip to the next one
                    continue

            print("Äänitys kalibraatio", tiedostoLista.index(tiedosto)+1, "/", len(tiedostoLista))
            print("Äänitä seuraava vokaali", vokaali.upper())
            while True:
                aloitus = input("Aloita äänitys? Kyllä (k) /Ei (e)?: ")
                if aloitus == "k":
                    break
                elif aloitus == "e":
                    quit()
                else:
                    continue

            # here in nauhoitus it just basic recording, everything else happens in this file
            file_name = ar.nauhoitus(1, tiedosto+vokaali, polku)
            
            # TODO TÄNNE JOKIN FAILSAFE JOS NAUHOITUS "EPÄONNISTUUKIN" PÄÄSEE SITTEN TEKEMÄÄN UUDEN :D

            # parselmouth
            s = pm.Sound(file_name)
            if vokaali == "u":
                formant = s.to_formant_burg(maximum_formant=4000.0)
            else:
                formant = s.to_formant_burg(maximum_formant=4000.0) # default arvot oli samat kuin tuolla praat skriptissä 

            #print(formant)
            # take formant at time 0.5 because recording is 1 second long
            f1 = formant.get_value_at_time(1, 0.5)  # First formant frequency (second input is the point in time when to analyse)
            f2 = formant.get_value_at_time(2, 0.5)  # Second formant frequency

            # TODO tarkista onko formantti jotenkin järkevä, että pitääkö joko äänittää uudelleen tai muuttaa maximum formanttia?

            print("vokaali:", vokaali)
            print("f1", f1)
            print("f2", f2)

            # add to the dictionary for later use
            # need to check if these exist first
            if vokaali in vokaalien_formantit:
                f1_lista = vokaalien_formantit[vokaali]["f1"]
                f2_lista = vokaalien_formantit[vokaali]["f2"]

                f1_lista.append(f1)
                f2_lista.append(f2)
            else:
                f1_lista = [f1]
                f2_lista = [f2]

            vokaalien_formantit[vokaali] = {"f1": f1_lista, "f2": f2_lista}


    # save all the formants
    print("vokaalien formantit")
    f = open(polku + "/" + tiedosto + "_formantit.txt", "w", encoding='utf8')
    json.dump(vokaalien_formantit, f , ensure_ascii=False)
    f.close()

    print("Kalibraatio valmis")
    

    
    # f = open("KH2/KH2_kalib3_formantit.txt")
    # test = json.load(f)
    # f.close()
    mean =  lm.laskeSuhteet(vokaalien_formantit)  #lm.laskeSuhteet(test) # tulos
    f = open(polku + "/" + "KH" + "_suhteet.txt", "w")
    json.dump(mean, f) # tulos
    f.close()

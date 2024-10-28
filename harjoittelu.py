import vokaaliAvaruus as va
import json
import audioRecorder as ar
import parselmouth as pm
import listaMetodit as lm


def harjoittele():
    try:
        f = open("osallistujat.json", "r")
        participants = json.load(f)
        f.close()

    # if file does not exist previously
    except IOError:
        print("Osallistujia ei ole olemassa!")
        quit()


    while True:
        # print the participant number and name because nobody will actually remember those...
        for participant in participants:
            print(participant)

        try:
            osallistuja = int(input("Mikä oli koehenkilönumerosi?"))
        except ValueError:
            print("Input ei ollut numero. Yritä uudelleen.")
            continue

        if "KH"+str(osallistuja) in participants:
            tiedosto = "KH"+str(osallistuja)+"/KH_suhteet.txt"
            try:
                f = open(tiedosto, "r")
                f.close()

            # if file does not exist previously
            except IOError:
                print("Kalibrointia ei ole tehty loppuun. Käy tekemässä se ja yritä myöhemmin uudelleen.")
                quit()
                # TODO vie kalibrointiin takaisin? tai sulje
            break
        else:
            print("Koehenkilönumeroa ei löytynyt osallistujien listasta. Yritä uudelleen.")
            continue

            
    # take the previous ratio numbers 
    f = open(tiedosto)
    mean = json.load(f)
    f.close()


    while True:
        # TODO tämä siis jatkuu näin loputtomiin :D periaatteessa voisi olla valikko josta valita mitä vokaalia harjoitella
        # TODO maybe ask what they want to practice??? and have obvs different vowels
        for vokaali in ["a", "e", "i", "o", "u", "y", "ä", "ö"]:
            print("Äänitä seuraava vokaali", vokaali.upper())
            while True:
                aloitus = input("Aloita äänitys? Kyllä (k) /Ei (e)?: ")
                if aloitus == "k":
                    break
                elif aloitus == "e":
                    quit()
                else:
                    continue

            # here in nauhoitus is just basic recording, everything else happens in this file
            file_name = ar.nauhoitus(1, "KH"+str(osallistuja)+vokaali, "KH"+str(osallistuja))

            # parselmouth
            s = pm.Sound(file_name)
            if vokaali == "u":
                formant = s.to_formant_burg(maximum_formant=4000.0)
            else:
                formant = s.to_formant_burg(maximum_formant=4000.0)

            #print(formant)
            f1 = formant.get_value_at_time(1, 0.5)  # First formant frequency (second input is the point in time when to analyse)
            f2 = formant.get_value_at_time(2, 0.5)  # Second formant frequency
            print("vokaali:", vokaali)
            print("f1", f1)
            print("f2", f2)

            #suhde = lm.laskeUudet(suhteet, f1, f2) # TODO tee jotain niille uusille formanteille :DDD 

            va.vokaaliHarjoittelu(mean, f1, f2, vokaali)
import harjoittelu
import calibration
import json
import trainingStructure as ts

# this is the file to run when you want to start making a new calibration


# TODO tee requirements tiedosto!

while True:
    try:
        check = int(input("Haluatko: \n 1. luoda uuden osallistujan ja kalibroida vokaaliavaruuden \n 2. harjoitella uusia äänteitä ja piirtää ne vokaaliavaruuteen \n 3. ladata koehenkilön tiedot ja tehdä kalibroinnin (joka jäänyt kesken) \n"))
    except ValueError:
        print("Syöte ei ollut numero. Yritä uudelleen.")
        continue
    if check == 2:
        harjoittelu.harjoittele()
    if check == 1:
        calibration.kalibrointi()
    if check == 3:
        # if calibration is not done and want to load the participant 
        # TODO :D this functionality could be in a different file or def... because I use some of it in harjoittelu as well....
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
                koehenkilo = int(input("Mikä oli koehenkilönumerosi?"))
            except ValueError:
                print("Syöte ei ollut numero. Yritä uudelleen.")
                continue
            if "KH"+str(koehenkilo) in participants:
                break
            else:
                print("Koehenkilönumeroa ei löytynyt osallistujien listasta. Yritä uudelleen.")
                continue

        tiedostot = ["KH"+str(koehenkilo) + "_kalib1", "KH"+str(koehenkilo) + "_kalib2", "KH"+str(koehenkilo) + "_kalib3"] # why do we set up 3 files? to make the calibration I guess
        ts.kalibraatio(tiedostot, "KH"+str(koehenkilo), "vanha")


    elif check not in [1,2,3]: 
        print("Syöte ei ollut yksi vaihtoehdoista. Yritä uudelleen")
        continue
    else:
        # return to the "menu"
        continue
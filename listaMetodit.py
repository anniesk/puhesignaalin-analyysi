import statistics
import numpy as np


# TODO suhteiden sijaan keskiarvo niistä kolmesta kalibroinnista????? -> testiin koska en ymmärrä näistä suhteista muuten mitään



def laskeSuhteet(formanttiLista):    

    f1 = []
    f2 = []

    for vokaali in formanttiLista:
        # make this for each vowel at a time
        print(vokaali)
        print(formanttiLista[vokaali])
        f1.append((formanttiLista[vokaali]["f1"]))
        f2.append((formanttiLista[vokaali]["f2"]))


    mean_f1 = []
    mean_f2 = []
    # take mean for each vowel
    for one,two in zip(f1,f2):
        mean_f1.append(np.mean(one))
        mean_f2.append(np.mean(two))

    return list(zip(mean_f1, mean_f2))

    # f1 = []
    # f2 = []
    # f1_new = []
    # f2_new = []
    # suhteet = []

    # for vokaali in formanttiLista:
    #     # make this for each vowel at a time
    #     print(vokaali)
    #     print(formanttiLista[vokaali])
    #     f1.append((formanttiLista[vokaali]["f1"]))
    #     f2.append((formanttiLista[vokaali]["f2"]))

    #     # take mean from each vowel calibration (idk if I should adjust the range or something? or calculate the suhde somehow differently)
    #     f1_new.append(statistics.mean(formanttiLista[vokaali]["f1"]))
    #     f2_new.append(statistics.mean(formanttiLista[vokaali]["f2"]))

    #     print(f1_new)
    #     print(f2_new)

    # # flatten
    # flat_f1 = [x for xs in f1 for x in xs]
    # flat_f2 = [x for xs in f2 for x in xs]

    # # range pitää olla kaikkien keskiarvosta, sitten voi laskea suhteen :D
    # f1range = float(sorted(flat_f1)[-1]) - float(sorted(flat_f1)[0])
    # f2range = float(sorted(flat_f2)[-1]) - float(sorted(flat_f2)[0])

    # # TODO HOW TO DO THIS SO IT DOESN'T SUCK :D maybe need to check before that the f1 and f2 values even make sense lol
    # f1suhde = [(i - sorted(f1_new)[0])/f1range for i in f1_new]
    # f2suhde = [(i - sorted(f2_new)[0])/f2range for i in f2_new]

    # suhteet = []
    # for i in range(0,len(f1suhde)):
    #     suhteet.append((float(f1suhde[i]), float(f2suhde[i])))

    # return suhteet



# def laskeUudet(suhteet, f1, f2):
#     print()
#     # TODO laske jotenkin järkevä suhde noille uusille f1 ja f2 ja palauta ne :D

#     # flatten
#     flat_f1 = [x[0] for x in suhteet]
#     flat_f2 = [x[1] for x in suhteet]

#     f1range = float(sorted(flat_f1)[-1]) - float(sorted(flat_f1)[0])
#     f2range = float(sorted(flat_f2)[-1]) - float(sorted(flat_f2)[0])

#     # TODO tämähän menee ihan päin helvettiä lol (miksi laskea suhteita jos voin vaan pistää ne kuitenki suoraan periaatteessa siihen plottiin alunperinkin????)
#     f1suhde = f1 - sorted(flat_f1)[0] / f1range
#     f2suhde = f2 - sorted(flat_f2)[0]/ f2range

#     print(f1suhde,flat_f1[0])

#     suhde = [f1suhde, f2suhde]

#     return suhde


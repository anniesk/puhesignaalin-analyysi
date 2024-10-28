import matplotlib.pyplot as plt
import json


# def vokaaliAvaruus(tiedosto):
#     f = open(tiedosto) 
#     suhteet = json.load(f)
#     f.close()

#     xaxis = [i[1] for i in suhteet]
#     yaxis = [i[0] for i in suhteet]

#     for i, j in zip(suhteet, ["a", "e", "i", "o", "u", "y", "ä", "ö"]):
#         print(i,j)

#     scatter = plt.scatter(xaxis, yaxis)
#     ax = scatter.axes
#     #ax.invert_xaxis()
#     #ax.invert_yaxis()

#     for i, txt in enumerate(["a", "e", "i", "o", "u", "y", "ä", "ö"]):
#         ax.annotate(txt, (xaxis[i], yaxis[i]))

#     plt.show()

def vokaaliHarjoittelu(mean, f1, f2, vokaali): #(suhteet, suhde, vokaali):

    xaxis = [i[1] for i in mean] # suhteet
    yaxis = [i[0] for i in mean] # suhteet
    x = f2 #suhde[1]
    y = f1 #suhde[0]

    for i, j in zip(mean, ["a", "e", "i", "o", "u", "y", "ä", "ö"]): # suhteet
        print(i,j)

    scatter_new = plt.scatter(x, y, color='red')
    ax_new = scatter_new.axes
    ax_new.annotate(vokaali, (x, y))

    scatter = plt.scatter(xaxis, yaxis)
    ax = scatter.axes
    ax.invert_xaxis()
    ax.invert_yaxis()
    ax.yaxis.tick_right()
    ax.xaxis.tick_top()
    ax.set_xlabel("F1",fontsize=16)
    ax.set_ylabel("F2",fontsize=16)
    ax.yaxis.set_label_position("right")
    ax.xaxis.set_label_position("top")

    for i, txt in enumerate(["a", "e", "i", "o", "u", "y", "ä", "ö"]):
        ax.annotate(txt, (xaxis[i], yaxis[i]))


    plt.show()


    # TODO voisi opetella muotoilemaan taustaksi sen vokaalikulmion :D 


from pylab import *
listex = []
liste_y1 = []
liste_y2 = []
for x in range(5, 15):
    listex.append(x)
    liste_y1.append(3)
    liste_y2.append(5)
plot(listex, liste_y1, '.k')
plot(listex, liste_y2, '.k')
xlim(0, 20)
ylim(2.0, 6.0)
show()

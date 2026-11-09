from pylab import *
listex = []
listey = []
for x in range(10, 41):
    listex.append(x)
    listey.append(x)
plot(listex, listey, '.k')
xlim(0, 50)
ylim(0, 50)
show()
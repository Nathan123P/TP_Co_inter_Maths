from pylab import *
lx = []
ly1 = []
ly2 = []
ly3 = []
for x in range(1, 21):
    lx.append(x)
    ly1.append(0.5 * x)
    ly2.append(1 * x)
    ly3.append(2 * x)
plot(lx, ly1, '*', color='orange')
plot(lx, ly2, 'ob')
plot(lx, ly3, 'dr')
xlim(0, 25)
ylim(0, 45)
show()
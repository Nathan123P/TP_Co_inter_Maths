from pylab import*
xlim(0, 50, 10)
ylim(2, 50, 10)
for i in range (31):
    x=10+i
    y=x
    plot(x, y, 'ob')
show()
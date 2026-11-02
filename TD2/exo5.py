from pylab import*
xlim(0,20)
ylim(0,30)
for j in range (10,20):
    y=10+j
    for i in range(5,15):
        x=5+i
        plot(x,y,"ob")
    show()
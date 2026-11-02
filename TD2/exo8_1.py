from pylab import*
xlim(-3,3,1)
ylim(-30,30,5)
liste_x=[]
liste_y=[]
for i in range (100):
    x = -3+0.006*i
    y=x**3
    liste_x.append(x)
    liste_y.append(y)
    plot(liste_x,liste_y,'k')
show()
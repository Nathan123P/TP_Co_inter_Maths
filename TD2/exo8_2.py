from pylab import*
xlim(-5,5,1)
ylim(-50,50,1)
liste_x=[]
liste_y=[]
for i in range (250):
    x = -5+0.02*i
    y=1/x
    liste_x.append(x)
    liste_y.append(y)

for i in range (250):
    x = 0.02+0.02*i
    y=1/x
    liste_x.append(x)
    liste_y.append(y)
    
    plot(liste_x,liste_y,'k')
show()
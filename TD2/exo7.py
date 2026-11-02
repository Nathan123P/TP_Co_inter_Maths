from pylab import*
xlim(0,25,5)
ylim(0,45,5)
for i in range (21):
    x = i
    y_1=2*x
    y_2=x
    y_3=0.5*x
    plot(x, y_1, 'dr')
    plot(x, y_2, 'ob')
    plot(x, y_3, '*r')
show()
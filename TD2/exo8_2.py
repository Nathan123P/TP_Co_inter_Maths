from pylab import *
import numpy as np
x1 = np.linspace(-5, -0.01, 250)
x2 = np.linspace(0.01, 5, 250)
y1 = 1 / x1
y2 = 1 / x2
plot(x1, y1, 'r-', linewidth=2, label='f(x) = 1/x')
plot(x2, y2, 'r-', linewidth=2)
xlabel('x')
ylabel('y')
xlim(-6, 6)
ylim(-10, 10)
grid(True)
legend()
show()
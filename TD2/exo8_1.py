from pylab import *
import numpy as np
x = np.linspace(-3, 3, 100)
y = x**3  
plot(x, y, 'b-', linewidth=2, label='f(x) = x^3')
xlabel('x')
ylabel('y')
grid(True)
legend()
show()
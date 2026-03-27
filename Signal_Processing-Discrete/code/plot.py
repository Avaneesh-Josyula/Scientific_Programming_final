import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Define system: y'' = sin(2x) - alpha*y
def system(state, x, alpha):
    y, v = state
    dydx = v
    dvdx = np.sin(2*x) - alpha * y
    return [dydx, dvdx]
    
# Timeline and start state (at rest)
x = np.linspace(0, 50, 1000)
start = [0, 0]

# Solve for Non-resonance (Alpha=2) and Resonance (Alpha=4)
y_non = odeint(system, start, x, args=(2,))[:, 0]
y_resonant = odeint(system, start, x, args=(4,))[:, 0]

# Plotting
plt.figure(figsize=(10, 5))
plt.plot(x, y_non, label='Alpha=2: Non-Resonance (Mismatch)', color='gray')
plt.plot(x, y_resonant, label='Alpha=4: Resonant (Match)', color='red')

plt.title('Amplitude Comparison: Mismatched vs. Matched Frequencies')
plt.xlabel('x (Time)')
plt.ylabel('y (Displacement)')
plt.legend()
plt.grid(True)
plt.savefig("../plot.png")
plt.show()

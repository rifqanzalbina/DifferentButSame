import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# === Codes ===
def pendulum(y, t, g, L):
    theta, omega = y
    dydt = [omega, -g/L * np.sin(theta)]
    return dydt

g = 9.8
L = 1.0

theta0 = np.pi/4
omega0 = 0.0
y0 = [theta0, omega0]

t = np.linspace(0, 10, 100)
sol = odeint(pendulum, y0, t, args=(g,L))

plt.plot(t, sol[:, 0])
plt.xlabel('Waktu (s)')
plt.ylabel('Sudut (rad)')
plt.title('Pendilium sederhana')
plt.grid(True)
plt.show()
# === EndCodes ===
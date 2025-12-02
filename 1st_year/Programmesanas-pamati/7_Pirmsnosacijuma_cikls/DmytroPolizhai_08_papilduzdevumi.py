"""
Ciklu lietošana līkņu veidošanā, uzzīmē grafiku Y = x2, ja x mainās diapazona no -3 līdz 3 ar soli 1, izmantojot matplotlib bibliotēku, 
kura palīdz izvadīt grafiku

Izveidoja: Dmytro Polizhai
"""

import matplotlib.pyplot as plt
import numpy as np

raw_y = []
raw_x = []

for x in range(-3, 4):
    y = x ** 2
    raw_x.append(x)
    raw_y.append(y)

x_points = np.array(raw_x)
y_points = np.array(raw_y)

plt.plot(x_points, y_points)
plt.show()
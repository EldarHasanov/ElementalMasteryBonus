import numpy as np
import math as m
import matplotlib.pyplot as plt

Wape = lambda em: 278 * em / (em + 1400)

WapeDer = lambda em: (278 * (1400 / pow((em + 1400), 2) ) )

Over = lambda em: 1600 * em / (em + 2000)

OverDer = lambda em: (1600 * (2000 / pow((em + 2000), 2) ) )

fig = plt.subplots()
x = np.linspace(0, 2000, 2000)

plt.plot(x, Wape(x), color = 'red')
plt.plot(x, Over(x), color='green')

plt.xlabel('Elemental mastery', color='gray')
plt.ylabel('DMG bonus %',color='gray')
plt.grid(True)

plt.figure()
plt.plot(x, WapeDer(x), color = 'red')
plt.plot(x, OverDer(x), color='green')

plt.xlabel('Elemental mastery', color='gray')
plt.ylabel('Bonus growth',color='gray')
plt.grid(True)

plt.show()
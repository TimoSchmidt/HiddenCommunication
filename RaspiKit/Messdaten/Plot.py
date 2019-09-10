import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

x, y = np.loadtxt('ServerPrinzipAlle2SekSenden.txt', delimiter = ' ', unpack = True)

'''
plt.plot(x, y)
plt.xlabel('Zeit in s')
plt.ylabel('Temperatur in °C')
plt.title('2 Sekunden senden, 8 Sekunden warten')
#plt.xticks(np.arange(min(x), max(x) + 1, 10.0)) # +1 to show the last step

'''
fig, ax = plt.subplots()
ax.plot(x,y, color = 'royalblue', linewidth = '1.5')
# x-Axis
ax.xaxis.set_ticks(np.arange(min(x), max(x) + 10.0, 10.0))
ax.xaxis.set_major_formatter(ticker.FormatStrFormatter('%0.1f'))
# y-Axis
ax.yaxis.set_ticks(np.arange(min(y)-0.01, max(y)+0.05, 0.02))
ax.yaxis.set_major_formatter(ticker.FormatStrFormatter('%0.2f'))

plt.xlabel('Zeit in s', fontweight = 'bold')
plt.ylabel('Temperatur in °C', fontweight = 'bold')
plt.title('')
plt.grid(True, linestyle = '--', linewidth = '0.5')

plt.show() # Anzeige am Ende


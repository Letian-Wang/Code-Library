import matplotlib.pyplot as plt
import numpy as np
''' ax 理解为一套坐标轴 '''
A = np.arange(1,5)
B = A**2
C = A**3
# fig = plt.figure()
# ax = fig.add_subplot(1,1,1)
fig, ax = plt.subplots(figsize=(14,7))
ax.plot(A,B)
ax.plot(B,A)

# title, labels
ax.set_title('Title')
ax.set_xlabel('xlabel', fontsize=18,fontfamily = 'sans-serif',fontstyle='italic')
ax.set_ylabel('ylabel', fontsize='x-large',fontstyle='oblique')
ax.legend()

# property
ax.set_aspect('equal')
ax.minorticks_on()
ax.set_xlim(0,16)
ax.grid(which='minor', axis='both')

# axis, ticks
ax.xaxis.set_tick_params(rotation=45,labelsize=18,colors='w') 
start, end = ax.get_xlim() 
ax.xaxis.set_ticks(np.arange(start, end,1)) 
ax.yaxis.tick_right()
plt.show()
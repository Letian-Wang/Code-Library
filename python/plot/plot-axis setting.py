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

# axis, ticks
ax.set_xticks(position)  ## setting tick position
ax.set_xticklabels(label, fontsize=18)  ## setting tick labels and fontsize
ax.tick_params(axis="y", labelsize=18)  # set fontsize only

# font
    # title:
    csfont = {'fontname':'Times New Roman'}
    plt.title('title',**csfont)

    # label:
    ax.set_xlabel("Median Population", fontname="Arial", fontsize=12)

    # legend:
    plt.legend(prop={'family': 'Arial'})

    # tick
    for tick in ax.get_xticklabels():
        tick.set_fontname("Comic Sans MS")
    for tick in ax.get_yticklabels():
        tick.set_fontname("Comic Sans MS")

# axes thickness and color
for tick in ax.xaxis.get_major_ticks():
    tick.label1.set_fontsize(fontsize)
    tick.label1.set_fontweight('bold')
for tick in ax.yaxis.get_major_ticks():
    tick.label1.set_fontsize(fontsize)
    tick.label1.set_fontweight('bold')


# color
    # When using figures, you can easily change the spine color with:
    ax.spines['bottom'].set_color('#dddddd')
    ax.spines['top'].set_color('#dddddd') 
    ax.spines['right'].set_color('red')
    ax.spines['left'].set_color('red')

    # Use the following to change only the ticks:
    ax.tick_params(axis='x', colors='red')
    ax.tick_params(axis='y', colors='red')

    # And the following to change only the label:
    ax.yaxis.label.set_color('red')
    ax.xaxis.label.set_color('red')

    # And finally the title:
    ax.title.set_color('red')
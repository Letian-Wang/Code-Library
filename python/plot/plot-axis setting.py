import matplotlib.pyplot as plt
import numpy as np
# ax
    ''' ax 理解为一套坐标轴 '''
    # create 
    A = np.arange(1,5)
    B = A**2
    C = A**3
    # fig = plt.figure()
    # ax = fig.add_subplot(1,1,1)
    fig, ax = plt.subplots(figsize=(14,7))
    ax.plot(A,B)
    ax.plot(B,A)
    # setting
    ax.set_aspect('equal')                      # the ratio of y-unit to x-unit
    ax.set_xlim(0,16)                           # range
    ax.grid(which='minor', axis='both')         # grid
    # axes setting
    for axis in ['top','bottom','left','right']:
        ax.spines[axis].set_linewidth(0.5)
        ax.spines[axis].set_color('Blue') 
        ax.spines[axis].set_visible(False) 

# tick setting
    # axis, ticks
    ax.set_xticks(position)  ## setting tick position
    ax.set_xticklabels(label, fontsize=18)  ## setting tick labels and fontsize
    ax.tick_params(axis="y", labelsize=18)  # set fontsize only
    start, end = ax.get_xlim() 
    ax.xaxis.set_ticks(np.arange(start, end,1)) 
    # space
    ax.tick_params(axis='both', which='major', pad=15, labelseize=18, colors='red')
    ax.tick_params(axis='x', which='major', pad=15, labelseize=18, colors='red')
    # font
    for tick in ax.get_xticklabels():
        tick.set_fontname("Times New Roman")
    for tick in ax.get_yticklabels():
        tick.set_fontname("Times New Roman")
    # rotate, position
    ax.xaxis.set_tick_params(rotation=45,labelsize=18,colors='w')   # rotate
    ax.yaxis.tick_right()           # move tick and ticklabel to right of axis
    # verbose
    ax.minorticks_on()                  # Display minor ticks on the axes.
    ax.minorticks_on()                  # Not display minor ticks on the axes.

# label 
    # space
    ax.set_xlabel('x', fontsize=30, fontname="Times New Roman", labelpad=15, fontweight='bold')
    # color
    ax.yaxis.label.set_color('red')
    ax.xaxis.label.set_color('red')

# title 
    # title:
    csfont = {'fontname':'Times New Roman'}
    ax.set_title('title',**csfont, fontsize=10)
    ax.set_title('title', fontname='Times New Roman', fontsize=10)
    # color
    ax.title.set_color('red')
    # space
    ax.set_title('Title', pad=20)

# legend
    ax.legend(prop={'family': 'Arial'})
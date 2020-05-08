https://zhuanlan.zhihu.com/p/37551786

gif: http://louistiao.me/posts/notebooks/save-matplotlib-animations-as-gifs/
3d plot: https://matplotlib.org/mpl_toolkits/mplot3d/tutorial.html
color map : https://matplotlib.org/tutorials/colors/colormaps.html

# General
    plt.figure(1, figsize=(15,7.5))
    plt.subplot(111)
    plt.title('AAA\n AAA', fontsize = 20)

    plt.scatter(x, y, s = 10, marker=".", color = 'red', label = 'label1')
    plot(x,y2,color='green', marker='o', linestyle='dashed', linewidth=1, markersize=6, label = 'label2')
    plt.legend()                                                        # show label
    plt.legend(loc='upper left', bbox_to_anchor=(0.6,0.95), ncol=3)     # location, location，column number

    plt.xticks(fontsize=20)                                      # Set x label size
    plt.yticks(fontsize=20)                                      # Set x label size
    plt.xticks([])                                              # Cancel x comment
    plt.yticks([])                                              # Cancel y comment
    name = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
    plt.xticks(x,name)  ## 可以设置坐标字
    plt.axis('off')

    plt.xlim(0,4)                                                # Set y range
    plt.ylim(0,4)                                                # Set x range
    plt.xlabel('x (m)')                                          # Set x label content
    plt.ylabel('y (m)')                                          # Set y label content

    plt.vlines(i, 0, 50, colors = "grey", linestyles = "dashed")        # 画直线

    plt.text(5.125,-0.75,'MDN Groundtruth',fontsize=15)

    plt.grid(True)                                  # Turn on the grid
    plt.savefig(image_name)

# create legend according to color
    #用label和color列表生成mpatches.Patch对象，它将作为句柄来生成legend
    import matplotlib.patches as mpatches
    color =  [[234/255,120/255,52/255], [0.2,0.8,0.4]]
    labels = ['Deterministic', 'Probablistic']  #legend标签列表，上面的color即是颜色列表
    patches = [ mpatches.Patch(color=color[i], label="{:s}".format(labels[i]) ) for i in range(len(color)) ] 
    ax=plt.gca()
    ax.legend(handles=patches, loc=1, bbox_to_anchor=(1.008,1.1), ncol=1) #生成legend
    
# class plot
    fig = plt.figure()
    ax = fig.add_subplot(121)
    ax.set_title('style: {!r}'.format(sty), color='C0')

    ax.plot(x,x)
    ax.scatter(x,x)
    ax.legend()

    ax.tick_params(axis="x", labelsize=12)
    ax.tick_params(axis="y", labelsize=12)
    ax.set_xticks([1,4,5]) 
    ax.set_xticklabels([1,4,5], fontsize=12)  
    ax.set_yticks([1,4,5]) 
    ax.set_yticklabels([1,4,5], fontsize=12)  
    ax.axis('off')

    ax.set_xlim(0, 3)
    ax.set_ylim(0, j + 2)
    axes.set_xlabel('x')
    axes.set_ylabel('y')

    plt.show()

# Tricks
fig, axes = plt.subplots(nrows=1, ncols=2)
for ax in axes:
    ax.plot(x, y, 'r')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('title')

# Error Bar
    plt.yticks(fontsize=20)
    plt.errorbar(x, time_mean_all, yerr=time_std_all,fmt='s', marker='s', ms=12, ecolor=[234/255,120/255,52/255],color=[95/255,100/255,255/255],elinewidth=16,capsize=20)

# plot bar
    val_ls = [np.random.randint(100) + i*20 for i in range(7)]
    scale_ls = range(7)
    plt.bar(scale_ls, val_ls)
    index_ls = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
    plt.xticks(scale_ls,index_ls)  ## 可以设置坐标字

# 3d plot scatter
    import matplotlib.pyplot as plt 
    from mpl_toolkits.mplot3d import Axes3D ## 3d plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(data[:,0,0], data[:,0,1], data[:,0], s=2, marker=".")
    plt.show()

# plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
X, Y, Z = axes3d.get_test_data(0.1)
ax.plot_wireframe(X, Y, Z, rstride=5, cstride=5)
ax.view_init(30, angle)                 # set angle, first is along the y axis, second is along z axis
plt.draw()
plt.pause(.001)


# # rotate a 3d figure
    from mpl_toolkits.mplot3d import axes3d
    import matplotlib.pyplot as plt
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    # # load some test data for demonstration and plot a wireframe
    X, Y, Z = axes3d.get_test_data(0.1)
    ax.plot_wireframe(X, Y, Z, rstride=5, cstride=5)
    # # rotate the axes and update
    for angle in range(0, 360):
        ax.view_init(30, angle)
        plt.draw()
        plt.pause(.001)
    '''
    def get_test_data(delta=0.05):

        from matplotlib.mlab import  bivariate_normal
        x = y = np.arange(-3.0, 3.0, delta)
        X, Y = np.meshgrid(x, y)

        Z1 = bivariate_normal(X, Y, 1.0, 1.0, 0.0, 0.0)
        Z2 = bivariate_normal(X, Y, 1.5, 0.5, 1, 1)
        Z = Z2 - Z1

        X = X * 10
        Y = Y * 10
        Z = Z * 500
        return X, Y, Z
    '''

# draw contour
    import matplotlib.pyplot as plt
    import numpy as np
    x = np.arange(-5, 5, 0.1)
    y = np.arange(-5, 5, 0.1)
    xx, yy = np.meshgrid(x, y, sparse=True)
    z = np.sin(xx**2 + yy**2) / (xx**2 + yy**2)
    h = plt.contourf(x,y,z)
    plt.show()




https://zhuanlan.zhihu.com/p/37551786

gif: http://louistiao.me/posts/notebooks/save-matplotlib-animations-as-gifs/
3d plot: https://matplotlib.org/mpl_toolkits/mplot3d/tutorial.html
color map : https://matplotlib.org/tutorials/colors/colormaps.html


# Error Bar
    plt.yticks(fontsize=20)
    plt.errorbar(x, time_mean_all, yerr=time_std_all,fmt='s', marker='s', ms=12, ecolor=[234/255,120/255,52/255],color=[95/255,100/255,255/255],elinewidth=16,capsize=20)

# plot scatter
    import matplotlib.pyplot as plt 
    plt.scatter(data[:,0], data[:,1], s=8, marker=".", color = 'red') # s means size
    plt.show()

# plot skill
    plt.title('TITLE',fontsize='large') 
    plt.subplot(141)                            # set subplot
    plt.xlim(0,4)                               # Set y range
    plt.ylim(0,4)                               # Set x range
    plt.xticks([])                              # Cancel x comment
    plt.yticks([])                              # Cancel y comment
    plt.grid()                                  # Turn on the grid

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

# class plot
    fig = plt.figure()
    ax1 = fig.add_subplot(121)
    ax1.plot(x,x)
    plt.show()


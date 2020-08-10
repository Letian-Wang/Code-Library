https://zhuanlan.zhihu.com/p/37551786

gif: http://louistiao.me/posts/notebooks/save-matplotlib-animations-as-gifs/
3d plot: https://matplotlib.org/mpl_toolkits/mplot3d/tutorial.html
color map : https://matplotlib.org/tutorials/colors/colormaps.html

# plot color block
    https://blog.csdn.net/coder_Gray/article/details/81867639
    def block_heatmap(data, xtick=None, ytick=None, xlabel=None, ylabel=None, title=None, cmap = None):
        '''
        >>>
        import random
        # Generate data
        data = []
        for i in range(8):
            temp = []
            for j in range(5):
                k = random.randint(0,100)
                temp.append(k)
            data.append(temp)
        # labels
        xLabel = ['A','B','C','D','E']
        yLabel = ['1','2','3','4','5']
        title = "Likelihood heatmap"
        # d = block_heatmap(data, xLabel, yLabel, title)
        block_heatmap(data, cmap='Blues')
        '''
        from matplotlib import pyplot as plt
        from matplotlib import cm
        from matplotlib import axes
        x_num = len(data[0])
        y_num = len(data)
        fig = plt.figure(figsize=(0.75*x_num, 0.75*y_num))
        ax = fig.add_subplot(111)
        # set ticks
        if xtick == None: xtick = [str(i+1) for i in range(x_num)]
        if ytick == None: ytick = [str(i) for i in range(y_num,0,-1)]
        ax.set_yticks(range(len(ytick)))
        ax.set_yticklabels(ytick)
        ax.set_xticks(range(len(xtick)))
        ax.set_xticklabels(xtick)
        # set label
        if xlabel != None: ax.set_xlabel(xlabel)
        if ylabel != None: ax.set_ylabel(ylabel)
        # choose cmap
        if cmap == None: cmap = plt.cm.hot_r
        # title
        if title != None: plt.title(title)
        # Draw seperate line
        for i in range(x_num):
            plt.vlines(i+0.5, -0.5, -0.5 + y_num, colors = "grey", linestyles = "solid")        # 画直线
        for i in range(y_num):
            plt.hlines(i+0.5, -0.5, -0.5 + x_num, colors = "grey", linestyles = "solid")        # 画直线
        # Draw
        im = ax.imshow(data, cmap=cmap)
        plt.colorbar(im)
        plt.show()

# plot Color
    color RGB: https://tug.org/pracjourn/2007-4/walden/color.pdf
    color bar: https://www.jianshu.com/p/d97c1d2e274f
    color map: https://matplotlib.org/examples/color/colormaps_reference.html
    x = np.random.rand(100000)
    y = np.random.rand(100000)
    plt.scatter(x,y,c=y,cmap='Wistia')
    plt.colorbar()

# color bar
    ''' match the size of graph '''
    import matplotlib.pyplot as plt
    from mpl_toolkits.axes_grid1 import make_axes_locatable
    import numpy as np
    plt.figure()
    ax = plt.gca()
    im = ax.imshow(np.arange(100).reshape((10,10)))
    # create an axes on the right side of ax. The width of cax will be 5%
    # of ax and the padding between cax and ax will be fixed at 0.05 inch.
    divider = make_axes_locatable(ax)
    cax = divider.append_axes("right", size="5%", pad=0.05)
    plt.colorbar(im, cax=cax)

# Get rgb from cmap with a value
    rgb = tuple(cm.get_cmap(cmap)(x)[np.newaxis, :, :3][0][INDEX])

    from matplotlib import cm
    import numpy as np
    def value_to_rgb_list(value_list, diverge_power, color_map, shift='tail'):
        ''' 
        input: 
            value_list: list of value in any range 
            diverge_power: the larger, the more scattered are the colors
            shift: head, center, tail. where the colors are distributed in colormap
        output: list of rgb in colormap

        >>> scatter_color_list = value_to_rgb_list(cost_list, 2, 'Wistia','center')
        '''
        def normalization(x):
            x = np.array(x)
            temp = x/(x.sum()+0.0000001)
            temp = temp.tolist()
            while( np.array(temp).sum() < 0.999):
                temp = np.array(temp)
                temp = temp/(temp.sum()+0.0000001)
                temp = temp.tolist()
            return temp
        def value_to_rgb(val, cmap_name):
            """ 
                Input：cmap_name, val range: [0,1]
                Rerutn: rgb on that cmap

                >>> value_to_rgb('YlOrBr', 1)
                (0.4, 0.1450980392156863, 0.02352941176470588)
            """
            RGB_Index = int(val * 299)
            x = np.linspace(0.0, 1.0, 300)
            rgb = tuple(cm.get_cmap(cmap_name)(x)[np.newaxis, :, :3][0][RGB_Index])
            return rgb
        def shift_color(val_list, shift='center'):
            ''' shift to be distributed around 0.5 '''
            assert shift in ['head', 'center', 'tail'], "function shift_color(): data are not shifted correctly" 
            CLAMP = lambda x, low, up: min(max(x, low), up) 
            MID = lambda lst:(min(lst) +  max(lst))/2
            mid = MID(val_list)
            if shift == 'center': target = 0.5
            if shift == 'head': target = 0.25
            if shift == 'tail': target = 0.75
            shift = mid - target
            shifted_list=[]
            for val in val_list: shifted_list.append(CLAMP(val - shift, 0, 1)) 
            return shifted_list
        value_list = np.power(np.array(value_list), diverge_power)
        color_list = [i for i in normalization(value_list)]
        color_list = shift_color(color_list, shift)
        print("shift: ",color_list)
        color_rgb_list = []
        for color_value in color_list: color_rgb_list.append(value_to_rgb(color_value, color_map))
        return color_rgb_list

    def value_to_rgb(val, cmap_name):
        """ 
            Input：cmap_name, val range: [0,1]
            Rerutn: rgb on that cmap

            >>> value_to_rgb(1, 'YlOrBr')
            (0.4, 0.1450980392156863, 0.02352941176470588)
        """
        RGB_Index = int(val * 299)
        x = np.linspace(0.0, 1.0, 300)
        rgb = tuple(cm.get_cmap(cmap_name)(x)[np.newaxis, :, :3][0][RGB_Index])
        return rgb
    
    def shift_val(val_list, shift='center'):
        ''' 
            shift to be distributed around 0.25, 0.5, 0.75 
            val_list: values in [0,1]
            shift: head, center, tail. where the colors are distributed in colormap
            >>>  color_list = shift_val(color_list, shift)
        '''
        assert shift in ['head', 'center', 'tail'], "function shift_val(): data are not shifted correctly" 
        CLAMP = lambda x, low, up: min(max(x, low), up) 
        MID = lambda lst:(min(lst) +  max(lst))/2
        mid = MID(val_list)
        if shift == 'center': target = 0.5
        if shift == 'head': target = 0.25
        if shift == 'tail': target = 0.75
        shift = mid - target
        shifted_list=[]
        for val in val_list: shifted_list.append(CLAMP(val - shift, 0, 1)) 
        return shifted_list

    # self defined
    def Cost_to_RGB(color_value):
        ''' Red to Green color '''
        color_value = color_value*2*218
        red = 241-min(color_value,218)
        green = 23+max((color_value-218),0)
        blue = 23
        return (red/255, green/255, blue/255)

# General
    plt.figure(1, figsize=(15,7.5))
    plt.subplot(111)
    plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=0.2, hspace=0.25)

    # 使用familiary Python切片语法指定子图位置和范围：https://zhuanlan.zhihu.com/p/75276939
    # subplot: https://www.zhihu.com/question/21953954
    # plt/ax/fig: https://zhuanlan.zhihu.com/p/93423829
    grid = plt.GridSpec(2, 3, wspace=0.4, hspace=0.3)
    plt.subplot(grid[0, 0])
    plt.subplot(grid[0, 1:])
    plt.subplot(grid[1, :2])
    plt.subplot(grid[1, 2])


    plt.title('AAA\n AAA', fontsize = 20)
    plt.suptitle('AAA \n AAA', fontsize=25)     # super title (main title）

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
    plt.savefig(image_name,dpi=800)

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

# scatter with gradual color
    import matplotlib.pyplot as plt
    cm = plt.cm.get_cmap('RdYlBu')
    xy = range(20)
    z = xy
    sc = plt.scatter(xy, xy, c=z, vmin=0, vmax=20, s=35, cmap=cm)
    plt.colorbar(sc)
    plt.show()

# plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    X, Y, Z = axes3d.get_test_data(0.1)
    ax.plot_wireframe(X, Y, Z, rstride=5, cstride=5)
    ax.view_init(30, angle)                 # set angle, first is along the y axis, second is along z axis
    plt.draw()
    plt.pause(.001)

# plot and not block the code
    plt.show(block=False)
    print("---Plot graph finish---")
    plt.show()

    plt.draw()
    print("---Plot graph finish---")
    plt.show()

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

# plot sphere 
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D
    import numpy as np

    fig = plt.figure(1, figsize=(5.5,5))    
    ax = fig.add_subplot(111, projection='3d')

    u = np.linspace(0, np.pi/2, 100)
    v = np.linspace(0, np.pi/2, 100)
    x = np.outer(np.cos(u), np.sin(v))
    y = np.outer(np.sin(u), np.sin(v))
    z = np.outer(np.ones(np.size(u)), np.cos(v))

    ax.plot_surface(x, y, z, linewidth=0.0, color=(0.8, 0.8, 0.8), cstride=1, rstride=1)
    ax.view_init(45, 45)                 # set angle, first is along the y axis, second is along z axis
    ax.set_xlabel('x-label')
    ax.set_ylabel('y-label')
    ax.set_zlabel('z-label')
    plt.show()
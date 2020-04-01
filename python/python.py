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

# run time
    import datetime
    starttime = datetime.datetime.now()
    #long running
    #do something other
    endtime = datetime.datetime.now()
    print (endtime - starttime).seconds

# remove file and directory
    os.makedirs(dirName)        # Create dir                          
    os.remove()                 # remove a file.=
    os.rmdir()                  # remove an empty directory.
    shutil.rmtree()             # delete a directory and all its contents.


# 3d plot scatter
    import matplotlib.pyplot as plt 
    from mpl_toolkits.mplot3d import Axes3D ## 3d plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(data[:,0,0], data[:,0,1], data[:,0], s=2, marker=".")
    plt.show()

# Dictionary
    thisdict = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }
    print(thisdict)
    print(thisdict["model"])
    for x in thisdict:
        print(thisdict[x])
    for x in thisdict.values():
        print(x)
    for x,y in thisdict.items():
        print(x,y)
# list
    list_a = []
    currentDirectory = os.getcwd()
    with open((os.path.join(currentDirectory, "data.txt")), "r") as filestream:
        for line in filestream:
            currrentline = line.split(' ')
            list_a.append(int(currrentline[0]))

    list = [1,2,4,8]
    for i in list:

    list = ["le","tian","wang"]
    for name in list:

# find the minimum index
    mini_index = res.index(min(res)) 

# numpy basic
    import numpy as np
    a = np.array([[1,2,3],[4,5,6]])
    b = np.ones((1,5)) 
    c = a[0,:]

# load data .mat
    import scipy.io as sio
    file = 'data.mat'
    data = sio.loadmat(file)

# string slice
    PATH = path1 + path2
    PATH = os.path.join(path1, path2)

# Get a specific-line data
import linecache
line_1 = linecache.getline(directory, 2)

# calculate vertical foot
    def footP(p1,p2,p0):
        # vertical foot of the point p0 on the line formed by p1 and p2
        # data structure: p(x,y)
        p12 = p2-p1
        len12 = np.sum(p12**2)
        x = ( p12[0]**2*p0[0] + p1[0]*p12[1]*(p2[1] - p0[1]) + p2[0]*p12[1]*(p0[1]-p1[1]) )/len12
        y = ( p12[1]**2*p0[1] + p1[1]*p12[0]*(p2[0] - p0[0]) + p2[1]*p12[0]*(p0[0]-p1[0]) )/len12
        return np.array((x,y))


# find the closet point of 2 curve
    def closestPoint(curv1,curv2):
        """
        find a closest point in crv1 for every point in crv2
        data structure: 
            curv1, curv2 are (n,2) array
            res is the position. refinds is the index
        """
        matchp = curveMatch(curv1,curv2)
        refinds = matchp[:]
        res = np.zeros_like(curv2)
        for i,p in enumerate(curv2):
            mchi = matchp[i]
            mchp = curv1[mchi]
            resp = curv1[mchi] # result point
            p21 = mchp - p
            # check two foots of the segment beside the matched point
            if(mchi==0):
                resp = footP(curv1[mchi+1],mchp,p) # elongating the first point
            elif(mchi>0 and  p21.dot( curv1[mchi-1] - mchp )<0):
                resp = footP(curv1[mchi-1],mchp,p) # the projection is on the last point
                refinds[i] = mchi - 1
            elif(mchi<len(curv1)-1 and  p21.dot( curv1[mchi+1] - mchp )<0):
                resp = footP(curv1[mchi+1],mchp,p)
            elif(mchi==len(curv1)-1):
                resp = footP(curv1[mchi-1],mchp,p) # elongating the last point
            res[i]= resp 
        return res, refinds

# locally find a closest point in crv1 for every point in crv2
    def curveMatch(crv1,crv2):
        # find a closest point in crv1 for every point in crv2
        # return the a list of index of matched crv1, same length with crv2
        i = 0
        lencrv1 = len(crv1)
        res = [0]*len(crv2)
        for j, p in enumerate(crv2):
            i = res[max(0,j-1)]
            min_dis = distance(crv1[i],p)
            min_ind = i
            while(i<lencrv1-1):
                d = distance(crv1[i+1],p)
                if(d < 2* min_dis):
                    i += 1
                    if( d < min_dis):
                        min_ind = i
                        min_dis = d
                else:
                    break
            res[j] = min_ind
        return res

# globally find a closest point in crv1 for every point in crv2
    def curveMatch_global(crv1,crv2):
        # find a closest point in crv1 for every point in crv2
        # return the a list of index and coresponding distance of matched crv1, same length with crv2
        # data structure: 
        #   crv1 and crv2 are (n,2) array
        #   record: (2,n) list -- min_distance and min_ind

        lencrv2 = len(crv2)
        record = [[0 for i in range(lencrv2)] for j in range(2)]
        for j,p in enumerate(crv2):
            min_dis = distance(crv1[0],p)
            min_ind = 0
            for i,s in enumerate(crv1):
                if distance(s,p) < min_dis :
                    min_dis = distance(s,p)
                    min_ind = i
            record[0][j] = min_dis
            record[1][j] = min_ind

        return record

# get the distance between 2 points
    def distance(a,b):
        """
        euclid distance between two points
        """
        return np.sum((a - b)**2)**0.5
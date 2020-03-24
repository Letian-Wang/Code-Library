# plot scatter
    import matplotlib.pyplot as plt 
    plt.scatter(data[:,0], data[:,1], s=8, marker=".", color = 'red') # s means size
    plt.show()

# run time
    import datetime
    starttime = datetime.datetime.now()
    #long running
    #do something other
    endtime = datetime.datetime.now()
    print (endtime - starttime).seconds


# 3d plot scatter
    import matplotlib.pyplot as plt 
    from mpl_toolkits.mplot3d import Axes3D ## 3d plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(data[:,0,0], data[:,0,1], data[:,0], s=2, marker=".")
    plt.show()

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
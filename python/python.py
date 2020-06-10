# Module
    https://www.runoob.com/python/python-modules.html

# Pass in parameter in terminal
    import argparse
    parser = argparse.ArgumentParser(description='manual to this script')
    parser.add_argument('--gpus', type=str, default = None)
    parser.add_argument('--batch-size', type=int, default=32)
    args = parser.parse_args()
    print args.gpus
    print args.batch_size

    python script.py --bool-val=0 # args.bool_val=True
    python script.py --bool-val=False # args.bool_val=True
    python script.py --bool-val=     # args.bool_val=什么都不写False

# Create variable by name
    variable = locals()["name"]

# unzip and move file
    # extract data
    path_cats_and_dogs = getcwd() + "/cats-and-dogs.zip"
    if not os.path.exists(getcwd() + '/tmp'):
        os.mkdir(getcwd() + '/tmp')
    else:
        shutil.rmtree(getcwd() + '/tmp')
    local_zip = path_cats_and_dogs
    zip_ref = zipfile.ZipFile(local_zip, 'r')
    zip_ref.extractall(getcwd()+'/tmp')
    zip_ref.close()
    print(len(os.listdir('/tmp/PetImages/Cat/')))
    print(len(os.listdir('/tmp/PetImages/Dog/')))

    os.path.getsize()
    shutil.copyfile(origin_file, destination_file)

# csv 
    csv_reader = csv.reader(training_file, delimiter=',')
    next(csv_reader)
    for line in csv_reader:

# JSON
    with open(getcwd() + '/sarcasm.json', 'r') as f:
        datastore = json.load(f)
    sentences = []
    labels = []
    urls = []
    for item in datastore:
        sentences.append(item['headline'])
        labels.append(item['is_sarcastic'])

# print
    print(val, end=" ") # end with " " not "\n"

# Assert
    def double(x):
        assert isinstance(x, int), "The input to double(x) must be an integer"
        return 2 * x

# Doctest, document of function
    def value_to_rgb(cmap_name,Val):
        """ 
            Input：cmap_name, Val range: [0,1]
            Rerutn: rgb on that cmap

            >>> value_to_rgb('YlOrBr', 1)
            (0.4, 0.1450980392156863, 0.02352941176470588)
        """
        RGB_Index = int(Val * 299)
        x = np.linspace(0.0, 1.0, 300)
        rgb = tuple(cm.get_cmap(cmap_name)(x)[np.newaxis, :, :3][0][RGB_Index])
        return rgb
    python3 -m doctest file.py
    print(value_to_rgb.__doc__)

# string
    s = "hello"
    print s.capitalize()  # Capitalize a string; prints "Hello"
    print s.upper()       # Convert a string to uppercase; prints "HELLO"
    print s.rjust(7)      # Right-justify a string, padding with spaces; prints "  hello"
    print s.center(7)     # Center a string, padding with spaces; prints " hello "
    print s.replace('l', '(ell)')  # Replace all instances of one substring with another;
                                # prints "he(ell)(ell)o"
    print '  world '.strip()  # Strip leading and trailing whitespace; prints "world"

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

    # Key with max value dictionary
    key = max(dic.items(), key=operator.itemgetter(1))[0] 
    # max value in dictionary
    max(val_dic.values())
    # sum
    all_sum = sum(dic.values())

# list
    list_a = []
    currentDirectory = os.getcwd()
    with open((os.path.join(currentDirectory, "data.txt")), "r") as filestream:
        for line in filestream:
            currrentline = line.split(' ')
            list_a.append(int(currrentline[0]))

    list = [1,2,4,8]

    # two dimension list
    list = [[0 for i in range(9)] for j in range(5)]        
    # max in list
    max(list)
    List.index(max(List))
    
    for i in list:

    list = ["le","tian","wang"]
    for name in list:

# find the minimum index in a list
    mini_index = res.index(min(res)) 

# numpy basic
    import numpy as np
    a = np.array([[1,2,3],[4,5,6]])
    b = np.ones((1,5)) 
    c = a[0,:]

    a = np.zeros((2,2))  # Create an array of all zeros
    print a              # Prints "[[ 0.  0.]
                        #          [ 0.  0.]]"

    b = np.ones((1,2))   # Create an array of all ones
    print b              # Prints "[[ 1.  1.]]"

    c = np.full((2,2), 7) # Create a constant array
    print c               # Prints "[[ 7.  7.]
                        #          [ 7.  7.]]"

    d = np.eye(2)        # Create a 2x2 identity matrix
    print d              # Prints "[[ 1.  0.]
                        #          [ 0.  1.]]"

    e = np.random.random((2,2)) # Create an array filled with random values
    print e                     # Might print "[[ 0.91940167  0.08143941]
                                #               [ 0.68744134  0.87236687]]"

 # 整型数组访问：
    a = np.array([[1,2], [3, 4], [5, 6]])
    # An example of integer array indexing.
    # The returned array will have shape (3,) and 
    print a[[0, 1, 2], [0, 1, 0]]  # Prints "[1 4 5]"


 # 布尔型数组访问：
    a = np.array([[1,2], [3, 4], [5, 6]])

    bool_idx = (a > 2)  # Find the elements of a that are bigger than 2;
                        # this returns a numpy array of Booleans of the same
                        # shape as a, where each slot of bool_idx tells
                        # whether that element of a is > 2.

    print bool_idx      # Prints "[[False False]
                        #          [ True  True]
                        #          [ True  True]]"

    # We use boolean array indexing to construct a rank 1 array
    # consisting of the elements of a corresponding to the True values
    # of bool_idx
    print a[bool_idx]  # Prints "[3 4 5 6]"

    # We can do all of the above in a single concise statement:
    print a[a > 2]     # Prints "[3 4 5 6]"

 # 数组计算
    import numpy as np

    x = np.array([[1,2],[3,4]], dtype=np.float64)
    y = np.array([[5,6],[7,8]], dtype=np.float64)

    # Elementwise sum; both produce the array
    # [[ 6.0  8.0]
    #  [10.0 12.0]]
    print x + y
    print np.add(x, y)

    # Elementwise difference; both produce the array
    # [[-4.0 -4.0]
    #  [-4.0 -4.0]]
    print x - y
    print np.subtract(x, y)

    # Elementwise product; both produce the array
    # [[ 5.0 12.0]
    #  [21.0 32.0]]
    print x * y
    print np.multiply(x, y)

    # Elementwise division; both produce the array
    # [[ 0.2         0.33333333]
    #  [ 0.42857143  0.5       ]]
    print x / y
    print np.divide(x, y)

    # Elementwise square root; produces the array
    # [[ 1.          1.41421356]
    #  [ 1.73205081  2.        ]]
    print np.sqrt(x)

    # 点乘
    x = np.array([[1,2],[3,4]])
    y = np.array([[5,6],[7,8]])

    v = np.array([9,10])
    w = np.array([11, 12])

    # Inner product of vectors; both produce 219
    print v.dot(w)
    print np.dot(v, w)

    # Matrix / vector product; both produce the rank 1 array [29 67]
    print x.dot(v)
    print np.dot(x, v)

    # Matrix / matrix product; both produce the rank 2 array
    # [[19 22]
    #  [43 50]]
    print x.dot(y)
    print np.dot(x, y)

    # 求和
    x = np.array([[1,2],[3,4]])
    print np.sum(x)  # Compute sum of all elements; prints "10"
    print np.sum(x, axis=0)  # Compute sum of each column; prints "[4 6]"
    print np.sum(x, axis=1)  # Compute sum of each row; prints "[3 7]"

 # broadcast
    # Compute outer product of vectors
    v = np.array([1,2,3])  # v has shape (3,)
    w = np.array([4,5])    # w has shape (2,)
    # To compute an outer product, we first reshape v to be a column
    # vector of shape (3, 1); we can then broadcast it against w to yield
    # an output of shape (3, 2), which is the outer product of v and w:
    # [[ 4  5]
    #  [ 8 10]
    #  [12 15]]
    print np.reshape(v, (3, 1)) * w

    # Add a vector to each row of a matrix
    x = np.array([[1,2,3], [4,5,6]])
    # x has shape (2, 3) and v has shape (3,) so they broadcast to (2, 3),
    # giving the following matrix:
    # [[2 4 6]
    #  [5 7 9]]
    print x + v

    # Add a vector to each column of a matrix
    # x has shape (2, 3) and w has shape (2,).
    # If we transpose x then it has shape (3, 2) and can be broadcast
    # against w to yield a result of shape (3, 2); transposing this result
    # yields the final result of shape (2, 3) which is the matrix x with
    # the vector w added to each column. Gives the following matrix:
    # [[ 5  6  7]
    #  [ 9 10 11]]
    print (x.T + w).T

    # Another solution is to reshape w to be a row vector of shape (2, 1);
    # we can then broadcast it directly against x to produce the same
    # output.
    print x + np.reshape(w, (2, 1))

    # Multiply a matrix by a constant:
    # x has shape (2, 3). Numpy treats scalars as arrays of shape ();
    # these can be broadcast together to shape (2, 3), producing the
    # following array:
    # [[ 2  4  6]
    #  [ 8 10 12]]
    print x * 2

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

# little function:
    CLAMP = lambda x, low, up: min(max(x, low), up) 
    MID = lambda lst:(min(lst) +  max(lst))/2
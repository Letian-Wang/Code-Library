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
        def distance(a,b):
            """
            euclid distance between two points
            """
            return np.sum((a - b)**2)**0.5

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

# globally find a closest element in lst1 for every element in lst2
    def LstMatch_global(lst1,lst2):
        # find a closest element in lst1 for every element in lst2
        # return the a list of index and coresponding error of matched lst1, same length with lst2
        # data structure: 
        #   lst1 and lst2 are (n,1) array
        #   record: (2,n) list -- min_error and min_ind
        lenlst2 = len(lst2)
        record = [[0 for i in range(lenlst2)] for j in range(2)]
        for j,p in enumerate(lst2):
            min_error = abs(lst1[0] - p)
            min_ind = 0
            for i,s in enumerate(lst1):
                if abs(s - p) < min_error :
                    min_error = abs(s - p)
                    min_ind = i
            record[0][j] = min_error
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

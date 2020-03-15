import os
currentDirectory = os.getcwd()
#os.chdir('/home/varun')
wb.save(os.path.join(currentDirectory, "lt", "pass","cost.xls"))

# path
directory = os.path.dirname(__file__) + "/dir2/file.txt"

# splice string
a = 1
ego_file_name = 'ego_%d.txt' % a            # % is the occupation string, 
                                            # %s : string   %d : int    %f : float

# create directory
if not os.path.exists(dirName):
    os.mkdir(dirName)
    print("Directory " , dirName ,  " Created ")
else:    
    print("Directory " , dirName ,  " already exists")          

# Create target directory & all intermediate directories if don't exists
dirName = 'tempDir2/temp2/temp' 
os.makedirs(dirName)                         

# Use string to create variable
var = "This is a string"
varName = 'var'
s= locals()[varName]


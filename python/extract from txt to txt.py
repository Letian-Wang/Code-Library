import os
from xlwt import Workbook 
import string

currentDirectory = os.getcwd()
#os.chdir('/home/varun')
substr = "time"
# read comma-separated values from txt file and write to txt
    with open((os.path.join(currentDirectory, "vehicle_data.txt")), "r") as filestream:
        with open("vehicle_data2.txt", "w") as filestreamtwo:     # replace "w" with "a+"
            for line in filestream:
                if line.find(substr) != -1:
                    continue
                currentline = line.split(",")
                filestreamtwo.write(currentline[4])
                filestreamtwo.write(',')
                filestreamtwo.write(currentline[5])
                filestreamtwo.write('\n')




# extract data from an unknown-length txt including (n,2) array
    currentDirectory = os.getcwd()
    obstacle_ref_lenth = 0
    # get length
    with open((os.path.join(currentDirectory, file_name)), "r") as filestream:
        for line in filestream:
            lenth += 1
    data = np.zeros((lenth,2))
    # Give the value to data
    j = 0
    with open((os.path.join(currentDirectory, file_name)), "r") as filestream:
        for line in filestream:
            line = line.split(',')
            data[j,0] = line[0]
            data[j,1] = line[1]
            j += 1
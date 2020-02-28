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

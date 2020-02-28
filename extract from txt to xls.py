import os
from xlwt import Workbook 
import string

currentDirectory = os.getcwd()
#os.chdir('/home/varun')
global flag
flag = 0
wb = Workbook()
sheet1 = wb.add_sheet('Speed')
sheet1.write(0,0, "Ego speed")
sheet1.write(0,1, "Decsion Speed")
i = 1
with open ((os.path.join(currentDirectory, "lt", "yield","log.txt")),'rt') as myfile:
    substr = "current_speed"
    substr2 = "@@@@end speed:"
    for line in myfile:
        if line.find(substr) != -1:
            speed = line[13:]
            print("curent speed: ", speed)
            flag = 1
            sheet1.write(i,0,float(speed))


        if line.find(substr2) != -1 and flag == 1:
            decision = line[16:]
            print("decision: ", decision)
            flag = 0
            sheet1.write(i,1,float(decision))
            i += 1
wb.save(os.path.join(currentDirectory, "lt", "yield","speed.xls"))
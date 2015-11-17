import os 
import numpy as np

def getPID():
    os.system("qstat > qstat.temp")
    qstat = open("qstat.temp","r")
    qstatString = qstat.readlines()
    print qstatString[0]
    PID=[] 
    for line in qstatString:
        lineSplit=line.split()
        PID.append(lineSplit[0])
    print PID
    print os.system("qstat | awk ' {print $1}' ")

    for i in len(PID):
        print float(PID[i])

def trackMemory(pid):
    for id in pid:
        os.system("qstat -j "+str(id[0])+" >> temp.info")
        memInfo=open("temp.info", "r").read()
        ''' well you need to now go through the memInfo string
                find the memory info and then write this to a file... then wait for 5 mins'''


if __name__=="__main__":
    
    getPID()



        



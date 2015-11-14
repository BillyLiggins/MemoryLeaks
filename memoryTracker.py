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


    print float(PID[3])



if __name__=="__main__":
    
    getPID()

import time
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
    
    print PID[2:]
    return PID[2:]


def trackMemory(pid,memoryDatefile,timestep):
    for i in pid:
        memoryDatefile.write(i+"\t")
    memoryDatefile.write("\n")
    while True:
        for id in pid:
            os.system("qstat -j "+str(id)+" > temp.info")
            memInfo=open("temp.info", "r")
            with open('temp.info') as f:
               for line in f:
                    if "maxvmem" in line:
                        print line.split()[7][8:-1]
                        tempVar=line.split()[7][8:-1]
                        memoryDatefile.write(tempVar+"\t")
                                        
                    if 'str' in line:
                            break
        memoryDatefile.write("\n")
        memoryDatefile.flush()
        time.sleep(timestep)


if __name__=="__main__":
    
    pid=getPID()
    print "len of PID ", len(pid)
    memoryDatefile=open("memoryData.dat","w")
    trackMemory(pid,memoryDatefile,30)
    memoryDatefile.close()


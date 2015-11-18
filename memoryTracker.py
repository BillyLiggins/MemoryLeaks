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


def trackMemory(pid):
    for id in pid:
        #print id
        os.system("qstat -j "+str(id)+" > temp.info")
        memInfo=open("temp.info", "r")
        with open('temp.info') as f:
           for line in f:
                if "maxvmem" in line:
                    print line.split()[7][8:-1]
                                    
                if 'str' in line:
                        break
        #print memInfo
        ''' well you need to now go through the memInfo string
                find the memory info and then write this to a file... then wait for 5 mins'''
        print "You have finished the loop"
if __name__=="__main__":
    
    pid=getPID()
    print "len of PID ", len(pid)
    trackMemory(pid)

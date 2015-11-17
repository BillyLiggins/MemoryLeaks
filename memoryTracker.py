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
    #print os.system("qstat | awk ' {print $1}' ")

#    for i in PID:
#        #print float(PID)
#        print "the is the elememnt " ,i
    
    return PID[2:]


def trackMemory(pid):
    for id in pid:
        print id
        os.system("qstat -j "+str(id)+" > temp.info")
        memInfo=open("temp.info", "r").read()
        print memInfo
        ''' well you need to now go through the memInfo string
                find the memory info and then write this to a file... then wait for 5 mins'''
        print "You have finished the loop"

if __name__=="__main__":
    
    pid=getPID()
    print "len of PID ", len(pid)
    trackMemory(pid)



        



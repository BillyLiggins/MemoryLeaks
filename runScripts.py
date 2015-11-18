import numpy as np

import os 
import glob

seedList= np.random.randint(40000000, size=10)


for i in seedList:
	inFile = open('script/templateScript.scr', 'r')
	outFile = open('script/freija_'+str(i)+'.scr', 'w')
	
	
	inFileStr=inFile.read()

	inFileStr=inFileStr.replace("rat -l /data/liggins/Myjob.log /data/liggins/SimpleBatch/mac/Myjob.mac","rat -s "+str(i)+" -l /data/snoplus/liggins/year1/memoryLeaks/logs/freija_"+str(i)+".log /data/snoplus/liggins/year1/memoryLeaks/macs/FRscript.mac") # This is the standard line 
#       inFileStr=inFileStr.replace("rat -l /data/liggins/Myjob.log /data/liggins/SimpleBatch/mac/Myjob.mac","rat -s "+str(i)+" -l /data/snoplus/liggins/year1/memoryLeaks/logs/freija_"+str(i)+"_with_Jacks_mod.log /data/snoplus/liggins/year1/memoryLeaks/macs/FRscript.mac") # This is the line with Jack's mod

	outFile.write(inFileStr)

	inFile.close()
	outFile.close() 
	
	
 	os.system("qsub -cwd -q snoplusSL6 script/freija_"+str(i)+".scr")
	os.system("rm script/freija_"+str(i)+".scr")


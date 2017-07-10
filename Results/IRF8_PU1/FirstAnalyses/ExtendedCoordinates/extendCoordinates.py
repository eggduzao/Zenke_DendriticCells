
# Import
import os
import sys

totalExt = 60
inputLocation = "/home/egg/work/eg474423/ig440396_dendriticcells/exp/diffpeak/res/peakstatsnew/pu1_IRF8/"
outputLocation = "/home/egg/work/eg474423/eg474423_Projects/trunk/DendriticCells/IRF8_MotifStatistics_Scripts/Input/"
inList = ["CDP_PU1_IRF8.bed", "CDP_m_PU1_IRF8.bed", "CDP_PU1_m_IRF8.bed", "cDC_PU1_IRF8.bed", "cDC_m_PU1_IRF8.bed", 
          "cDC_PU1_m_IRF8.bed", "pDC_PU1_IRF8.bed", "pDC_m_PU1_IRF8.bed", "pDC_PU1_m_IRF8.bed"]

outputLocation = outputLocation+"coord_ext_"+str(totalExt)+"/"
os.system("mkdir -p "+outputLocation)
for inputFileName in inList:
    inputFile = open(inputLocation+inputFileName,"r")
    outputFileName = outputLocation + inputFileName
    outputFile = open(outputFileName,"w")
    for line in inputFile:
        ll = line.strip().split("\t")
        mid = (int(ll[1])+int(ll[2]))/2
        p1 = str(mid-(totalExt/2))
        p2 = str(mid+(totalExt/2)+1)
        outputFile.write("\t".join([ll[0],p1,p2])+"\n")
    inputFile.close()
    outputFile.close()



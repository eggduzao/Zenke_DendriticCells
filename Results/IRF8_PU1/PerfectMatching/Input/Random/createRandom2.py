
# Import
import os
import sys
import random

# Input
rep = 2
inputfileName = "/work/eg474423/eg474423_Projects/trunk/DendriticCells/PerfectMatching/Input/Coordinates/irf8_dup_summits_500_4.bed"
outputFileName = "/work/eg474423/eg474423_Projects/trunk/DendriticCells/PerfectMatching/Input/Random/random.bed"

# Reading chromosome sizes
csFile = open("/hpcwork/izkf/projects/egg/Data/MM9/mm9.chrom.sizes","r")
csDict = dict()
for line in csFile:
    ll = line.strip().split("\t")
    csDict[ll[0]] = int(ll[1])
csFile.close()

# Creating random set
inFile = open(inputfileName,"r")
outFile = open(outputFileName,"w")
for line in inFile:
    ll = line.strip().split("\t")
    chrName = ll[0]; width = int(ll[2])-int(ll[1])
    for i in range(0,rep):
        r = random.randint(0,csDict[chrName]-(10*width))
        outFile.write("\t".join([chrName,str(r),str(r+width)])+"\n")
inFile.close()
outFile.close()



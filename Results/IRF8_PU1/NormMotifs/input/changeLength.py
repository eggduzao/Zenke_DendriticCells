import os
import sys
from glob import glob
ext = 100
inLoc = "/work/eg474423/eg474423_Projects/trunk/DendriticCells/Results/IRF8_PU1_NormMotifs/input/"
for inFileName in glob(inLoc+"500/*.bed"):
  inName = inFileName.split("/")[-1]
  outFileName = inLoc+str(ext)+"/"+inName
  inFile = open(inFileName,"r")
  outFile = open(outFileName,"w")
  for line in inFile:
    ll = line.strip().split("\t")
    mid = (int(ll[1])+int(ll[2]))/2
    outFile.write("\t".join([ll[0],str(mid-(ext/2)),str(1+mid+(ext/2))])+"\n")
  inFile.close()
  outFile.close()



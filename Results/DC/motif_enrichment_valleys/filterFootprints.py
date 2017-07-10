
# Import
import os
import sys
from glob import glob

# Input
extList = [500,1000]
il="/work/eg474423/eg474423_Projects/trunk/DendriticCells/Results/DC/motif_enrichment_valleys/input/"
inList = glob(il+"*_valleys.bed") + glob(il+"*_PU1.bed")

for inFileName in inList:
  inName = inFileName.split("/")[-1].split(".")[0]
  for ext in extList:
    outFileName = il+inName+"_ext"+str(ext)+".bed"
    outFile = open(outFileName,"w")
    inFile = open(inFileName,"r")
    for line in inFile:
      ll = line.strip().split("\t")
      if((int(ll[2]) - int(ll[1])) > 500): 
        m = (int(ll[1]) + int(ll[2])) / 2
        outFile.write("\t".join([ll[0],str(m-ext/2),str(m+ext/2)])+"\n")
      else: outFile.write("\t".join(ll[0:3])+"\n")
    inFile.close()
    outFile.close()



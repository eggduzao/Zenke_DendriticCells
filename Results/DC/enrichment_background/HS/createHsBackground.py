# Protocol:
# 1. Extend all peaks to 500 bp from the center (no summit information was made available).
# 2. Remove chrY and chrM.
# 3. Sort all peaks.
# 4. Merge all peaks.

# Import
import os
import sys
from glob import glob

# Input
il="/home/egg/Projects/DendriticCells/Results/DC/enrichment_background/HS/"
inFileList = glob(il+"dnase_psu/*.narrowPeak")+glob(il+"dnase_uw/*.narrowPeak")

# Initializations
outputFileName = "HS_background.bed"
to_remove = []
chr_removed = ["chrY","chrM"]

# Extend to 500 bp and remove chrY and chrM
extFileName = il+outputFileName+"_ext.bed"
to_remove.append(extFileName)
outputFile = open(extFileName,"w")
for inFileName in inFileList:
  inFile = open(inFileName,"r")
  for line in inFile:
    ll = line.strip().split("\t")
    if(ll[0] in chr_removed): continue
    p1 = int(ll[1]); p2 = int(ll[2])
    mid = (p1+p2)/2
    outputFile.write("\t".join([ll[0],str(mid-250),str(mid+250)])+"\n")
  inFile.close()
outputFile.close()

# Sort peaks
sorFileName = il+outputFileName+"_sort.bed"
to_remove.append(sorFileName)
os.system("sort -k1,1 -k2,2n "+extFileName+" > "+sorFileName)

# Merge peaks
mergeFileName = il+outputFileName
os.system("mergeBed -i "+sorFileName+" > "+mergeFileName)

# Termination
for e in to_remove: os.system("rm "+e)




# Import
import os
import sys

# Input
inLoc = "/work/eg474423/eg474423_Projects/trunk/DendriticCells/Results/DC/enrichment_background/filtered_random/result/"
inFileName = "/work/eg474423/eg474423_Projects/trunk/DendriticCells/Results/DC/enrichment_background/filtered_random/random_regions_annotated.bed"
outFileName = "/work/eg474423/eg474423_Projects/trunk/DendriticCells/Results/DC/enrichment_background/filtered_random/random_regions_filtered.bed"

# Parameters
topN = 30 # It will remove the top N %
cpgWeight = 499
mapWeight = 499
blackWeight = 2

# Merging files
#os.system("cat "+inLoc+"*.bed > "+inFileName)

# Fetching values
valueList = [[],[],[]]
inFile = open(inFileName,"r")
for line in inFile:
  ll = line.strip().split("\t")
  valueList[0].append(float(ll[3]))
  valueList[1].append(float(ll[4]))
  valueList[2].append(float(ll[5]))
inFile.close()

# Standardizing values
maxList = [max(e) for e in valueList]
minList = [min(e) for e in valueList]
inFile = open(inFileName,"r")
outFileNameT = outFileName+"_t.bed"
to_remove = [outFileNameT]
outFile = open(outFileNameT,"w")
c = 0
for line in inFile:
  ll = line.strip().split("\t")
  s1 = (valueList[0][c] - minList[0])/(maxList[0] - minList[0])
  s2 = (valueList[1][c] - minList[1])/(maxList[1] - minList[1])
  s3 = (valueList[2][c] - minList[2])/(maxList[2] - minList[2])
  ssum = (s1*cpgWeight)+(s2*mapWeight)+(s3*blackWeight)
  outFile.write("\t".join(ll[:3]+[str(e) for e in [s1,s2,s3,ssum]])+"\n")
  c += 1
inFile.close()
outFile.close()

# Sorting and trimming
totalLines = sum(1 for line in open(outFileNameT))
nlines = str(int(float(totalLines) * (float(100-topN)/100.0)))
sFileName = "./s.bed"; to_remove.append(sFileName)
hFileName = "./h.bed"; to_remove.append(hFileName)
cFileName = "./c.bed"; to_remove.append(cFileName)
os.system("sort -k7,7g "+outFileNameT+" > "+sFileName)
os.system("head -n "+nlines+" "+sFileName+" > "+hFileName)
os.system("cut -f 1,2,3 "+hFileName+" > "+cFileName)
os.system("sort -k1,1 -k2,2n "+cFileName+" > "+outFileName)

# Termination
for e in to_remove: os.system("rm "+e)



import os
import sys
r = 1000000
csFile = open("/hpcwork/izkf/projects/TfbsPrediction/Data/MM9/mm9.chrom.sizes","r")
csDict = dict()
for line in csFile:
  ll = line.strip().split("\t")
  csDict[ll[0]] = int(ll[1])
csFile.close()
chrList = sorted(csDict.keys())
outFileName = "./tiled_genome.bed"
outFile = open(outFileName,"w")
for chrName in chrList:
  for i in range(0,csDict[chrName],r):
    outFile.write("\t".join([chrName,str(i),str(min(i+r,csDict[chrName]))])+"\n")
outFile.close()



import os
import sys
from glob import glob
inFileList = glob("./*.txt")
for inFileName in inFileList:
  resMat = [[],[],[],[]]
  inFile = open(inFileName,"r")
  for line in inFile:
    if(line[0] == ">"): continue
    ll = line.strip().split("\t")
    for i in range(0,len(ll)): resMat[i].append(ll[i])
  inFile.close()
  outFileName = inFileName[:-3]+"pwm"
  outFile = open(outFileName,"w")
  for e in resMat: outFile.write(" ".join(e)+"\n")
  outFile.close()



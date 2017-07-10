#################################################################################################
# Separates perfectMatching results in tables.
#################################################################################################
params = []
params.append("###")
params.append("Input: ")
params.append("    1. inputLocation = Location with the results of perfectMatching.")
params.append("    2. outputLocation = Location of the output and temporary files.")
params.append("###")
params.append("Output: ")
params.append("    1. Tables in text format.")
params.append("###")
#################################################################################################

# Import
import os
import sys
import glob
if(len(sys.argv) <= 1): 
    for e in params: print e
    sys.exit(0)

# Parameters
outNames = ["NumberMotifs","NumberPeaks","PropPeaks"]

# Reading input
inputLocation = sys.argv[1]
outputLocation = sys.argv[2]
if(outputLocation[-1] != "/"): outputLocation+="/"

# Iterating on conditions to create tables
table = dict()
for inFileName in glob.glob(inputLocation+"*.txt"):
    if("_EA.txt" in inFileName): continue
    inName = inFileName.split("/")[-1].split(".")[0]
    table[inName] = dict()
    inFile = open(inFileName,"r")
    for line in inFile:
        ll = line.strip().split("\t")
        table[inName][ll[0]] = ll[1:]
    inFile.close()

# Getting keys
condKeys = table.keys()
print table
condKeys.sort()
motifKeys = table[condKeys[0]].keys()
motifKeys.sort()

# Writing table
for i in range(0,len(outNames)):
    outputFile = open(outputLocation+outNames[i]+".txt","w")
    outputFile.write("\t".join(["Motif"]+condKeys)+"\n")
    for m in motifKeys: outputFile.write("\t".join([m]+[table[c][m][i] for c in condKeys])+"\n")
    outputFile.close()



#################################################################################################
# Performs pairwise perfect matching given a set of input motifs / bed coordinates and genome.
#################################################################################################
params = []
params.append("###")
params.append("Input: ")
params.append("    1. spacerList = Spacer list separated by comma. Eg. 1,2,3")
params.append("    2. motifInputFileName = Motif input file with all motifs.")
params.append("    3. coordinateFileName = Locations to apply the perfect matching.")
params.append("    4. randomFileName = Random locations to perform enrichment.")
params.append("    5. genomeFileName = Genome file in UCSC format.")
params.append("    6. outputLocation = Location of the output and temporary files.")
params.append("###")
params.append("Output: ")
params.append("    1. A list of bed files with all individual / pairwise perfect matches.")
params.append("###")
#################################################################################################

# Import
import os
import re
import sys
import operator
from fisher import pvalue
import statsmodels.sandbox.stats.multicomp as sm
if(len(sys.argv) <= 1): 
    for e in params: print e
    sys.exit(0)

# Reading input
spacerList = sys.argv[1].split(",")
motifInputFileName = sys.argv[2]
coordinateFileName = sys.argv[3]
randomFileName = sys.argv[4]
genomeFileName = sys.argv[5]
outputLocation = sys.argv[6]
if(outputLocation[-1] != "/"): outputLocation+="/"

# Parameters
multipleAlpha = 0.05
compDict = dict([("A","T"),("T","A"),("C","G"),("G","C")])

# Calculate reverse complement
def revComp(m):
    return "".join([compDict[e] for e in m[::-1]])

############################################################################
# Creating Motif Dictionary
############################################################################

# All motifs will be stored in a dictionary with a specific label for each combination
motifDictTemp = dict() # Individual motifs
motifDict = dict() # All motifs

# Reading motifs and inserting individual entries
motifFile = open(motifInputFileName,"r")
for line in motifFile:
    m = line.strip().upper(); mr = "".join(m[::-1])
    motifDictTemp[m] = [m,revComp(m)]; motifDictTemp[mr] = [mr,revComp(mr)]
    motifDict[m] = [m,revComp(m)]; motifDict[mr] = [mr,revComp(mr)]
motifFile.close()

# Creating motif combinations
minS = str(min([int(e) for e in spacerList]))
maxS = str(max([int(e) for e in spacerList]))
for k1 in motifDictTemp.keys():
    for k2 in motifDictTemp.keys():
        for s in spacerList:
            regular = k1+".{"+s+"}"+k2
            revcomp = revComp(k2)+".{"+s+"}"+revComp(k1)
            motifDict[k1+("N"*int(s))+k2] = [regular,revcomp]
        regular = k1+".{"+minS+","+maxS+"}"+k2
        revcomp = revComp(k2)+".{"+minS+","+maxS+"}"+revComp(k1)
        motifDict[k1+"_"+k2] = [regular,revcomp]

############################################################################
# Fetching Genomic Sequences
############################################################################

# Fetching sequences using fastaFromBed
coordName = coordinateFileName.split("/")[-1].split(".")[0]
seqFileName = outputLocation+coordName+"_tempcoord.bed"
os.system("fastaFromBed -tab -fi "+genomeFileName+" -bed "+coordinateFileName+" -fo "+seqFileName)
randFileName = outputLocation+coordName+"_temprand.bed"
os.system("fastaFromBed -tab -fi "+genomeFileName+" -bed "+randomFileName+" -fo "+randFileName)

# Reading sequences
seqList = []
seqFile = open(seqFileName,"r")
for line in seqFile:
    ll = line.strip().split("\t")
    seqList.append([ll[0].split(":")[0],int(ll[0].split(":")[1].split("-")[0]),ll[1].upper()])
seqFile.close()
totalSeq = len(seqList)

# Reading random set
randList = []
randFile = open(randFileName,"r")
for line in randFile:
    ll = line.strip().split("\t")
    randList.append([ll[0].split(":")[0],int(ll[0].split(":")[1].split("-")[0]),ll[1].upper()])
randFile.close()
totalRand = len(randList)

# Removing temp file
os.system("rm "+seqFileName)
os.system("rm "+randFileName)

############################################################################
# Performing and Writing Matching
############################################################################

# Statistics = MotifName -> [# MPBS, # Peaks with at least 1 motif, % Peaks with at least 1 motif]
statsDict = dict()
# randDict = MotifName -> [pValue, corrected pValue, a(coord+motif), b(coord-motif), c(rand+motif), d(rand-motif), a/(a+b), c/(c+d)]
randDict = dict()

# Creating output files
outputMotifFile = open(outputLocation+coordName+".bed","w")
outputStatsFile = open(outputLocation+coordName+".txt","w")
outputEnrichFile = open(outputLocation+coordName+"_EA.txt","w")

# Iterating on motifs
for k in motifDict.keys():

    # Statistics
    motifCounter = 0; motifCounterRand = 0
    peakCounter = 0; peakCounterRand = 0

    # Iterating on sequence/coordinates
    for coord in seqList:
        chrName = coord[0]; p1 = coord[1]; seq = coord[2]
        foundMotif = False
        for m in re.finditer(motifDict[k][0],seq):
            outputMotifFile.write("\t".join([chrName,str(p1+m.start()),str(p1+m.end()),k,"1000","+"])+"\n")
            motifCounter += 1
            foundMotif = True
        for m in re.finditer(motifDict[k][1],seq):
            outputMotifFile.write("\t".join([chrName,str(p1+m.start()),str(p1+m.end()),k,"1000","-"])+"\n")
            motifCounter += 1
            foundMotif = True
        if(foundMotif): peakCounter += 1

    # Iterating on random set
    for coord in randList:
        chrName = coord[0]; p1 = coord[1]; seq = coord[2]
        foundMotif = False
        for m in re.finditer(motifDict[k][0],seq):
            motifCounterRand += 1
            foundMotif = True
        for m in re.finditer(motifDict[k][1],seq):
            motifCounterRand += 1
            foundMotif = True
        if(foundMotif): peakCounterRand += 1

    # Updating statistics
    statsDict[k] = [str(motifCounter),str(peakCounter),str(round((float(peakCounter)*100)/totalSeq,2))]
    a = peakCounter; b = totalSeq-peakCounter; c = peakCounterRand; d = totalRand-peakCounterRand
    pValue = pvalue(a,b,c,d)
    randDict[k] = [pValue.right_tail,1.0,a,b,c,d,round((float(a)*100)/totalSeq,4),round((float(c)*100)/totalRand,4)]

# Creating fixed list of motif keys
kList = statsDict.keys()
kList.sort()

# Correct pValues
#[h,pc,a,b] = sm.multipletests([randDict[k][0] for k in kList], alpha=multipleAlpha, returnsorted=False)
counter = 0
for k in kList:
    randDict[k][1] = randDict[k][0] # pc[counter]
    counter += 1

# Writing statistics and 
for k in kList: outputStatsFile.write("\t".join([k]+statsDict[k])+"\n")

# Sorting and writing enrichment analysis
eaTable = []
for k in kList: eaTable.append([k]+randDict[k])
eaTable = sorted(eaTable,key=operator.itemgetter(1))
eaTable = sorted(eaTable,key=operator.itemgetter(2))
for vec in eaTable: outputEnrichFile.write("\t".join([str(e) for e in vec])+"\n")

# Termination
outputMotifFile.close()
outputStatsFile.close()
outputEnrichFile.close()



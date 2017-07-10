
# Import
import os
import sys

# Input
inLoc = "/work/eg474423/eg474423_Projects/trunk/DendriticCells/Results/DC/enrichment_background/filtered_random/result/"
inFileName = "/work/eg474423/eg474423_Projects/trunk/DendriticCells/Results/DC/enrichment_background/filtered_random/random_regions_annotated.bed"
outFileName = "/work/eg474423/eg474423_Projects/trunk/DendriticCells/Results/DC/enrichment_background/filtered_random/random_regions_filtered.bed"

# Parameters
totalLines = sum(1 for line in open(inFileName))
topN_cpg = str(int(float(totalLines) * (float(100-20)/100.0)))
topN_map = str(int(float(totalLines) * (float(100-40)/100.0)))
topN_black = str(int(float(totalLines) * (float(100-41)/100.0)))

# Temp File Names
to_remove = []
aFileName = "./a.bed"; to_remove.append(aFileName)
bFileName = "./b.bed"; to_remove.append(bFileName)
cFileName = "./c.bed"; to_remove.append(cFileName)
dFileName = "./d.bed"; to_remove.append(dFileName)
eFileName = "./e.bed"; to_remove.append(eFileName)
fFileName = "./f.bed"; to_remove.append(fFileName)
gFileName = "./g.bed"; to_remove.append(gFileName)

# Cut cpg
os.system("sort -k4,4gr "+inFileName+" > "+aFileName)
os.system("head -n "+topN_cpg+" "+aFileName+" > "+bFileName)

# Cut map
os.system("sort -k5,5g "+bFileName+" > "+cFileName)
os.system("head -n "+topN_map+" "+cFileName+" > "+dFileName)

# Cut black
os.system("sort -k6,6g "+dFileName+" > "+eFileName)
os.system("head -n "+topN_black+" "+eFileName+" > "+fFileName)

# Termination
os.system("cut -f 1,2,3 "+fFileName+" > "+gFileName)
#os.system("cut -f 1,2,3,4,5,6 "+fFileName+" > "+gFileName)
os.system("sort -k1,1 -k2,2n "+gFileName+" > "+outFileName)
for e in to_remove: os.system("rm "+e)



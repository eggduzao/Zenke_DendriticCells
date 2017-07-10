
# Import
import os
import sys
from pysam import Fastafile

# Input
bedFileName = "/work/eg474423/eg474423_Projects/trunk/DendriticCells/Results/DC/enrichment_background/filtered_random/random_regions_original.bed"
outFileName = "/work/eg474423/eg474423_Projects/trunk/DendriticCells/Results/DC/enrichment_background/filtered_random/random_regions_annotated.bed"
mapFileName = "/work/eg474423/eg474423_Projects/trunk/RGT/Results/ExcludedRegions/mappability/mm9_map4_filter_50.bed"
blackFileName = "/work/eg474423/eg474423_Projects/trunk/RGT/Results/ExcludedRegions/blacklist/blacklist_mm9_kundaje_format.bed"
genomeFileName = "/hpcwork/izkf/projects/TfbsPrediction/Data/MM9/mm9.fa"

# Initialization
to_remove = []
genome_file = Fastafile(genomeFileName)

# Intersect map
mapIntFileName = "./tempM.bed"
to_remove.append(mapIntFileName)
os.system("intersectBed -wao -a "+bedFileName+" -b "+mapFileName+" > "+mapIntFileName)

# Intersect map
blackIntFileName = "./tempB.bed"
to_remove.append(blackIntFileName)
os.system("intersectBed -wao -a "+bedFileName+" -b "+blackFileName+" > "+blackIntFileName)

# Fetch CpG
bedFile = open(bedFileName,"r")
mFile = open(mapIntFileName,"r")
bFile = open(blackIntFileName,"r")
outFile = open(outFileName,"w")
for line in bedFile:

  # Initialization
  ll = line.strip().split("\t")
  total_length = float(int(ll[2])-int(ll[1]))

  # Fetching mappability and blacklist overlap
  mLine = mFile.readline()
  mValue = str(float(mLine.strip().split("\t")[-1]) / total_length)
  bLine = bFile.readline()
  bValue = str(float(bLine.strip().split("\t")[-1]) / total_length)

  # Fetching CpG content
  try:
    seq = str(genome_file.fetch(ll[0], int(ll[1]), int(ll[2]))).upper()
    prev = "N"; nc = 0; ng = 0; ncg = 0
    for i in range(0,len(seq)): 
      if(seq[i] == "C"): nc += 1
      elif(seq[i] == "G"):
        ng += 1
        if(prev == "C"): ncg += 1
      prev = seq[i]
    cpgScore = str((float(ncg)/(float(nc)+float(ng)))/ total_length)
  except Exception: cpgScore = "0"

  # Writing
  outFile.write("\t".join(ll[:3]+[cpgScore,mValue,bValue])+"\n")

# Termination
for e in to_remove: os.system("rm "+e)



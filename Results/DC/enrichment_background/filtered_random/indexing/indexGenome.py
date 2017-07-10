# This script indexes a genome by [indexingWindow] bp regions for percentiles on CpG islands, 
# mappability and blacklist frequencies.

# Import
import os
import sys
from math import ceil
from pysam import Fastafile
from whoosh.index import create_in, open_dir
from whoosh.fields import Schema, NUMERIC, TEXT
from whoosh.qparser import QueryParser
from whoosh.analysis import StandardAnalyzer

# Input
indexingWindow = int(sys.argv[1])
genomeFileName = sys.argv[2]
chromSizesFileName = sys.argv[3]
mapFileName = sys.argv[4]
blackFileName = sys.argv[5]
outputLocation = sys.argv[6]

# Initialization
to_remove = []
genome_file = Fastafile(genomeFileName)

# Index
schema=Schema(cpg=NUMERIC(int,32,stored=True),map=NUMERIC(int,32,stored=True),blk=NUMERIC(int,32,stored=True),region=TEXT(stored=True))
index = create_in(outputLocation, schema)
writer = index.writer()

# Reading chrom sizes file
csDict = dict()
chromSizesFile = open(chromSizesFileName,"r")
for line in chromSizesFile:
  ll = line.strip().split("\t")
  csDict[ll[0]] = int(ll[1])
chromSizesFile.close()
chrList = sorted(csDict.keys())

# Creating tiled file
tiledFileName = outputLocation+"mytemp.bed"
to_remove.append(tiledFileName)
tiledFile = open(tiledFileName,"w")
for chrName in chrList:
  for i in range(0,csDict[chrName],indexingWindow):
    p1 = i; p2 = min(i+indexingWindow,csDict[chrName])
    tiledFile.write("\t".join([chrName,str(p1),str(p2)])+"\n")
tiledFile.close()

# Intersection with mappability
mapIntFileName = "tempM.bed"
to_remove.append(mapIntFileName)
os.system("coverageBed -a "+mapFileName+" -b "+tiledFileName+" | sort -k1,1 -k2,2n > "+mapIntFileName)

# Intersection with blacklist
blackIntFileName = "tempB.bed"
to_remove.append(blackIntFileName)
os.system("coverageBed -a "+blackFileName+" -b "+tiledFileName+" | sort -k1,1 -k2,2n > "+blackIntFileName)

# Iterating on tiled file
tiledFile = open(tiledFileName,"r")
mFile = open(mapIntFileName,"r")
bFile = open(blackIntFileName,"r")
for line in tiledFile:

  # Initialization
  ll = line.strip().split("\t")
  currRegion = u":".join(ll[:3])
  mLine = mFile.readline()
  bLine = bFile.readline()
  # Fetching sequence
  try: seq = str(genome_file.fetch(ll[0],int(ll[1]),int(ll[2]))).upper()
  except Exception:
    print "ERROR FETCH SEQUENCE: "+":".join([ll[0],ll[1],ll[2]])
    continue

  # Evaluate CpG
  prev = "X"; nc = 0; ng = 0; ncg = 0; flagN = False
  for c in seq:
    if(c == "C"):
      nc += 1
      if(prev == "G"): ncg += 1
    elif(c == "G"):
      ng += 1
      if(prev == "C"): ncg += 1
    elif(c == "N"):
      flagN = True
      break
    prev = c
  if(flagN):
    print "SEQUENCE CONTAIN N: "+":".join([ll[0],ll[1],ll[2]])
    continue
  try: cpgScore = 100*float(ncg)/(float(nc)+float(ng))
  except Exception: cpgScore = 0.0
  cpgScoreCeil = int(ceil(cpgScore))

  # Fetching mappability overlap
  mValue = 100*float(mLine.strip().split("\t")[-1])
  mValueCeil = int(ceil(mValue))

  # Evaluate blacklist overlap
  bValue = 100*float(bLine.strip().split("\t")[-1])
  bValueCeil = int(ceil(bValue))

  # Adding to index
  writer.add_document(cpg=cpgScoreCeil,map=mValueCeil,blk=bValueCeil,region=currRegion)
  #print "\t".join(currRegion.split(":")+[str(cpgScoreCeil),str(mValueCeil),str(bValueCeil)])

# Termination
tiledFile.close()
mFile.close()
bFile.close()
writer.commit()
for e in to_remove: os.system("rm "+e)



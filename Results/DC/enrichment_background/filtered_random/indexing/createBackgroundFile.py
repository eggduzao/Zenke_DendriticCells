# This script indexes a genome by N bp regions for percentiles on CpG islands, mappability and blacklist frequencies

# Import
import os
import sys
from pysam import Fastafile
from random import randint
from math import ceil
from whoosh.index import create_in, open_dir
from whoosh.fields import Schema, NUMERIC, TEXT
from whoosh.qparser import QueryParser
from whoosh.query import Every, Term, And
from whoosh.analysis import StandardAnalyzer

# Input
rand_prop = 10
inFileName = "/work/eg474423/eg474423_Projects/trunk/DendriticCells/Results/DC/motif_enrichment/regions/cdp_mpp_pu1.bed"
mapFileName = "/work/eg474423/eg474423_Projects/trunk/RGT/Results/ExcludedRegions/mappability/mm9_map4_filter_50.bed"
genomeFileName = "/hpcwork/izkf/projects/TfbsPrediction/Data/MM9/mm9.fa"
outputFileName = "background_file.bed"

# Initialization
genome_file = Fastafile(genomeFileName)
to_remove = []

# Creating index
schema=Schema(cpg=NUMERIC(int,32,stored=True),map=NUMERIC(int,32,stored=True),blk=NUMERIC(int,32,stored=True),region=TEXT(stored=True))
index = open_dir("mm9_map_index")

# Removing bad chromosomes
bedFileName = "./temp_in.bed"
to_remove.append(bedFileName)
os.system("grep -v -E 'chrY|chrM|random' "+inFileName+" | sort -k1,1 -k2,2n > "+bedFileName)

# Evaluating mappability
mapIntFileName = "./tempM.bed"
to_remove.append(mapIntFileName)
os.system("coverageBed -a "+mapFileName+" -b "+bedFileName+" | sort -k1,1 -k2,2n > "+mapIntFileName)

# Reading regions
inFile = open(mapIntFileName,"r")
myList = [] # [len,map]
for line in inFile:
  ll = line.strip().split("\t")
  myL = int(ll[2])-int(ll[1])
  seq = str(genome_file.fetch(ll[0],int(ll[1]),int(ll[2]))).upper()
  prev = "X"; nc = 0; ng = 0; ncg = 0
  for c in seq:
    if(c == "C"):
      nc += 1
      if(prev == "G"): ncg += 1
    elif(c == "G"):
      ng += 1
      if(prev == "C"): ncg += 1
    prev = c
  cpg = int(ceil(100*float(ncg)/(float(nc)+float(ng))))
  myList.append([myL,int(ceil(100*float(ll[-1]))),cpg])
inFile.close()

# Load random into memory
randomMatrixDict = dict()

# Creating random regions
outFile = open(outputFileName,"w")
num_reg = rand_prop*len(myList)
reg_added = 0; counter = 0
with index.searcher() as searcher:
  while(reg_added < num_reg):
  
    # Tracking progress
    print str(round(100*float(reg_added)/num_reg,4))+"%"

    # Fetching mappability
    currM = myList[counter][1]
    strM = str(currM)

    # Evaluate CpG
    currC = myList[counter][2]
    strC = str(currC)

    # Dict key
    dk = strM+":"+strC

    try:
      r = randint(0,len(randomMatrixDict[dk]))
      mid = (int(randomMatrixDict[dk][r][1]) + int(randomMatrixDict[dk][r][2])) / 2
      p1 = mid - (myList[counter][0]/2)
      p2 = mid + (myList[counter][0]/2)
    except Exception:
      query = And([Term("map",currM), Term("cpg", currC)])
      results = searcher.search(query, limit=None, scored=False, sortedby=None)
      if(len(results) == 0):
        currC = max(min(currC,23),5)
        query = And([Term("map",currM), Term("cpg", currC)])
        results = searcher.search(query, limit=None, scored=False, sortedby=None)
      for e in results:
        try: randomMatrixDict[dk].append(e["region"].split(":")+[e["map"],e["cpg"]])
        except Exception: randomMatrixDict[dk] = [e["region"].split(":")+[e["map"],e["cpg"]]]
      r = randint(0,len(randomMatrixDict[dk])-1)
      mid = (int(randomMatrixDict[dk][r][1]) + int(randomMatrixDict[dk][r][2])) / 2
      p1 = mid - (myList[counter][0]/2)
      p2 = mid + (myList[counter][0]/2)

    outFile.write("\t".join([randomMatrixDict[dk][r][0],str(p1),str(p2)])+"\n")

    reg_added += 1
    counter += 1
    if(counter >= len(myList)): counter = 0

outFile.close()



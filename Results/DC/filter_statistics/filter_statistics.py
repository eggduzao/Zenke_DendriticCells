
# Import
import os
import sys
from pysam import Fastafile

# Input
il = "/work/eg474423/eg474423_Projects/trunk/DendriticCells/Results/DC/"

# Input Dictionary

inDict = dict([

("Pu1_Peaks",[
il+"enrichment_background/diffpeak/cdc_cdp_pu1_ev.bed",
il+"enrichment_background/diffpeak/cdc_pdc_pu1_ev.bed", 
il+"enrichment_background/diffpeak/cdp_mpp_pu1_ev.bed", 
il+"enrichment_background/diffpeak/mpp_cdp_pu1_ev.bed", 
il+"enrichment_background/diffpeak/pdc_cdc_pu1_ev.bed", 
il+"enrichment_background/diffpeak/pdc_cdp_pu1_ev.bed"]),

("Random_Bg",[
il+"motif_enrichment/regions/random_regions.bed"]),

("Random_Filtered_Bg",[
il+"enrichment_background/filtered_random/indexing/background_file.bed"]),

("HS_Bg",[
il+"enrichment_background/HS/HS_background.bed"]),

("DiffPeak_Bg",[
il+"enrichment_background/diffpeak/cdc_cdp_pu1_nev.bed", 
il+"enrichment_background/diffpeak/cdc_pdc_pu1_nev.bed", 
il+"enrichment_background/diffpeak/cdp_mpp_pu1_nev.bed", 
il+"enrichment_background/diffpeak/mpp_cdp_pu1_nev.bed", 
il+"enrichment_background/diffpeak/pdc_cdc_pu1_nev.bed", 
il+"enrichment_background/diffpeak/pdc_cdp_pu1_nev.bed"]),

("DiffGene_Bg",[
il+"enrichment_background/diffgene/cdc_cdp_pu1_unchanged_ev.bed",
il+"enrichment_background/diffgene/cdc_pdc_pu1_unchanged_ev.bed",
il+"enrichment_background/diffgene/cdp_mpp_pu1_unchanged_ev.bed",
il+"enrichment_background/diffgene/mpp_cdp_pu1_unchanged_ev.bed",
il+"enrichment_background/diffgene/pdc_cdc_pu1_unchanged_ev.bed",
il+"enrichment_background/diffgene/pdc_cdp_pu1_unchanged_ev.bed"])])

# Input files
mapFileName = "/work/eg474423/eg474423_Projects/trunk/RGT/Results/ExcludedRegions/mappability/mm9_map4_filter_50.bed"
blackFileName = "/work/eg474423/eg474423_Projects/trunk/RGT/Results/ExcludedRegions/blacklist/blacklist_mm9_kundaje_format.bed"
genomeFileName = "/hpcwork/izkf/projects/TfbsPrediction/Data/MM9/mm9.fa"
outLoc = "/work/eg474423/eg474423_Projects/trunk/DendriticCells/Results/DC/filter_statistics/result/"
genome_file = Fastafile(genomeFileName)

# Iterating on dictionary
for k in inDict.keys():

  # Initialization
  mapVector = []
  blackVector = []
  cpgVector = []

  # Iterating on files
  for inFileName in inDict[k]:

    # Initialization
    to_remove = []

    # Mappability
    intFileName = "./temp.bed"
    to_remove.append(intFileName)
    os.system("coverageBed -a "+mapFileName+" -b "+inFileName+" | sort -k1,1 -k2,2n > "+intFileName)
    intFile = open(intFileName,"r")
    for line in intFile:
      ll = line.strip().split("\t")
      mapVector.append(str(float(ll[-1])))
    intFile.close()

    # Blacklist
    intFileName = "./temp.bed"
    os.system("coverageBed -a "+blackFileName+" -b "+inFileName+" | sort -k1,1 -k2,2n > "+intFileName)
    intFile = open(intFileName,"r")
    for line in intFile:
      ll = line.strip().split("\t")
      blackVector.append(str(float(ll[-1])))
    intFile.close()

    # CpG
    sortFileName = "./temp.bed"
    os.system("sort -k1,1 -k2,2n "+inFileName+" > "+sortFileName)
    bedFile = open(sortFileName,"r")
    for line in bedFile:
      ll = line.strip().split("\t")
      try:
        seq = str(genome_file.fetch(ll[0], int(ll[1]), int(ll[2]))).upper()
        prev = "X"; nc = 0; ng = 0; ncg = 0
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
        cpgScore = str(float(ncg)/(float(nc)+float(ng)))
      except Exception: cpgScore = "0"
      cpgVector.append(cpgScore)
    bedFile.close()

  # Writing results
  outFileName = outLoc+k+"_stats.txt"
  outFile = open(outFileName,"w")
  for i in range(0,len(cpgVector)): outFile.write("\t".join([cpgVector[i],mapVector[i],blackVector[i]])+"\n")
  outFile.close()
  for e in to_remove: os.system("rm "+e)
genome_file.close()

# Reading results
sortedKeys = ["Pu1_Peaks","Random_Bg","Random_Filtered_Bg","HS_Bg","DiffPeak_Bg","DiffGene_Bg"]
inFileNameList = [outLoc+e+"_stats.txt" for e in sortedKeys]
tables = [[],[],[]]
for inFileName in inFileNameList:
  inFile = open(inFileName,"r")
  tables[0].append([]); tables[1].append([]); tables[2].append([])
  for line in inFile:
    ll = line.strip().split("\t")
    tables[0][-1].append(ll[0])
    tables[1][-1].append(ll[1])
    tables[2][-1].append(ll[2])
  inFile.close()

# Writing results
outputFileNameList = [outLoc+"table_cpg.txt",outLoc+"table_map.txt",outLoc+"table_blk.txt"]
outputFileList = [open(e,"w") for e in outputFileNameList]
for i in range(0,len(outputFileList)):
  of = outputFileList[i]
  of.write("\t".join(sortedKeys)+"\n")
  maxL = max([len(e) for e in tables[i]])
  for j in range(0,maxL):
    vec = []
    for k in range(0,len(sortedKeys)): 
      try: vec.append(tables[i][k][j])
      except Exception: vec.append("NA")
    of.write("\t".join(vec)+"\n")
for e in outputFileList: e.close()

# Applying R scripts
os.system("R CMD BATCH boxplot.R")




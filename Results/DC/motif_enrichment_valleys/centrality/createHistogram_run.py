
# Import
import os
import sys

# Input
ext = "_ext1000"
il = "/work/eg474423/eg474423_Projects/trunk/DendriticCells/Results/DC/motif_enrichment_valleys/centrality/input/"
ol = "/work/eg474423/eg474423_Projects/trunk/DendriticCells/Results/DC/motif_enrichment_valleys/centrality/results"+ext+"/"
puList = ["PU1_cDC_summits", "PU1_CDP_summits", "PU1_MPP_summits", "PU1_pDC_summits"]
fpList = ["DC_cDC_footprints"+ext, "DC_CDP_footprints"+ext, "DC_MPP_footprints"+ext, "DC_pDC_footprints"+ext]
labelList = ["cDC", "CDP", "MPP", "pDC"]

# Creating individual histograms
outList = []
os.system("mkdir -p "+ol)
for i in range(0,len(puList)):
  label = labelList[i]
  bedFileName1 = il+puList[i]+".bed"
  bedFileName2 = il+fpList[i]+".bed"
  outFileName = ol+labelList[i]+".txt"
  outFileNameSizeDist = ol+labelList[i]+"_size.txt"
  outFileNameStats = ol+labelList[i]+"_stats.txt"
  outList.append(outFileName)
  os.system("python /work/eg474423/eg474423_Projects/trunk/DendriticCells/Results/DC/motif_enrichment_valleys/centrality/createHistogram_pipeline.py "+" ".join([label,bedFileName1,bedFileName2,outFileName,outFileNameSizeDist,outFileNameStats]))

# Merging histograms
os.system("paste "+" ".join(outList)+" > "+ol+"histograms.txt")



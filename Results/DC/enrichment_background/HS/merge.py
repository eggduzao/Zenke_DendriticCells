import os
import sys
from glob import glob

csFileName = "/hpcwork/izkf/projects/TfbsPrediction/Data/MM9/mm9.chrom.sizes.ext10000"
inLoc1 = "/work/eg474423/eg474423_Projects/trunk/DendriticCells/Results/DC/enrichment_background/HS/motif_match/Match/"
inLoc2 = "/work/eg474423/eg474423_Projects/trunk/DendriticCells/Results/DC/enrichment_background/HS/motif_match2/Match/"
inLoc3 = "/work/eg474423/eg474423_Projects/trunk/DendriticCells/Results/DC/enrichment_background/HS/motif_internal/Match/"
outLoc = "/work/eg474423/eg474423_Projects/trunk/DendriticCells/Results/DC/enrichment_background/HS/res/"

for inFileName in glob(inLoc1+"*.bed"):
  inName = inFileName.split("/")[-1]
  inFileName1 = inFileName
  inFileName2 = inLoc2+inName
  inFileName3 = inLoc3+inName
  mergeFileName = outLoc+inName+"_cat.bed"
  sortFileName = outLoc+inName
  bbFileName = outLoc+inName[:-3]+"bb"
  if(os.path.isfile(bbFileName)): continue
  os.system("cat "+inFileName1+" "+inFileName2+" > "+mergeFileName)
  os.system("sort -k1,1 -k2,2n "+mergeFileName+" > "+sortFileName)
  os.system("bedToBigBed "+sortFileName+" "+csFileName+" "+bbFileName)
  os.system("rm "+mergeFileName+" "+sortFileName)



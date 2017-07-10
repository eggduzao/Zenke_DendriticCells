
# Import
import os
import sys
from glob import glob

inLoc = "/work/eg474423/eg474423_Projects/trunk/DendriticCells/Results/DC/motif_enrichment_valleys/results/random_background/Match/"
intLoc = "/work/eg474423/eg474423_Projects/trunk/DendriticCells/Results/DC/motif_enrichment_valleys/input/"
csFileName = "/hpcwork/izkf/projects/TfbsPrediction/Data/MM9/mm9.chrom.sizes"
outLoc5 = "/work/eg474423/eg474423_Projects/trunk/DendriticCells/Results/DC/motif_enrichment_valleys/results/random_background_e500/Match/"
outLoc10 = "/work/eg474423/eg474423_Projects/trunk/DendriticCells/Results/DC/motif_enrichment_valleys/results/random_background_e1000/Match/"

os.system("mkdir -p "+outLoc5)
os.system("mkdir -p "+outLoc10)

for inFileName in glob(inLoc+"*.bb"):

  if("random_regions" in inFileName): continue
  fName = inFileName.split("/")[-1].split(".")[0]
  fNameInt = "_".join(fName.split("_")[:-1])

  inBB = inLoc+fName+".bb"
  inBed = inLoc+fName+"_T.bed"
  os.system("bigBedToBed "+inBB+" "+inBed)

  intBed5 = intLoc+fNameInt+"_ext500.bed"
  intBed10 = intLoc+fNameInt+"_ext1000.bed"
  intRes5 = intLoc+fNameInt+"_res5.bed"
  intRes10 = intLoc+fNameInt+"_res10.bed"
  os.system("intersectBed -wa -u -a "+inBed+" -b "+intBed5+" > "+intRes5)
  os.system("intersectBed -wa -u -a "+inBed+" -b "+intBed10+" > "+intRes10)

  intResBB5 = outLoc5+fName+".bb"
  intResBB10 = outLoc10+fName+".bb"
  os.system("bedToBigBed "+intRes5+" "+csFileName+" "+intResBB5)
  os.system("bedToBigBed "+intRes10+" "+csFileName+" "+intResBB10)

  os.system("rm "+inBed)
  os.system("rm "+intRes5)
  os.system("rm "+intRes10)



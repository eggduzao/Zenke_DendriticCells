import os
import sys
from glob import glob

csFileName = "/hpcwork/izkf/projects/TfbsPrediction/Data/MM9/mm9.chrom.sizes.ext10000"

# BED to BB
for inFileName in glob("./*.bed"):
  os.system("bedToBigBed "+inFileName+" "+csFileName+" "+inFileName[:-3]+"bb")

# BB to BED
#for inFileName in glob("./*.bb"):
#  os.system("bigBedToBed "+inFileName+" "+inFileName[:-2]+"bed")



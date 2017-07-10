
# Import
import sys
from Bio import motifs
from glob import glob

# Reading input
outputLoc = "./"
inList = glob("./*.pwm")

# Execution
for inFileName in inList:
  inFile = open(inFileName,"r")
  outFileName = outputLoc+inFileName+".png"
  pwm = motifs.read(inFile, "pfm")
  pwm.weblogo(outFileName, format="png_print", stack_width = "medium", color_scheme = "color_classic")
  inFile.close()



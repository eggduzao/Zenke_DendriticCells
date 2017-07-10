
# Import
import os
import sys
import random

# Input
rep = 10
cl1 = "/work/eg474423/ig440396_dendriticcells/exp/diffpeakdc/macs/irf8/"
cl2 = "/work/eg474423/ig440396_dendriticcells/exp/diffpeakdc/diff/res/"
inputList = [cl1+"pu1_mpp_irf8_summit_500.bed", cl1+"pu1_cdp_irf8_summit_500.bed", cl1+"pu1_cdc_irf8_summit_500.bed",
             cl1+"pu1_pdc_irf8_summit_500.bed", cl1+"irf8_dup_summits_500_4.bed",
             cl2+"mpp_cdp_pu1.bed", cl2+"cdp_mpp_pu1.bed", cl2+"cdc_pdc_pu1.bed", cl2+"pdc_cdc_pu1.bed",
             cl2+"mpp_pu1_irf8_up_summit_final.bed", cl2+"cdp_pu1_irf8_up_summit_final.bed",
             cl2+"cdc_pu1_irf8_up_summit_final.bed", cl2+"pdc_pu1_irf8_up_summit_final.bed" ]
outputLocation = "/work/eg474423/eg474423_Projects/trunk/DendriticCells/PerfectMatching/Input/Random/"

# Reading chromosome sizes
csFile = open("/hpcwork/izkf/projects/egg/Data/MM9/mm9.chrom.sizes","r")
csDict = dict()
for line in csFile:
    ll = line.strip().split("\t")
    csDict[ll[0]] = int(ll[1])
csFile.close()

# Iterating on input files
for inFileName in inputList:
    inName = inFileName.split("/")[-1].split(".")[0]
    inFile = open(inFileName,"r")
    outFile = open(outputLocation+inName+".bed","w")
    for line in inFile:
        ll = line.strip().split("\t")
        chrName = ll[0]; width = int(ll[2])-int(ll[1])
        for i in range(0,rep):
            r = random.randint(0,csDict[chrName]-(10*width))
            outFile.write("\t".join([chrName,str(r),str(r+width)])+"\n")
    inFile.close()
    outFile.close()



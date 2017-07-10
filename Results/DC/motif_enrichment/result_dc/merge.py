
import os
import sys

csf = "/hpcwork/izkf/projects/TfbsPrediction/Data/MM9/mm9.chrom.sizes.ext10000"
il1 = "/work/eg474423/eg474423_Projects/trunk/DendriticCells/Results/DC/motif_enrichment/result_dc/random_filtered2/Match/"
il2 = "/work/eg474423/eg474423_Projects/trunk/DendriticCells/Results/DC/motif_enrichment/result_dc/random_filtered3/Match/"
inList = ["cdc_cdp", "cdc_pdc", "cdp_mpp", "mpp_cdp", "pdc_cdc", "pdc_cdp"]
for inName in inList:
  bb1=il1+inName+"_mpbs.bb"
  bed1=il1+inName+"_mpbs.bed"
  bb2=il2+inName+"_mpbs.bb"
  bed2=il2+inName+"_mpbs.bed"
  m=il2+inName+"_merge.bed"
  s=il2+inName+"_sort.bed"
  to_remove = [bed1,bed2,m,s]
  os.system("bigBedToBed "+bb1+" "+bed1)
  os.system("bigBedToBed "+bb2+" "+bed2)
  os.system("cat "+bed1+" "+bed2+" > "+m)
  os.system("sort -k1,1 -k2,2n "+m+" > "+s)
  os.system("bedToBigBed "+s+" "+csf+" "+bb2)
  for e in to_remove: os.system("rm "+e)



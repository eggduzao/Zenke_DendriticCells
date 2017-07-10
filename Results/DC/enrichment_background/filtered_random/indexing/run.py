
import os
import sys

# MM9
indexingWindow = "1000"
genomeFileName = "/hpcwork/izkf/projects/TfbsPrediction/Data/MM9/mm9.fa"
chromSizesFileName = "/hpcwork/izkf/projects/TfbsPrediction/Data/MM9/mm9.chrom.sizes"
mapFileName = "/work/eg474423/eg474423_Projects/trunk/RGT/Results/ExcludedRegions/mappability/mm9_map4_filter_50.bed"
blackFileName = "/work/eg474423/eg474423_Projects/trunk/RGT/Results/ExcludedRegions/blacklist/blacklist_mm9_kundaje_format.bed"
outputLocation = "/work/eg474423/eg474423_Projects/trunk/DendriticCells/Results/DC/enrichment_background/filtered_random/indexing/mm9_map_index/"
os.system("python2.7 indexGenome.py "+" ".join([indexingWindow,genomeFileName,chromSizesFileName,mapFileName,blackFileName,outputLocation]))

# HG19
indexingWindow = "1000"
genomeFileName = "/hpcwork/izkf/projects/TfbsPrediction/Data/HG19/hg19.fa"
chromSizesFileName = "/hpcwork/izkf/projects/TfbsPrediction/Data/HG19/hg19.chrom.sizes.filtered"
mapFileName = "/work/eg474423/eg474423_Projects/trunk/RGT/Results/ExcludedRegions/mappability/hg19_map4_filter_50.bed"
blackFileName = "/work/eg474423/eg474423_Projects/trunk/RGT/Results/ExcludedRegions/blacklist/blacklist_hg19_duke_format.bed"
outputLocation = "/work/eg474423/eg474423_Projects/trunk/DendriticCells/Results/DC/enrichment_background/filtered_random/indexing/hg19_map_index/"
os.system("python2.7 indexGenome.py "+" ".join([indexingWindow,genomeFileName,chromSizesFileName,mapFileName,blackFileName,outputLocation]))



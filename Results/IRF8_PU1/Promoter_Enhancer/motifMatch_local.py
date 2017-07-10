
# Import
import os

# Parameters
organism="--organism mm9"
fpr="--fpr 0.0001"
precision="--precision 10000"
pseudocounts="--pseudocounts 0.1"
rand_proportion="--rand-proportion 10"
bigbed="--bigbed"

"""
# CDP
inputMatrix="/work/eg474423/eg474423_Projects/trunk/DendriticCells/Results/IRF8_PU1_Promoter_Enhancer/ExpMat/MotifMatch.txt"
output_location="--output-location /work/eg474423/eg474423_Projects/trunk/DendriticCells/Results/IRF8_PU1_Promoter_Enhancer/Results/"
myL = "MMIPE"
clusterCommand = "rgt-motifanalysis --matching "
clusterCommand += organism+" "+fpr+" "+precision+" "+pseudocounts+" "+rand_proportion+" "
clusterCommand += output_location+" "+bigbed+" "+inputMatrix
os.system(clusterCommand)
"""

# cDC
inputMatrix="/work/eg474423/eg474423_Projects/trunk/DendriticCells/Results/IRF8_PU1_Promoter_Enhancer/ExpMat/cdc_up.txt"
output_location="--output-location /work/eg474423/eg474423_Projects/trunk/DendriticCells/Results/IRF8_PU1_Promoter_Enhancer/Results/c/"
myL = "MMIPEC"
clusterCommand = "rgt-motifanalysis --matching "
clusterCommand += organism+" "+fpr+" "+precision+" "+pseudocounts+" "+rand_proportion+" "
clusterCommand += output_location+" "+bigbed+" "+inputMatrix
os.system(clusterCommand)
"""
# pDC
inputMatrix="/work/eg474423/eg474423_Projects/trunk/DendriticCells/Results/IRF8_PU1_Promoter_Enhancer/ExpMat/pdc_up.txt"
output_location="--output-location /work/eg474423/eg474423_Projects/trunk/DendriticCells/Results/IRF8_PU1_Promoter_Enhancer/Results/p/"
myL = "MMIPEP"
clusterCommand = "rgt-motifanalysis --matching "
clusterCommand += organism+" "+fpr+" "+precision+" "+pseudocounts+" "+rand_proportion+" "
clusterCommand += output_location+" "+bigbed+" "+inputMatrix
os.system(clusterCommand)
"""



# Import
import os

# Parameters
organism="--organism mm9"
fpr="--fpr 0.0001"
precision="--precision 10000"
pseudocounts="--pseudocounts 0.1"
rand_proportion="--rand-proportion 10"
bigbed="--bigbed"
norm_threshold="--norm-threshold"
normalize_bitscore="--normalize-bitscore"
output_location="--output-location /work/eg474423/eg474423_Projects/trunk/DendriticCells/Results/IRF8_PU1_NormMotifs/results/"

# Input
inputMatrix="/work/eg474423/eg474423_Projects/trunk/DendriticCells/Results/IRF8_PU1_NormMotifs/exp_mat/IRF8_PU1.txt"

# Execution
"""
myL = "MMIPNPWM"
clusterCommand = "bsub "
clusterCommand += "-J "+myL+" -o "+myL+"_out.txt -e "+myL+"_err.txt "
clusterCommand += "-W 300:00 -M 42000 -S 100 -P izkf -R \"select[hpcwork]\" ./motifAnalysis_pipeline.zsh --matching "
clusterCommand += organism+" "+fpr+" "+precision+" "+pseudocounts+" "+rand_proportion+" "
clusterCommand += output_location+" "+bigbed+" "+norm_threshold+" "+normalize_bitscore+" "+inputMatrix
os.system(clusterCommand)
"""

# Local
clusterCommand = "rgt-motifanalysis --matching "
clusterCommand += organism+" "+fpr+" "+precision+" "+pseudocounts+" "+rand_proportion+" "
clusterCommand += output_location+" "+bigbed+" "+norm_threshold+" "+normalize_bitscore+" "+inputMatrix
os.system(clusterCommand)



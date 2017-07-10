
# Import
import os

# Parameters
organism="--organism mm9"
fpr="--fpr 0.0001"
precision="--precision 10000"
pseudocounts="--pseudocounts 0.1"
rand_proportion="--rand-proportion 0.001"
output_location="--output-location /work/eg474423/eg474423_Projects/trunk/DendriticCells/Results/DC_enhanceosome/motif_match/results/"
bigbed="--bigbed"
inputMatrix="/work/eg474423/eg474423_Projects/trunk/DendriticCells/Results/DC_enhanceosome/motif_match/exp_mat/motif_match.txt"

# Execution
myL = "MM_QIONG"
clusterCommand = "bsub "
clusterCommand += "-J "+myL+" -o "+myL+"_out.txt -e "+myL+"_err.txt "
clusterCommand += "-W 120:00 -M 24000 -S 100 -P izkf -R \"select[hpcwork]\" ./motifAnalysis_pipeline.zsh --matching "
clusterCommand += organism+" "+fpr+" "+precision+" "+pseudocounts+" "+rand_proportion+" "
clusterCommand += output_location+" "+bigbed+" "+inputMatrix
os.system(clusterCommand)



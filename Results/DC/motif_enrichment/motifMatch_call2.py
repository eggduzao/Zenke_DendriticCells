
# Import
import os

###################################################################################################
# DC
###################################################################################################

# Parameters
organism="--organism mm9"
fpr="--fpr 0.0001"
precision="--precision 10000"
pseudocounts="--pseudocounts 0.1"
rand_proportion="--rand-proportion 0.0001"
output_location="--output-location /work/eg474423/eg474423_Projects/trunk/DendriticCells/Results/DC/motif_enrichment/result_dc/random_filtered3/"
bigbed="--bigbed"
inputMatrix="/work/eg474423/eg474423_Projects/trunk/DendriticCells/Results/DC/motif_enrichment/exp_mat/dc_motifmatch.txt"

# Execution
myL = "MM_DC_FIX"
clusterCommand = "bsub "
clusterCommand += "-J "+myL+" -o "+myL+"_out.txt -e "+myL+"_err.txt "
clusterCommand += "-W 12:00 -M 12000 -S 100 -P izkf -R \"select[hpcwork]\" ./motifAnalysis_pipeline.zsh --matching "
clusterCommand += organism+" "+fpr+" "+precision+" "+pseudocounts+" "+rand_proportion+" "
clusterCommand += output_location+" "+bigbed+" "+inputMatrix
os.system(clusterCommand)



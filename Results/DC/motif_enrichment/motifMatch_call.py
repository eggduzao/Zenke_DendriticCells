
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
#rand_proportion="--rand-proportion 10"
rand_proportion="--rand-proportion 0.0001"
#output_location="--output-location /work/eg474423/eg474423_Projects/trunk/DendriticCells/Results/DC/motif_enrichment/result_dc/random/"
output_location="--output-location /work/eg474423/eg474423_Projects/trunk/DendriticCells/Results/DC/motif_enrichment/result_dc_internal/"
bigbed="--bigbed"
inputMatrix="/work/eg474423/eg474423_Projects/trunk/DendriticCells/Results/DC/motif_enrichment/exp_mat/dc_motifmatch2.txt"

# Execution
myL = "MM_DC_INTERNAL"
clusterCommand = "bsub "
clusterCommand += "-J "+myL+" -o "+myL+"_out.txt -e "+myL+"_err.txt "
clusterCommand += "-W 48:00 -M 12000 -S 100  -R \"select[hpcwork]\" ./motifAnalysis_pipeline.zsh --matching "
#clusterCommand += "-W 100:00 -M 12000 -S 100  -R \"select[hpcwork]\" ./motifAnalysis_pipeline.zsh --matching "
clusterCommand += organism+" "+fpr+" "+precision+" "+pseudocounts+" "+rand_proportion+" "
clusterCommand += output_location+" "+bigbed+" "+inputMatrix
os.system(clusterCommand)




# Import
import os

###################################################################################################
# HS background
###################################################################################################

# Parameters
organism="--organism mm9"
fpr="--fpr 0.0001"
precision="--precision 10000"
pseudocounts="--pseudocounts 0.1"
rand_proportion="--rand-proportion 0.00001"
output_location="--output-location /work/eg474423/eg474423_Projects/trunk/DendriticCells/Results/DC/enrichment_background/HS/motif_internal/"
#bigbed="--bigbed"
inputMatrix="/work/eg474423/eg474423_Projects/trunk/DendriticCells/Results/DC/enrichment_background/HS/exp_mat.txt"

# Execution
myL = "MM_HSI"
clusterCommand = "bsub "
clusterCommand += "-J "+myL+" -o "+myL+"_out.txt -e "+myL+"_err.txt "
#clusterCommand += "-W 300:00 -M 40960 -S 100 -P izkf -R \"select[hpcwork]\" ./motifAnalysis_pipeline.zsh --matching "
clusterCommand += "-W 48:00 -M 12000 -S 100 -P izkf -R \"select[hpcwork]\" ./motifAnalysis_pipeline.zsh --matching "
clusterCommand += organism+" "+fpr+" "+precision+" "+pseudocounts+" "+rand_proportion+" "
#clusterCommand += output_location+" "+bigbed+" "+inputMatrix
clusterCommand += output_location+" "+inputMatrix
os.system(clusterCommand)



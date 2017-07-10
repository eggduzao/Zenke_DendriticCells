
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
rand_proportion="--rand-proportion 0.01"
#output_location="--output-location /work/eg474423/eg474423_Projects/trunk/DendriticCells/Results/DC/enrichment_background/diffgene/motif_match/"
output_location="--output-location /work/eg474423/eg474423_Projects/trunk/DendriticCells/Results/DC/enrichment_background/diffgene/motif_match/novel/"
bigbed="--bigbed"
inputMatrix="/work/eg474423/eg474423_Projects/trunk/DendriticCells/Results/DC/enrichment_background/diffgene/motif_match/exp_mat.txt"

# Execution
myL = "MM_DG"
clusterCommand = "bsub "
clusterCommand += "-J "+myL+" -o "+myL+"_out.txt -e "+myL+"_err.txt "
#clusterCommand += "-W 150:00 -M 48000 -S 100 -P izkf -R \"select[hpcwork]\" ./motifAnalysis_pipeline.zsh --matching "
clusterCommand += "-W 48:00 -M 12000 -S 100 -P izkf -R \"select[hpcwork]\" ./motifAnalysis_pipeline.zsh --matching "
clusterCommand += organism+" "+fpr+" "+precision+" "+pseudocounts+" "+rand_proportion+" "
clusterCommand += output_location+" "+bigbed+" "+inputMatrix
os.system(clusterCommand)



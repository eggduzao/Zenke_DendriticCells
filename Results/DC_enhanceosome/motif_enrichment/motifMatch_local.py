
# Import
import os

# Parameters
organism="--organism mm9"
fpr="--fpr 0.0001"
precision="--precision 10000"
pseudocounts="--pseudocounts 0.1"
rand_proportion="--rand-proportion 10"
output_location="--output-location /work/eg474423/eg474423_Projects/trunk/DendriticCells/Results/DC_enhanceosome/motif_enrichment/results/"
bigbed="--bigbed"
inputMatrix="/work/eg474423/eg474423_Projects/trunk/DendriticCells/Results/DC_enhanceosome/motif_enrichment/exp_mat/motif_match.txt"

# Execution
clusterCommand = "rgt-motifanalysis --matching "
clusterCommand += organism+" "+fpr+" "+precision+" "+pseudocounts+" "+rand_proportion+" "
clusterCommand += output_location+" "+bigbed+" "+inputMatrix
os.system(clusterCommand)



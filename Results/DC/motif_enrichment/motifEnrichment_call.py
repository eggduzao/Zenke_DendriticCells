
# Import
import os

# Parameters
organism="--organism mm9"
promoter_length="--promoter-length 1000"
maximum_association_length="--maximum-association-length 50000"
multiple_test_alpha="--multiple-test-alpha 0.05"
processes="--processes 1"
print_thresh="--print-thresh 1.0"
bigbed="--bigbed"

# Random
inputMatrix="/work/eg474423/eg474423_Projects/trunk/DendriticCells/Results/DC/motif_enrichment/exp_mat/dc_motifmatch.txt"
matchLoc="/work/eg474423/eg474423_Projects/trunk/DendriticCells/Results/DC/motif_enrichment/result_dc/random/"
output_location="--output-location /work/eg474423/eg474423_Projects/trunk/DendriticCells/Results/DC/motif_enrichment/test/"
myL = "ME_R"
clusterCommand = "bsub "
clusterCommand += "-J "+myL+" -o "+myL+"_out.txt -e "+myL+"_err.txt "
clusterCommand += "-W 120:00 -M 12000 -S 100 -P izkf -R \"select[hpcwork]\" ./motifAnalysis_pipeline.zsh --enrichment "
clusterCommand += organism+" "+promoter_length+" "+maximum_association_length+" "+multiple_test_alpha+" "
clusterCommand += processes+" "+output_location+" "+print_thresh+" "+bigbed+" "+inputMatrix+" "+matchLoc
os.system(clusterCommand)

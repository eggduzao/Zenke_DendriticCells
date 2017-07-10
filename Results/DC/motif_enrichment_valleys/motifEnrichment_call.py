
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

###################################################################################################
# RANDOM BACKGROUND / NO EXT
###################################################################################################

##########
### UP
##########

# Parameters
inputMatrix="/work/eg474423/eg474423_Projects/trunk/DendriticCells/Results/DC/motif_enrichment_valleys/matrix/dc_me_up.txt"
matchLoc="/work/eg474423/eg474423_Projects/trunk/DendriticCells/Results/DC/motif_enrichment_valleys/results/random_background/"
output_location="--output-location /work/eg474423/eg474423_Projects/trunk/DendriticCells/Results/DC/motif_enrichment_valleys/results/random_background/"
myL = "ME_RAND_UP"

# Execution
clusterCommand = "bsub "
clusterCommand += "-J "+myL+" -o "+myL+"_out.txt -e "+myL+"_err.txt "
clusterCommand +="-W 120:00 -M 12000 -S 100 -P izkf -R \"select[hpcwork]\" ./motifAnalysis_pipeline.zsh --enrichment "
clusterCommand += organism+" "+promoter_length+" "+maximum_association_length+" "+multiple_test_alpha+" "
clusterCommand += processes+" "+output_location+" "+print_thresh+" "+bigbed+" "+inputMatrix+" "+matchLoc
#os.system(clusterCommand)

##########
### DOWN
##########

# Parameters
inputMatrix="/work/eg474423/eg474423_Projects/trunk/DendriticCells/Results/DC/motif_enrichment_valleys/matrix/dc_me_down.txt"
matchLoc="/work/eg474423/eg474423_Projects/trunk/DendriticCells/Results/DC/motif_enrichment_valleys/results/random_background/"
output_location="--output-location /work/eg474423/eg474423_Projects/trunk/DendriticCells/Results/DC/motif_enrichment_valleys/results/random_background/"
myL = "ME_RAND_DW"

# Execution
clusterCommand = "bsub "
clusterCommand += "-J "+myL+" -o "+myL+"_out.txt -e "+myL+"_err.txt "
clusterCommand +="-W 120:00 -M 12000 -S 100 -P izkf -R \"select[hpcwork]\" ./motifAnalysis_pipeline.zsh --enrichment "
clusterCommand += organism+" "+promoter_length+" "+maximum_association_length+" "+multiple_test_alpha+" "
clusterCommand += processes+" "+output_location+" "+print_thresh+" "+bigbed+" "+inputMatrix+" "+matchLoc
#os.system(clusterCommand)


###################################################################################################
# RANDOM BACKGROUND / 500 EXT
###################################################################################################

##########
### UP
##########

# Parameters
inputMatrix="/work/eg474423/eg474423_Projects/trunk/DendriticCells/Results/DC/motif_enrichment_valleys/matrix/dc_me_up_ext500.txt"
matchLoc="/work/eg474423/eg474423_Projects/trunk/DendriticCells/Results/DC/motif_enrichment_valleys/results/random_background_e500/"
output_location="--output-location /work/eg474423/eg474423_Projects/trunk/DendriticCells/Results/DC/motif_enrichment_valleys/results/random_background_e500/"
myL = "ME_RAND_UP_500"

# Execution
clusterCommand = "bsub "
clusterCommand += "-J "+myL+" -o "+myL+"_out.txt -e "+myL+"_err.txt "
clusterCommand +="-W 120:00 -M 12000 -S 100 -P izkf -R \"select[hpcwork]\" ./motifAnalysis_pipeline.zsh --enrichment "
clusterCommand += organism+" "+promoter_length+" "+maximum_association_length+" "+multiple_test_alpha+" "
clusterCommand += processes+" "+output_location+" "+print_thresh+" "+bigbed+" "+inputMatrix+" "+matchLoc
os.system(clusterCommand)

##########
### DOWN
##########

# Parameters
inputMatrix="/work/eg474423/eg474423_Projects/trunk/DendriticCells/Results/DC/motif_enrichment_valleys/matrix/dc_me_down_ext500.txt"
matchLoc="/work/eg474423/eg474423_Projects/trunk/DendriticCells/Results/DC/motif_enrichment_valleys/results/random_background_e500/"
output_location="--output-location /work/eg474423/eg474423_Projects/trunk/DendriticCells/Results/DC/motif_enrichment_valleys/results/random_background_e500/"
myL = "ME_RAND_DW_500"

# Execution
clusterCommand = "bsub "
clusterCommand += "-J "+myL+" -o "+myL+"_out.txt -e "+myL+"_err.txt "
clusterCommand +="-W 120:00 -M 12000 -S 100 -P izkf -R \"select[hpcwork]\" ./motifAnalysis_pipeline.zsh --enrichment "
clusterCommand += organism+" "+promoter_length+" "+maximum_association_length+" "+multiple_test_alpha+" "
clusterCommand += processes+" "+output_location+" "+print_thresh+" "+bigbed+" "+inputMatrix+" "+matchLoc
os.system(clusterCommand)


###################################################################################################
# RANDOM BACKGROUND / 1000 EXT
###################################################################################################

##########
### UP
##########

# Parameters
inputMatrix="/work/eg474423/eg474423_Projects/trunk/DendriticCells/Results/DC/motif_enrichment_valleys/matrix/dc_me_up_ext1000.txt"
matchLoc="/work/eg474423/eg474423_Projects/trunk/DendriticCells/Results/DC/motif_enrichment_valleys/results/random_background_e1000/"
output_location="--output-location /work/eg474423/eg474423_Projects/trunk/DendriticCells/Results/DC/motif_enrichment_valleys/results/random_background_e1000/"
myL = "ME_RAND_UP_1000"

# Execution
clusterCommand = "bsub "
clusterCommand += "-J "+myL+" -o "+myL+"_out.txt -e "+myL+"_err.txt "
clusterCommand +="-W 120:00 -M 12000 -S 100 -P izkf -R \"select[hpcwork]\" ./motifAnalysis_pipeline.zsh --enrichment "
clusterCommand += organism+" "+promoter_length+" "+maximum_association_length+" "+multiple_test_alpha+" "
clusterCommand += processes+" "+output_location+" "+print_thresh+" "+bigbed+" "+inputMatrix+" "+matchLoc
os.system(clusterCommand)

##########
### DOWN
##########

# Parameters
inputMatrix="/work/eg474423/eg474423_Projects/trunk/DendriticCells/Results/DC/motif_enrichment_valleys/matrix/dc_me_down_ext1000.txt"
matchLoc="/work/eg474423/eg474423_Projects/trunk/DendriticCells/Results/DC/motif_enrichment_valleys/results/random_background_e1000/"
output_location="--output-location /work/eg474423/eg474423_Projects/trunk/DendriticCells/Results/DC/motif_enrichment_valleys/results/random_background_e1000/"
myL = "ME_RAND_DW_1000"

# Execution
clusterCommand = "bsub "
clusterCommand += "-J "+myL+" -o "+myL+"_out.txt -e "+myL+"_err.txt "
clusterCommand +="-W 120:00 -M 12000 -S 100 -P izkf -R \"select[hpcwork]\" ./motifAnalysis_pipeline.zsh --enrichment "
clusterCommand += organism+" "+promoter_length+" "+maximum_association_length+" "+multiple_test_alpha+" "
clusterCommand += processes+" "+output_location+" "+print_thresh+" "+bigbed+" "+inputMatrix+" "+matchLoc
os.system(clusterCommand)




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

"""
# CDP UP
inputMatrix="/work/eg474423/eg474423_Projects/trunk/DendriticCells/Results/IRF8_PU1_Promoter_Enhancer/ExpMat/MotifEnrichmentUP.txt"
matchLoc="/work/eg474423/eg474423_Projects/trunk/DendriticCells/Results/IRF8_PU1_Promoter_Enhancer/Results/"
output_location="--output-location /work/eg474423/eg474423_Projects/trunk/DendriticCells/Results/IRF8_PU1_Promoter_Enhancer/Results/"
myL = "MEIPEUP"
clusterCommand = "bsub "
clusterCommand += "-J "+myL+" -o "+myL+"_out.txt -e "+myL+"_err.txt "
clusterCommand += "-W 300:00 -M 24000 -S 100 -P izkf -R \"select[hpcwork]\" ./motifAnalysis_pipeline.zsh --enrichment "
clusterCommand += organism+" "+promoter_length+" "+maximum_association_length+" "+multiple_test_alpha+" "
clusterCommand += processes+" "+output_location+" "+print_thresh+" "+bigbed+" "+inputMatrix+" "+matchLoc
os.system(clusterCommand)

# CDP DW
inputMatrix="/work/eg474423/eg474423_Projects/trunk/DendriticCells/Results/IRF8_PU1_Promoter_Enhancer/ExpMat/MotifEnrichmentDOWN.txt"
matchLoc="/work/eg474423/eg474423_Projects/trunk/DendriticCells/Results/IRF8_PU1_Promoter_Enhancer/Results/"
output_location="--output-location /work/eg474423/eg474423_Projects/trunk/DendriticCells/Results/IRF8_PU1_Promoter_Enhancer/Results/"
myL = "MEIPEDW"
clusterCommand = "bsub "
clusterCommand += "-J "+myL+" -o "+myL+"_out.txt -e "+myL+"_err.txt "
clusterCommand += "-W 300:00 -M 24000 -S 100 -P izkf -R \"select[hpcwork]\" ./motifAnalysis_pipeline.zsh --enrichment "
clusterCommand += organism+" "+promoter_length+" "+maximum_association_length+" "+multiple_test_alpha+" "
clusterCommand += processes+" "+output_location+" "+print_thresh+" "+bigbed+" "+inputMatrix+" "+matchLoc
os.system(clusterCommand)
"""

# CDC UP
inputMatrix="/work/eg474423/eg474423_Projects/trunk/DendriticCells/Results/IRF8_PU1_Promoter_Enhancer/ExpMat/cdc_up.txt"
matchLoc="/work/eg474423/eg474423_Projects/trunk/DendriticCells/Results/IRF8_PU1_Promoter_Enhancer/Results/c/"
output_location="--output-location /work/eg474423/eg474423_Projects/trunk/DendriticCells/Results/IRF8_PU1_Promoter_Enhancer/Results/c/"
myL = "MEIPEC"
clusterCommand = "bsub "
clusterCommand += "-J "+myL+" -o "+myL+"_out.txt -e "+myL+"_err.txt "
clusterCommand += "-W 10:00 -M 12000 -S 100 -R \"select[hpcwork]\" ./motifAnalysis_pipeline.zsh --enrichment "
clusterCommand += organism+" "+promoter_length+" "+maximum_association_length+" "+multiple_test_alpha+" "
clusterCommand += processes+" "+output_location+" "+print_thresh+" "+bigbed+" "+inputMatrix+" "+matchLoc
os.system(clusterCommand)
# -P izkf

"""
# PDC UP
inputMatrix="/work/eg474423/eg474423_Projects/trunk/DendriticCells/Results/IRF8_PU1_Promoter_Enhancer/ExpMat/pdc_up.txt"
matchLoc="/work/eg474423/eg474423_Projects/trunk/DendriticCells/Results/IRF8_PU1_Promoter_Enhancer/Results/p/"
output_location="--output-location /work/eg474423/eg474423_Projects/trunk/DendriticCells/Results/IRF8_PU1_Promoter_Enhancer/Results/p/"
myL = "MEIPEP"
clusterCommand = "bsub "
clusterCommand += "-J "+myL+" -o "+myL+"_out.txt -e "+myL+"_err.txt "
clusterCommand += "-W 10:00 -M 12000 -S 100 -R \"select[hpcwork]\" ./motifAnalysis_pipeline.zsh --enrichment "
clusterCommand += organism+" "+promoter_length+" "+maximum_association_length+" "+multiple_test_alpha+" "
clusterCommand += processes+" "+output_location+" "+print_thresh+" "+bigbed+" "+inputMatrix+" "+matchLoc
os.system(clusterCommand)
# -P izkf
"""



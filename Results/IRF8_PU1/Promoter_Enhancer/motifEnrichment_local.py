
# Import
import os

# Parameters
organism="--organism mm9"
promoter_length="--promoter-length 1000"
maximum_association_length="--maximum-association-length 50000"
multiple_test_alpha="--multiple-test-alpha 0.05"
processes="--processes 1"
output_location="--output-location /work/eg474423/eg474423_Projects/trunk/DendriticCells/Results/IRF8_PU1_Promoter_Enhancer/Results/"
print_thresh="--print-thresh 1.0"
bigbed="--bigbed"
matchLoc="/work/eg474423/eg474423_Projects/trunk/DendriticCells/Results/IRF8_PU1_Promoter_Enhancer/Results/"

"""
# Execution 1
inputMatrix="/work/eg474423/eg474423_Projects/trunk/DendriticCells/Results/IRF8_PU1_Promoter_Enhancer/ExpMat/MotifEnrichmentUP.txt"
myL = "MEIPEUP"
clusterCommand = "rgt-motifanalysis --enrichment "
clusterCommand += organism+" "+promoter_length+" "+maximum_association_length+" "+multiple_test_alpha+" "
clusterCommand += processes+" "+output_location+" "+print_thresh+" "+bigbed+" "+inputMatrix+" "+matchLoc+" > "+myL+".txt "
os.system(clusterCommand)

# Execution 2
inputMatrix="/work/eg474423/eg474423_Projects/trunk/DendriticCells/Results/IRF8_PU1_Promoter_Enhancer/ExpMat/MotifEnrichmentDOWN.txt"
myL = "MEIPEDW"
clusterCommand = "rgt-motifanalysis --enrichment "
clusterCommand += organism+" "+promoter_length+" "+maximum_association_length+" "+multiple_test_alpha+" "
clusterCommand += processes+" "+output_location+" "+print_thresh+" "+bigbed+" "+inputMatrix+" "+matchLoc+" > "+myL+".txt "
os.system(clusterCommand)
"""

# Execution 1
inputMatrix="/work/eg474423/eg474423_Projects/trunk/DendriticCells/Results/IRF8_PU1_Promoter_Enhancer/ExpMat/MotifEnrichmentUP.txt"
myL = "MEIPEUP"
clusterCommand = "rgt-motifanalysis --enrichment "
clusterCommand += organism+" "+promoter_length+" "+maximum_association_length+" "+multiple_test_alpha+" "
clusterCommand += processes+" "+output_location+" "+print_thresh+" "+bigbed+" "+inputMatrix+" "+matchLoc+" > "+myL+".txt "
os.system(clusterCommand)

# Execution 2
inputMatrix="/work/eg474423/eg474423_Projects/trunk/DendriticCells/Results/IRF8_PU1_Promoter_Enhancer/ExpMat/MotifEnrichmentDOWN.txt"
myL = "MEIPEDW"
clusterCommand = "rgt-motifanalysis --enrichment "
clusterCommand += organism+" "+promoter_length+" "+maximum_association_length+" "+multiple_test_alpha+" "
clusterCommand += processes+" "+output_location+" "+print_thresh+" "+bigbed+" "+inputMatrix+" "+matchLoc+" > "+myL+".txt "
os.system(clusterCommand)

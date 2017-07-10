
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

#########################################################################################
# Random
# Evidence = Whole set of peaks
# Background = Randomly selected genomic regions
#########################################################################################
"""
# Random
inputMatrix="/work/eg474423/eg474423_Projects/trunk/DendriticCells/Results/DC/motif_enrichment/exp_mat/dc_motifmatch.txt"
matchLoc="/work/eg474423/eg474423_Projects/trunk/DendriticCells/Results/DC/motif_enrichment/result_dc/random/"
output_location="--output-location /work/eg474423/eg474423_Projects/trunk/DendriticCells/Results/DC/motif_enrichment/result_dc/random/"
print "ME_R"
clusterCommand = "rgt-motifanalysis --enrichment "
clusterCommand += organism+" "+promoter_length+" "+maximum_association_length+" "+multiple_test_alpha+" "
clusterCommand += processes+" "+output_location+" "+print_thresh+" "+bigbed+" "+inputMatrix+" "+matchLoc
os.system(clusterCommand)
"""

#########################################################################################
# HS
# Evidence = Whole set of peaks
# Background = HS regions from ENCODE DNase-seq tracks from mm9
#########################################################################################
"""
# HS UP
inputMatrix="/work/eg474423/eg474423_Projects/trunk/DendriticCells/Results/DC/motif_enrichment/exp_mat/dc_up.txt"
matchLoc="/work/eg474423/eg474423_Projects/trunk/DendriticCells/Results/DC/motif_enrichment/result_dc/hs/"
output_location="--output-location /work/eg474423/eg474423_Projects/trunk/DendriticCells/Results/DC/motif_enrichment/result_dc/hs/"
print "ME_HS_UP"
clusterCommand = "rgt-motifanalysis --enrichment "
clusterCommand += organism+" "+promoter_length+" "+maximum_association_length+" "+multiple_test_alpha+" "
clusterCommand += processes+" "+output_location+" "+print_thresh+" "+bigbed+" "+inputMatrix+" "+matchLoc
os.system(clusterCommand)

# HS DOWN
inputMatrix="/work/eg474423/eg474423_Projects/trunk/DendriticCells/Results/DC/motif_enrichment/exp_mat/dc_down.txt"
matchLoc="/work/eg474423/eg474423_Projects/trunk/DendriticCells/Results/DC/motif_enrichment/result_dc/hs/"
output_location="--output-location /work/eg474423/eg474423_Projects/trunk/DendriticCells/Results/DC/motif_enrichment/result_dc/hs/"
print "ME_HS_DOWN"
clusterCommand = "rgt-motifanalysis --enrichment "
clusterCommand += organism+" "+promoter_length+" "+maximum_association_length+" "+multiple_test_alpha+" "
clusterCommand += processes+" "+output_location+" "+print_thresh+" "+bigbed+" "+inputMatrix+" "+matchLoc
os.system(clusterCommand)
"""

#########################################################################################
# Random & Diffpeak
# Evidence = Set of peaks in differential genes (dc up and dc down)
# Background = Randomly selected genomic regions and the set peaks without differential genes
#########################################################################################
"""
# DC UP
inputMatrix="/work/eg474423/eg474423_Projects/trunk/DendriticCells/Results/DC/motif_enrichment/exp_mat/dc_up.txt"
matchLoc="/work/eg474423/eg474423_Projects/trunk/DendriticCells/Results/DC/motif_enrichment/result_dc/random/"
output_location="--output-location /work/eg474423/eg474423_Projects/trunk/DendriticCells/Results/DC/motif_enrichment/result_dc/random_diffpeak/"
print "ME_RD_UP"
clusterCommand = "rgt-motifanalysis --enrichment "
clusterCommand += organism+" "+promoter_length+" "+maximum_association_length+" "+multiple_test_alpha+" "
clusterCommand += processes+" "+output_location+" "+print_thresh+" "+bigbed+" "+inputMatrix+" "+matchLoc
os.system(clusterCommand)

# DC DOWN
inputMatrix="/work/eg474423/eg474423_Projects/trunk/DendriticCells/Results/DC/motif_enrichment/exp_mat/dc_down.txt"
matchLoc="/work/eg474423/eg474423_Projects/trunk/DendriticCells/Results/DC/motif_enrichment/result_dc/random/"
output_location="--output-location /work/eg474423/eg474423_Projects/trunk/DendriticCells/Results/DC/motif_enrichment/result_dc/random_diffpeak/"
print "ME_RD_DW"
clusterCommand = "rgt-motifanalysis --enrichment "
clusterCommand += organism+" "+promoter_length+" "+maximum_association_length+" "+multiple_test_alpha+" "
clusterCommand += processes+" "+output_location+" "+print_thresh+" "+bigbed+" "+inputMatrix+" "+matchLoc
os.system(clusterCommand)
"""

#########################################################################################
# Diffgene
# Evidence = Whole set of peaks
# Background = Set of non-differential peaks in differential gene regions
#########################################################################################
"""
# Parameters
expMatLoc = "/work/eg474423/eg474423_Projects/trunk/DendriticCells/Results/DC/motif_enrichment/exp_mat/"
resLoc = "/work/eg474423/eg474423_Projects/trunk/DendriticCells/Results/DC/motif_enrichment/result_dc/diffgene/"
inList = ["cdc_cdp_up", "cdc_pdc_up", "cdp_mpp_up", "mpp_cdp_up", "pdc_cdc_up", "pdc_cdp_up", 
          "cdc_cdp_down", "cdc_pdc_down", "cdp_mpp_down", "mpp_cdp_down", "pdc_cdc_down", "pdc_cdp_down"]

# Execution
for inCell in inList:

  inputMatrix=expMatLoc+"diffgene_"+inCell+".txt"
  matchLoc=resLoc+inCell+"/"
  output_location="--output-location "+resLoc+inCell+"/"
  print "ME_DG_"+inCell.upper()

  clusterCommand = "rgt-motifanalysis --enrichment "
  clusterCommand += organism+" "+promoter_length+" "+maximum_association_length+" "+multiple_test_alpha+" "
  clusterCommand += processes+" "+output_location+" "+print_thresh+" "+bigbed+" "+inputMatrix+" "+matchLoc
  os.system(clusterCommand)
"""

#########################################################################################
# Random Filtered & Diffpeak
# Evidence = Set of peaks in differential genes (dc up and dc down)
# Background = Randomly selected genomic regions (filtered) and the set peaks without differential genes
#########################################################################################

# DC UP
inputMatrix="/work/eg474423/eg474423_Projects/trunk/DendriticCells/Results/DC/motif_enrichment/exp_mat/dc_up.txt"
matchLoc="/work/eg474423/eg474423_Projects/trunk/DendriticCells/Results/DC/motif_enrichment/result_dc/random_filtered3/"
output_location="--output-location /work/eg474423/eg474423_Projects/trunk/DendriticCells/Results/DC/motif_enrichment/result_dc/random_filtered3/"
print "ME_RFD_UP"
clusterCommand = "rgt-motifanalysis --enrichment "
clusterCommand += organism+" "+promoter_length+" "+maximum_association_length+" "+multiple_test_alpha+" "
clusterCommand += processes+" "+output_location+" "+print_thresh+" "+bigbed+" "+inputMatrix+" "+matchLoc
os.system(clusterCommand)




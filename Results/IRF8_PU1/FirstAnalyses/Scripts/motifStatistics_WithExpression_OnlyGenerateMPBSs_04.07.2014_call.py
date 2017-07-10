
# Import
import os
import sys

#################################################
# Input
#################################################

# Motif list
motifListFileName = "/work/eg474423/eg474423_Projects/trunk/DendriticCells/IRF8_MotifStatistics_Scripts/Input/motifList_04.07.2014.txt"

# Coordinates
coordLocation = "/work/eg474423/ig440396_dendriticcells/exp/diffpeak/res/stats/code_pu1_irf8/"
coordLabel1 = ["CDP_m_PU1_IRF8","CDP_PU1_m_IRF8","CDP_PU1_IRF8"]
coordList1 = ["CDP_m_PU1_IRF8.bed","CDP_PU1_m_IRF8.bed","CDP_PU1_IRF8.bed"]
coordLabel2 = ["cDC_m_PU1_IRF8","cDC_PU1_m_IRF8","cDC_PU1_IRF8",
               "pDC_m_PU1_IRF8","pDC_PU1_m_IRF8","pDC_PU1_IRF8"]
coordList2 = ["cDC_m_PU1_IRF8.bed","cDC_PU1_m_IRF8.bed","cDC_PU1_IRF8.bed",
              "pDC_m_PU1_IRF8.bed","pDC_PU1_m_IRF8.bed","pDC_PU1_IRF8.bed"]

# Gene Lists
geneLocation= "/work/eg474423/ig440396_dendriticcells/exp/diffpeak/expression/"
geneLabel1 = ["irf8_paper_genes"]
geneList1 = ["irf8_paper_genes.txt"]
geneLabel2 = ["irf8_paper_genes"]
geneList2 = ["irf8_paper_genes.txt"]

# Enrichment Input
enrichCoordLabel = [coordLabel1,coordLabel2]
enrichCoordList = [coordList1,coordList2]
enrichGeneLabel = [geneLabel1,geneLabel2]
enrichGeneList = [geneList1,geneList2]

#################################################
# Cluster Call
#################################################

# Enrichment Loop
for i in range(0,len(enrichCoordLabel)):
  
  # Parameters
  coordLabel = enrichCoordLabel[i]
  coordList = enrichCoordList[i]
  geneLabel = enrichGeneLabel[i]
  geneList = enrichGeneList[i]

  # Coordinate Loop
  for c in range(0,len(coordLabel)):

    # Gene List Loop
    for g in range(0,len(geneLabel)):

      ###########################################
      # Parameters
      ###########################################

      coord_file="-coord_file="+coordLocation+coordList[c]
      motif_list="-motif_list="+motifListFileName
      gene_list="-gene_list="+geneLocation+geneList[g]
      #assoc_coord_file="-assoc_coord_file="
      #mpbs_file="-mpbs_file="
      #mpbs_final_file="-mpbs_final_file="

      #genome_list="-genome_list="
      #association_file="-association_file="
      #chrom_sizes_file="-chrom_sizes_file="
      pwm_dataset="-pwm_dataset=/work/eg474423/eg474423_Projects/trunk/DendriticCells/IRF8_MotifStatistics_Scripts/Input/PWM/"
      logo_location="-logo_location=../../../logo/"
      #random_coordinates="-random_coordinates="

      organism="-organism=mm9"
      motif_match_fpr="-motif_match_fpr=0.0001"
      motif_match_precision="-motif_match_precision=10000"
      motif_match_pseudocounts="-motif_match_pseudocounts=0.0"
      multiple_test_alpha="-multiple_test_alpha=0.05"
      promoter_length="-promoter_length=1000"
      maximum_association_length="-maximum_association_length=50000"
      #cobinding="-cobinding="
      #cobinding_enriched_only="-cobinding_enriched_only="
      #enriched_pvalue="-enriched_pvalue="
      rand_proportion_size="-rand_proportion_size=0.1"
      all_coord_evidence="-all_coord_evidence=N"

      outLoc = "/work/eg474423/eg474423_Projects/trunk/DendriticCells/MotifStatistics/IRF8_PU1_WithExp_OnlyMPBSforNetwork_04.07.2014/"+coordLabel[c]+"__"+geneLabel[g]+"/"
      os.system("mkdir -p "+outLoc)
      output_location="-output_location="+outLoc
      print_association="-print_association=Y"
      print_mpbs="-print_mpbs=Y"
      print_results_text="-print_results_text=Y"
      print_results_html="-print_results_html=Y"
      print_enriched_genes="-print_enriched_genes=N"
      print_rand_coordinates="-print_rand_coordinates=Y"
      print_graph_mmscore="-print_graph_mmscore=N"
      print_graph_heatmap="-print_graph_heatmap=N"

      ###########################################
      # Execution
      ###########################################

      # Label: E = enrichment | Y = expression | 0407 = 04.07
      myL = "EY0407_"+coordLabel[c]+"_"+geneLabel[g]
      clusterCommand = "bsub "
      clusterCommand += "-J "+myL+" -o "+myL+"_out.txt -e "+myL+"_err.txt "
      clusterCommand += "-W 330:00 -M 20000 -S 100 -P izkf -R \"select[hpcwork]\" ./motifStatistics_pipeline.zsh "
      clusterCommand += coord_file+" "+motif_list+" "+gene_list+" "+pwm_dataset+" "+logo_location+" "
      clusterCommand += organism+" "+motif_match_fpr+" "+motif_match_precision+" "+motif_match_pseudocounts+" "+multiple_test_alpha+" "
      clusterCommand += promoter_length+" "+maximum_association_length+" "+rand_proportion_size+" "+all_coord_evidence+" "
      clusterCommand += output_location+" "+print_association+" "+print_mpbs+" "+print_results_text+" "+print_results_html+" "
      clusterCommand += print_enriched_genes+" "+print_rand_coordinates+" "+print_graph_mmscore+" "+print_graph_heatmap
      os.system(clusterCommand)



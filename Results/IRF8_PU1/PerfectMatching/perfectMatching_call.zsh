#!/bin/zsh

##########################################################################
### Perfect Matching for IRF8/PU1 motifs
##########################################################################

# Parameters
spacerList="1,2,3"
motifInputFileName="/work/eg474423/eg474423_Projects/trunk/DendriticCells/PerfectMatching/Input/IRF_ETS.txt"
randomFileName="/work/eg474423/eg474423_Projects/trunk/DendriticCells/PerfectMatching/Input/Random/random.bed"
genomeFileName="/hpcwork/izkf/projects/egg/Data/MM9/mm9.fa"
outputLocation="/work/eg474423/eg474423_Projects/trunk/DendriticCells/PerfectMatching/Results/ETS_IRF/"
cl="/work/eg474423/eg474423_Projects/trunk/DendriticCells/PerfectMatching/Input/Coordinates/"
rl="/work/eg474423/eg474423_Projects/trunk/DendriticCells/PerfectMatching/Input/Random/"
coordList=( "pu1_mpp_irf8_summit_500.bed" "pu1_cdp_irf8_summit_500.bed" "pu1_cdc_irf8_summit_500.bed"
            "pu1_pdc_irf8_summit_500.bed" "irf8_dup_summits_500_4.bed" 
            "mpp_cdp_pu1.bed" "cdp_mpp_pu1.bed" "cdc_pdc_pu1.bed" "pdc_cdc_pu1.bed" 
            "mpp_pu1_irf8_up_summit_final.bed" "cdp_pu1_irf8_up_summit_final.bed"
            "cdc_pu1_irf8_up_summit_final.bed" "pdc_pu1_irf8_up_summit_final.bed" )

# Coordinate Loop
for cn in $coordList
do

    #cn=${coordinateFileName:t:r}
    bsub -J $cn"_PM" -o $cn"_PM_out.txt" -e $cn"_PM_err.txt" -W 100:00 -M 12000 -S 100 -P izkf -R "select[hpcwork]" ./perfectMatching_pipeline.zsh $spacerList $motifInputFileName $cl$cn $randomFileName $genomeFileName $outputLocation
    
done



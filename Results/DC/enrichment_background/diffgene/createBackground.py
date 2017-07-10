
# Import
import os
import sys
from rgt.GenomicRegion import GenomicRegion
from rgt.GenomicRegionSet import GenomicRegionSet
from rgt.GeneSet import GeneSet

# Input
pl = "/work/eg474423/ig440396_dendriticcells/exp/diffpeakdc/diff/res/"
gl = "/work/eg474423/ig440396_dendriticcells/exp/diffpeakdc/expression/"
ol = "/work/eg474423/eg474423_Projects/trunk/DendriticCells/Results/DC/enrichment_background/diffgene/"
allPeaksFileName = "/work/eg474423/eg474423_Projects/trunk/DendriticCells/Results/DC/enrichment_background/diffgene/all_PU1_peaks.bed"
inPairs = [
(pl+"cdc_cdp_pu1.bed",gl+"cdp_cdc_1_under.txt"),
(pl+"pdc_cdp_pu1.bed",gl+"cdp_pdc_1_under.txt"),
(pl+"mpp_cdp_pu1.bed",gl+"mpp_cdp_1_under.txt"),
(pl+"cdp_mpp_pu1.bed",gl+"mpp_cdp_1_over.txt"),
(pl+"pdc_cdc_pu1.bed",gl+"pdc_cdc_1_under.txt"),
(pl+"cdc_pdc_pu1.bed",gl+"cdc_pdc_1_under.txt")
]

# Iterating on pairs
for pair in inPairs:
  
  # Initialization
  peakFileName = pair[0]
  geneFileName = pair[1]
  peakName = peakFileName.split("/")[-1].split(".")[0]
  outUnchangedFileName = ol+peakName+"_unchanged.bed"
  outEvFileName = ol+peakName+"_unchanged_ev.bed"
  outNevFileName = ol+peakName+"_unchanged_nev.bed"

  # Creating unchanged file
  os.system("intersectBed -wa -v -a "+allPeaksFileName+" -b "+peakFileName+" > "+outUnchangedFileName)

  # Creating gene set
  g = GeneSet("gs")
  geneFile = open(geneFileName,"r")
  for line in geneFile:
    g.genes.append(line.strip())
  geneFile.close()

  # Creating genomic region
  grs = GenomicRegionSet("grs")
  grs.read_bed(outUnchangedFileName)

  # Associating with genes
  grsa = grs.gene_association(g, "mm9")

  # Writing output
  outEvFile = open(outEvFileName,"w")
  outNevFile = open(outNevFileName,"w")
  for gr in grsa:
    genes = gr.name.split(":")
    flagEv = False
    for e in genes:
      if(e[0]!="."):
        flagEv = True
        break
    if(flagEv): outEvFile.write("\t".join([gr.chrom,str(gr.initial),str(gr.final)])+"\n")
    else: outNevFile.write("\t".join([gr.chrom,str(gr.initial),str(gr.final)])+"\n")
  outEvFile.close()
  outNevFile.close()



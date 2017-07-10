
# Import
library(lattice)
library(reshape)
library(plotrix)
w2l <- function(xx) melt(xx, measure.vars = colnames(xx))

# Parameters
inLoc = "/work/eg474423/eg474423_Projects/trunk/DendriticCells/Results/DC/filter_statistics/result/"
mar.default <- c(8,5,4,2)

median.data.frame <- function(x, na.rm=TRUE) {
   sapply(x, function(y, na.rm=FALSE) if(is.factor(y)) NA else
median(y, na.rm=na.rm), na.rm=na.rm)
}

mean.data.frame <- function(x, na.rm=TRUE) {
   sapply(x, function(y, na.rm=FALSE) if(is.factor(y)) NA else
mean(y, na.rm=na.rm), na.rm=na.rm)
}

# BOXPLOT
createBoxplot <- function(inFileName, yLab, yLim, ablineVec, factor, outFileName){

  dataFrame = read.table(inFileName, header=TRUE)
  dataFrame = dataFrame[,c(1,3,2)]
  dataFrame = dataFrame * factor
  #colnames(dataFrame) <- c("PU.1", "New\nRandom\nBackground","Old\nRandom\nBackground")
  colnames(dataFrame) <- c("A", "B", "C")
  test_df2 <- w2l(dataFrame)

  meds = round(median.data.frame(dataFrame), digits = 4)

  #postscript(outFileName,width=8.0,height=5.0,horizontal=FALSE,paper='special')
  pdf(outFileName,width=8.0,height=3.0,paper='special')
  par(cex.axis=1.0)
  p = bwplot(value ~ variable, data = test_df2,
             scales=list(
               tck=0, 
               x=list(rot=0,cex=1.0, col="black"), 
               y=list(cex=1.0), at=ablineVec, labels=rep("",length(ablineVec))),
             col = "black",
             main = "", xlab = "", ylab = list(yLab,cex=1.0), ylim=yLim,
             par.settings = list( 
               plot.symbol=list(col = "black", alpha = 0.1),
               box.rectangle = list(col = "black"),
               box.dot = list(col = "black"), 
               box.umbrella= list(lty=1, col = "black")),
             panel=function(...) {
               panel.abline(h=ablineVec,lty=2,lwd=1.0,col="gray") 
               panel.bwplot(...)
               #panel.text(c(1,2,3,4,5,6)-0.1, 0.95*yLim[2], rot=90, labels = meds)
               #panel.axis(side = "top",labels = meds, rot=0, outside=TRUE)
             })
  print(p)
  #plot(c(1,2,3,4,5,6),c(rep(yLim[1],3),rep(yLim[2],3)))
  #text(c(1,2,3,4,5,6), rep(yLim[2],6), labels=meds, cex= 0.3)
  #mtext("AAAAA", at = 1, cex = 1.0)
  dev.off()
  #system(paste("epstopdf",outFileName,sep=" "))
  #system(paste("rm",outFileName,sep=" "))

}

# PAIRED T-TEST
hypTest <- function(inFileName, outFileName){

  dataFrame = read.table(inFileName, header=TRUE)
  methodNameVec = colnames(dataFrame)

  toWrite = c("XXXXX",methodNameVec)
  for (i in (1:ncol(dataFrame))){
    toWrite = c(toWrite,methodNameVec[i])
    for (j in (1:ncol(dataFrame))){
      if(i == j){
        toWrite = c(toWrite,"XXXXX")
      }
      else{
        teste = wilcox.test(dataFrame[,i],dataFrame[,j],paired=FALSE)
        toWrite = c(toWrite,format(teste$p.value,digits=5))
      }
    }
  }
  write(toWrite,file=outFileName,ncolumns=ncol(dataFrame)+1,append=FALSE,sep='\t')

}

# CpG
#createBoxplot(paste(inLoc,"table_cpg.txt",sep=""),"CpG Content (%)",c(-1,25),c(0,5,10,15,20),100,paste(inLoc,"cpg.pdf",sep=""))
createBoxplot(paste(inLoc,"table_cpg.txt",sep=""),"",c(-1,25),c(0,5,10,15,20),100,paste(inLoc,"cpg_woLabel.pdf",sep=""))
hypTest(paste(inLoc,"table_cpg.txt",sep=""),paste(inLoc,"cpg.txt",sep=""))

# Map
#createBoxplot(paste(inLoc,"table_map.txt",sep=""),"Unmappable Regions (%)",c(-1,40),c(0,10,20,30),100,paste(inLoc,"map.pdf",sep=""))
createBoxplot(paste(inLoc,"table_map.txt",sep=""),"",c(-1,40),c(0,10,20,30),100,paste(inLoc,"map_woLabel.pdf",sep=""))
hypTest(paste(inLoc,"table_map.txt",sep=""),paste(inLoc,"map.txt",sep=""))

# Black
#createBoxplot(paste(inLoc,"table_blk.txt",sep=""),"Blacklisted Regions (%)",c(-1,9),c(0,2,4,6,8),100,paste(inLoc,"blk.pdf",sep=""))
createBoxplot(paste(inLoc,"table_blk.txt",sep=""),"",c(-1,9),c(0,2,4,6,8),100,paste(inLoc,"blk_woLabel.pdf",sep=""))
hypTest(paste(inLoc,"table_blk.txt",sep=""),paste(inLoc,"blk.txt",sep=""))



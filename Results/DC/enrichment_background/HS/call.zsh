#!/bin/zsh

bsub -J "BB" -o "BB_out.txt" -e "BB_err.txt" -W 24:00 -M 60000 -S 100 -P izkf -R "select[hpcwork]" ./pipeline.zsh



#!/usr/bin/env bash
source /opt/intel/mkl/bin/mklvars.sh intel64
for i in {1..5}
do
  time Rscript benchmark-gcbd.R
  time Rscript benchmark-revolution.R
  time Rscript benchmark-sample.R
  time Rscript benchmark-urbanek.R
done

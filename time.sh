#!/usr/bin/env bash
source /opt/intel/mkl/bin/mklvars.sh intel64
for i in {1..5}
do
  time ~/R-3.5.1/bin/Rscript benchmark-gcbd.R
  time ~/R-3.5.1/bin/Rscript benchmark-revolution.R
  time ~/R-3.5.1/bin/Rscript benchmark-sample.R
  time ~/R-3.5.1/bin/Rscript benchmark-urbanek.R
done

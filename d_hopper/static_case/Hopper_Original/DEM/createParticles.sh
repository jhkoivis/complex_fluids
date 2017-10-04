#!/bin/bash
#SBATCH --time=00-04:00:00
#SBATCH -p short
#SBATCH -o log.dat
#SBATCH -e errorlog.log
#SBATCH -n 48
#SBATCH -N 4


mpirun -np 48 $CFDEM_LIGGGHTS_SRC_DIR/lmp_$CFDEM_LIGGGHTS_MAKEFILE_NAME < in.liggghts_init

#!/bin/bash
#SBATCH --time=05-00:00:00
#SBATCH -p batch
#SBATCH -o log2.log
#SBATCH -e errorlog2.log
#SBATCH --constraint=[wsm|hsw|ivb]
#SBATCH -n 96
#SBATCH -N 8
#SBATCH --mem-per-cpu=750

cd ./CFD
mpirun -np 96 cfdemSolverPiso -parallel

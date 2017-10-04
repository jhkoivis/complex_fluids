#!/bin/bash
#SBATCH --time=05-00:00:00
#SBATCH -p batch
#SBATCH -o log3.log
#SBATCH -e errorlog3.log
#SBATCH --constraint=[wsm|hsw|ivb]
#SBATCH -n 96
#SBATCH -N 8
#SBATCH --mem-per-cpu=750

cd ./CFD
decomposePar
mpirun -np 96 cfdemSolverPiso -parallel

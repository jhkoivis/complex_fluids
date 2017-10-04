#!/bin/bash

# This script is used to calculate the fraction of particles that have their z-coordinates below zero (Hopper problem).
# Requires input: 1: the number of particles and 2: the LAMMPS (standard) ASCII dump file, where the 6th column corresponds to z-coordinate 

for dirs in "${@:2}"
do
tail -n $1 "$dirs" > temp.dat
awk '{print $6}' temp.dat > temp2.dat
count=$(grep -c ^-0 temp2.dat)
foo=${dirs#d*p}
foo=${foo%h*r}
echo -n "${foo} "
echo "scale=10; $count/$1" | bc
rm temp.dat
rm temp2.dat
done
  
 

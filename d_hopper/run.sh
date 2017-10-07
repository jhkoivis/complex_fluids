#!/bin/bash
#SBATCH -p batch
#SBATCH --time=05-00:00:00
#SBATCH --exclusive
#SBATCH --constraint=hsw
#SBATCH --ntasks=48
#SBATCH --mem-per-cpu=1500

particle_diameter_in_um=$1

# check that cores is the same as the --ntasks above (6th line)
cores=48


case_folder=d_hopper_$particle_diameter_in_um
root_dir=`pwd`
case_dir=$root_dir/$case_folder
log_dir=$case_dir/logs


###########################################
# prepare case
###########################################

mkdir -p old_cases
mv $case_folder $root_dir/old_cases/case_folder.`date +%s`

mkdir -p $case_dir
cp -r $root_dir/static_case/Hopper_Altered/* $case_dir/

mkdir -p $log_dir


############################################
# cleanup
############################################
cd $case_dir
make clean

###########################################
# split to processors
##########################################

python 	$root_dir/static_case/tools/replace_strings.py \
	$case_dir/CFD/system/decomposeParDict \
	numberOfSubdomains \
	numberOfSubdomains\ $cores\;

cd $case_dir/CFD
decomposePar 	>  $log_dir/01_decomposePar.stdout.log \
		2> $log_dir/01_decomposePar.stderr.log

###########################################
# Alter partcile number and size
###########################################

python 	$root_dir/static_case/tools/replace_particle_size_and_number.py \
	$case_dir/DEM/in.liggghts_init \
	$particle_diameter_in_um

python  $root_dir/static_case/tools/replace_particle_size_and_number.py \
        $case_dir/DEM/in.liggghts_run \
        $particle_diameter_in_um

###########################################
# insert particles to DEM side
###########################################

cd 	$case_dir/DEM

srun    -p batch \
        --time=05-00:00:00 \
        --exclusive \
        --constraint=hsw \
        --ntasks=$cores \
        --mem-per-cpu=1500 \
	$CFDEM_LIGGGHTS_SRC_DIR/lmp_$CFDEM_LIGGGHTS_MAKEFILE_NAME < in.liggghts_init \
	>  $log_dir/02_liggghts_init.stdout.log \
	2> $log_dir/02_liggghts_init.stderr.log

###########################################
# start coupled simulation
###########################################

cp 	$case_dir/DEM/liggghts_init.restart $case_dir/DEM/liggghts.restart

cd 	$case_dir/CFD

srun    -p batch \
        --time=05-00:00:00 \
        --exclusive \
        --constraint=hsw \
        --ntasks=$cores \
        --mem-per-cpu=1500 \
        cfdemSolverPiso -parallel \
        >  $log_dir/03_cfdem_run.stdout.log \
        2> $log_dir/03_cfdem_run.stderr.log



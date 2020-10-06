#!/bin/bash
#BSUB -J Src_T338I_Perror_0.25_100k
#BSUB -n 1
#BSUB -R span[ptile=1]
#BSUB -R rusage[mem=8]
#BSUB -W 12:00
#BSUB -o %J.stdout
#BSUB -eo %J.stderr

# make sure job’s submission CWD path can be accessed on the job’s execution host 
cd $LS_SUBCWD

# Activate the environment where Assaytools is installed
source activate assaytools_af411f0

# Export current conda environment requirements
conda list --export > requirements.txt

# Run my program
echo “Started running Assaytools...”
quickmodel --inputs inputs_multiple_well_single_wv_Src_T338I_4ligs --type singlet --nsamples 100000
echo “Done.”

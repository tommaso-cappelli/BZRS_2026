#!/bin/bash

#SBATCH --job-name=cov.sf0nf
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=2G
#SBATCH --time=03:00:00
#SBATCH --qos=6hours
#SBATCH --output=/scicore/home/nimwegen/cappel0001/BZRS_PROJECT/breseq_test/score0_freq0_nf/txt_outputs_cov/output_%A_%a.txt
#SBATCH --error=/scicore/home/nimwegen/cappel0001/BZRS_PROJECT/breseq_test/score0_freq0_nf/errors_cov/err_%A_%a.txt
#SBATCH --mail-type=END,FAIL,TIME_LIMIT
#SBATCH --mail-user=tommaso.cappelli@unibas.ch
#SBATCH --array=0-20%11

ml purge
ml SAMtools/1.22.1-GCC-14.2.0

script_path='/scicore/home/nimwegen/cappel0001/BZRS_PROJECT/breseq_test/input_files/cov_csvfiles.py'
tsv_path='/scicore/home/nimwegen/cappel0001/BZRS_PROJECT/breseq_test/input_files/breseq_samples_stdpar.txt'

python -u "$script_path" \
        --dataset_path "$tsv_path" \
        --row_index "$SLURM_ARRAY_TASK_ID" \
        --pars_folder "score0_freq0_nf"
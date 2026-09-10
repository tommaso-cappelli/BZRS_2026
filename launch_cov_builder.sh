#!/bin/bash

#SBATCH --job-name=cov.freq0_score0_nofilters
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=2G
#SBATCH --time=03:00:00
#SBATCH --qos=6hours
#SBATCH --output=/scicore/home/nimwegen/cappel0001/BZRS_PROJECT/mixed_samples_breseq/freq0_score0_nofilters/txt_outputs_cov/output_%A_%a.txt
#SBATCH --error=/scicore/home/nimwegen/cappel0001/BZRS_PROJECT/mixed_samples_breseq/freq0_score0_nofilters/errors_cov/err_%A_%a.txt
#SBATCH --mail-type=END,FAIL,TIME_LIMIT
#SBATCH --mail-user=tommaso.cappelli@unibas.ch
#SBATCH --array=0-477%10

ml purge
ml SAMtools/1.22.1-GCC-14.2.0

script_path='/scicore/home/nimwegen/cappel0001/BZRS_PROJECT/mixed_samples_breseq/input_files/cov_csvfiles.py'
csv_path='/scicore/home/nimwegen/cappel0001/BZRS_PROJECT/mixed_samples_breseq/input_files/mixed_df_breseq.csv'

python -u "$script_path" \
        --dataset_path "$csv_path" \
        --row_index "$SLURM_ARRAY_TASK_ID" \
        --pars_folder "freq0_score0_nofilters"
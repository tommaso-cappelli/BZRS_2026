#!/bin/bash

#SBATCH --job-name=400.breseq
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=2G
#SBATCH --time=05:59:59
#SBATCH --qos=6hours
#SBATCH --output=/scicore/home/nimwegen/cappel0001/BZRS_PROJECT/mixed_samples_breseq/stdpar/outputs/output__%A_%3a.txt
#SBATCH --error=/scicore/home/nimwegen/cappel0001/BZRS_PROJECT/mixed_samples_breseq/stdpar/errors/error__%A_%3a.txt
#SBATCH --mail-type=END,FAIL,TIME_LIMIT
#SBATCH --mail-user=tommaso.cappelli@unibas.ch

#SBATCH --array=400-477%20

ml purge
ml breseq/0.38.1-foss-2022a
export LMOD_DISABLE_SAME_NAME_AUTOSWAP=no

script_path="/scicore/home/nimwegen/cappel0001/BZRS_PROJECT/mixed_samples_breseq/input_files/single_breseq.py"
csv_path="/scicore/home/nimwegen/cappel0001/BZRS_PROJECT/mixed_samples_breseq/input_files/mixed_df_breseq.csv"
freq_par="0.05"
score_par="2"
# The -u flag tells Python not to buffer the output
python -u "$script_path" \
        --master_csv_path "$csv_path" \
        --row_index "$SLURM_ARRAY_TASK_ID" \
        --frequency_cutoff "0.025" \
        --score_cutoff "1"
        
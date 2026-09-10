#!/bin/bash

#SBATCH --job-name=bam2cov_stdpar
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=2G
#SBATCH --time=03:00:00
#SBATCH --qos=6hours
#SBATCH --output=/scicore/home/nimwegen/cappel0001/BZRS_PROJECT/breseq_test/stdpar/txt_outputs/output_BAM2COV_TABLES_%A_%3a.txt
#SBATCH --error=/scicore/home/nimwegen/cappel0001/BZRS_PROJECT/breseq_test/stdpar/errors/err_BAM2COV_TABLES_%A_%3a.txt
#SBATCH --mail-type=END,FAIL,TIME_LIMIT
#SBATCH --mail-user=tommaso.cappelli@unibas.ch

#SBATCH --array=0-20%11

ml breseq/0.38.1-foss-2022a
export LMOD_DISABLE_SAME_NAME_AUTOSWAP=no

script_path='/scicore/home/nimwegen/cappel0001/BZRS_PROJECT/breseq_test/input_files/bamcovtables.py'
tsv_path='/scicore/home/nimwegen/cappel0001/BZRS_PROJECT/breseq_test/input_files/samples_data.txt'

# The -u flag tells Python not to buffer the output
python -u "$script_path" \
        --dataset_path "$tsv_path" \
        --row_index "$SLURM_ARRAY_TASK_ID"
#!/bin/bash

#SBATCH --job-name=master.csv
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=2G
#SBATCH --time=03:00:00
#SBATCH --qos=6hours
#SBATCH --output=/scicore/home/nimwegen/cappel0001/BZRS_PROJECT/mixed_samples_breseq/input_files/output_mastercsv.txt
#SBATCH --error=/scicore/home/nimwegen/cappel0001/BZRS_PROJECT/mixed_samples_breseq/input_files/err_mastercsv.txt
#SBATCH --mail-type=END,FAIL,TIME_LIMIT

ml SciPy-bundle/2026.05-gfbf-2026.1

script_path='/scicore/home/nimwegen/cappel0001/BZRS_PROJECT/mixed_samples_breseq/input_files/master_csv.py'
csv_path='/scicore/home/nimwegen/bojani0000/20260520-strain-deconvolution/real_data/modified_metadata.csv'

# The -u flag tells Python not to buffer the output
python -u "$script_path" \
        --dataset_path "$csv_path" \
        --strain_frequency_threshold "0.1"

        
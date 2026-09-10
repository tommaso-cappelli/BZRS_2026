#!/bin/bash

#SBATCH --job-name=intra_lineage_comparison
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=1G
#SBATCH --time=01:00:00
#SBATCH --qos=6hours
#SBATCH --output=/scicore/home/nimwegen/cappel0001/BZRS_PROJECT/breseq_test/score1_freq10/lineages_comp/output.txt
#SBATCH --error=/scicore/home/nimwegen/cappel0001/BZRS_PROJECT/breseq_test/score1_freq10/lineages_comp/err.txt
#SBATCH --mail-type=END,FAIL,TIME_LIMIT
#SBATCH --mail-user=tommaso.cappelli@unibas.ch

ml breseq/0.38.1-foss-2022a
export LMOD_DISABLE_SAME_NAME_AUTOSWAP=no

script_path="/scicore/home/nimwegen/cappel0001/BZRS_PROJECT/breseq_test/input_files/compare_lineages.py"
# The -u flag tells Python not to buffer the output
python -u "$script_path"

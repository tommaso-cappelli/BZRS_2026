#FULL GENOME TABLES FOR THE COVERAGE

import subprocess  #Starting from the previous code for a single file, let's modify this one in order to work with a single csv file and work with a single line 
#for each parallel script
import argparse
import sys
import pandas as pd
import os
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument('--dataset_path') #what I'm getting from here is the csv/tsv-like file that has a sample name and its reference genome path
parser.add_argument('--row_index') #what I'm getting from here is the index of the row that I want to analyze in a single iteration

args = parser.parse_args()

idx = int(args.row_index) #saving the index in a variable
tmp_dataset = pd.read_csv(args.dataset_path)
sample_taken = tmp_dataset.loc[idx] #dataset with one single row, basically

main_folder = '/scicore/home/nimwegen/cappel0001/BZRS_PROJECT/breseq_test/score0_freq0_nf/'+ sample_taken['Sample_name'].replace('_', '-') + '-breseq/data/'

ref_input = main_folder + 'reference.fasta'
bam_file = main_folder + 'reference.bam'

csv_cov_file = main_folder + 'coverage.csv'
csv_coverage = pd.read_csv(csv_cov_file, sep = '\t', names = ['Contig', 'Position', 'Coverage'])
contig_lengths = csv_coverage.groupby(by='Contig')['Position'].max()
outdir = main_folder + '/bam2cov_table/'
os.makedirs(outdir, exist_ok=True)

targets = [f"{contig}:1-{length}" for contig, length in contig_lengths.items()]

for contig, length in contig_lengths.items():
    outfile = os.path.join(outdir, f"{contig}_coverage")
    target = f"{contig}:1-{length}"
    
    cmd = [
        "breseq", "BAM2COV",
        "-t",
        "--resolution", "0",        # Number of bins = number of base pairs
        "-b", bam_file,
        "-f", ref_input,
        "-o", outfile,
        target
    ]

    try:
        # check=True forces Python to raise an error if the command fails
        res = subprocess.run(cmd, capture_output=True, text=True, check=True)
        print(res.stdout)
    except subprocess.CalledProcessError as e:
        print(f"BAM2COV failed with error code {e.returncode}")
        print(f"Standard Error output:\n{e.stderr}")
        sys.exit(1)
    except Exception as e:
        # This catches literally any other crash (like breseq not being found)
        print(f"A different Python error occurred: {e}")
        sys.exit(1)
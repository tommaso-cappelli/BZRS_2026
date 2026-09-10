import argparse
import sys
import pandas as pd
import json
import ast
import csv
import subprocess
import os
parser = argparse.ArgumentParser()
parser.add_argument('--master_csv_path') #what I'm getting from here is the csv file with sample_name, condition (etc) pathway in the original plots as well)
parser.add_argument('--row_index')
parser.add_argument('--frequency_cutoff', default='0.05') #I'll set the minimum frequency that a strain should have in order to be considered for the breseq algorithm
parser.add_argument('--score_cutoff', default = '2')
args = parser.parse_args()

idx = int(args.row_index)
df = pd.read_csv(args.master_csv_path)

if args.frequency_cutoff == '0.05' and args.score_cutoff == '2':
    par_summary = 'stdpar'
else:
    par_summary = f'freq{args.frequency_cutoff}_score{args.score_cutoff}'

outdir = '/scicore/home/nimwegen/cappel0001/BZRS_PROJECT/mixed_samples_breseq/'+par_summary+'/'+df.iloc[idx]['sample']+'/'+df.iloc[idx]['strain']+'/'+df.iloc[idx]['condition']

cmd = ["breseq", "-p", "--polymorphism-score-cutoff", args.score_cutoff, "--polymorphism-frequency-cutoff", args.frequency_cutoff,"-r", df.iloc[idx]['ref_file'], "-o", outdir, "-j", "1", df.iloc[idx]['fastq1'], df.iloc[idx]['fastq2']]

try:
    # check=True forces Python to raise an error if the command fails
    res = subprocess.run(cmd, capture_output=True, text=True, check=True)
    print(res.stdout)
except subprocess.CalledProcessError as e:
    print(f"Breseq failed with error code {e.returncode}")
    print(f"Standard Error output:\n{e.stderr}")
    sys.exit(1)
except Exception as e:
    # This catches literally any other crash (like breseq not being found)
    print(f"A different Python error occurred: {e}")
    sys.exit(1)








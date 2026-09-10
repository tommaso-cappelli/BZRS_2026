#BUILDS THE COVERAGE CSV FILE FOR EACH BP

import subprocess
import argparse
import sys
import csv # Replaced pandas with Python's built-in csv module

parser = argparse.ArgumentParser()
parser.add_argument('--dataset_path')
parser.add_argument('--row_index')
parser.add_argument('--pars_folder')
args = parser.parse_args()
idx = int(args.row_index)

# Open and read the CSV file using built-in Python tools
with open(args.dataset_path, mode='r', encoding='utf-8') as f:
    # If your file is actually tab-separated, change to: csv.DictReader(f, delimiter='\t')
    reader = csv.DictReader(f, delimiter=',') 
    dataset = list(reader) #here the dataset will have a different format (master_df_breseq.csv)
    breseq_run = dataset[idx]

ref = breseq_run['ref_file']
sample_name = breseq_run['sample']
strain = breseq_run['strain']
condition = breseq_run['condition']

ref_folder =('/scicore/home/nimwegen/cappel0001/BZRS_PROJECT/mixed_samples_breseq/'+args.pars_folder+'/'+sample_name+'/'+strain+'/'+condition+'/data/')
bam_file = ref_folder + 'reference.bam'
cov_csv = ref_folder + 'coverage.csv'

cmd = ['samtools', 'depth', '-a', bam_file]

try:
    # Open the target CSV file in 'write' mode
    with open(cov_csv, "w") as out_file:
        # Route standard output (stdout) directly into the file
        res = subprocess.run(cmd, stdout=out_file, stderr=subprocess.PIPE, text=True, check=True)
        print(f"Successfully generated coverage for row {idx}: {sample_name}")

except subprocess.CalledProcessError as e:
    print(f"Samtools failed with error code {e.returncode}")
    print(f"Standard Error output:\n{e.stderr}")
    sys.exit(1)
except Exception as e:
    print(f"A different Python error occurred: {e}")
    sys.exit(1)
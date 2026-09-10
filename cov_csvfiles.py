#BUILDS THE PLOTS FOR THE TOTAL MEAN COVERAGE OF 100-BP-LONG BINS FOR EACH SAMPLE, and the samples for each lineage are plotted one next to each other.


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
    dataset = list(reader)
    
    # Get the specific row (0-indexed, excluding the header)
    sample_taken = dataset[idx]

ref = sample_taken['ref_genome']
sample_name = sample_taken['sample_name']

ref_folder = '/scicore/home/nimwegen/cappel0001/BZRS_PROJECT/breseq_test/' + args.pars_folder + '/' + sample_name + '-breseq/data/'
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
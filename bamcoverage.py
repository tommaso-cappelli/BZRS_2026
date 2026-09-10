#BUILDS THE COVERAGE PLOTS OF THE PREDICTED MUTATIONS FOR EVERY SINGLE SAMPLE ANALYZED

import subprocess  #Starting from the previous code for a single file, let's modify this one in order to work with a single csv file and work with a single line 
#for each parallel script
import argparse
import sys
import pandas as pd
import os

parser = argparse.ArgumentParser()
parser.add_argument('--dataset_path') #what I'm getting from here is the csv/tsv-like file that has a sample name and its reference genome path
parser.add_argument('--row_index') #what I'm getting from here is the index of the row that I want to analyze in a single iteration

args = parser.parse_args()



idx = int(args.row_index) #saving the index in a variable
tmp_dataset = pd.read_csv(args.dataset_path)
sample_taken = tmp_dataset.loc[idx] #dataset with one single row, basically

main_folder = '/scicore/home/nimwegen/cappel0001/BZRS_PROJECT/breseq_test/stdpar/'+ sample_taken['sample_name'] + '-breseq'
outdir = main_folder + '/data/bam2coverage/'
os.makedirs(outdir, exist_ok=True)

ref_input = main_folder + '/data/reference.fasta'
bam_file = main_folder + '/data/reference.bam'

max_expected_columns = 70
column_names = [f"col_{i}" for i in range(max_expected_columns)]
annotated_file = pd.read_csv(main_folder+'/data/annotated.gd', sep = '\t', names = column_names, comment='#')
predicted_mutations = annotated_file[annotated_file['col_0']=='SNP']

if predicted_mutations.empty:
    print(f"No SNPs found for sample {sample_taken['sample_name']}. Exiting.")
    sys.exit(0)
    
starting = (predicted_mutations['col_4']-500).clip(lower=1).astype(str)
ending = (predicted_mutations['col_4']+500).astype(str)
regions = (starting+'-'+ending).reset_index(drop=True)
contigs = predicted_mutations['col_3'].reset_index(drop=True)
targets_r  = (contigs + ':' + regions).to_list()


cmd = ["breseq", "BAM2COV", "-b", bam_file, "-f", ref_input, "-o", outdir] + targets_r

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


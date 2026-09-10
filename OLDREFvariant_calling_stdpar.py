import subprocess  #Starting from the previous code for a single file, let's modify this one in order to work with a single csv file and work with a single line 
#for each parallel script
import argparse
import sys
import pandas as pd

#HERE, WE ARE NOT DIRECTLY USING THE METADATA THAT DEFINES THE LINEAGES, THE REFERENCE BETWEEN B8 AND H1 (no path), and all the other features.
#We  only have to upload the file with the correctly formatted sample_name and its reference genome (B8/H1)

parser = argparse.ArgumentParser()
parser.add_argument('--dataset_path') #what I'm getting from here is the csv/tsv-like file that has a sample name and its reference genome path
parser.add_argument('--row_index') #what I'm getting from here is the index of the row that I want to analyze in a single iteration

args = parser.parse_args()

og_folder = '/scicore/home/nimwegen/peruzz0000/Growth_var/Succinate_DNAseq_202607/Microsynth_raw_data/Short_reads/4793919_2026_07_15_05_46_07_corr/' #folder that contains ALSO the fastq files for each sample

idx = int(args.row_index) #saving the index in a variable
tmp_dataset = pd.read_csv(args.dataset_path)
sample_taken = tmp_dataset.loc[idx] #dataset with one single row, basically

ref = sample_taken['ref_genome'] #I do get the reference genome path in thia way


outdir = '/scicore/home/nimwegen/cappel0001/BZRS_PROJECT/breseq_test/stdpar/'+ sample_taken['sample_name'] + '-breseq'

in1 = og_folder + sample_taken['sample_name'] + '.IlluminaPolishing/' + sample_taken['sample_name'] + '_R1.fastq.gz'
in2 = og_folder + sample_taken['sample_name'] + '.IlluminaPolishing/' + sample_taken['sample_name'] + '_R2.fastq.gz'

cmd = ["breseq", "-p", "-r", ref, "-o", outdir, "-j", "1", in1, in2]

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
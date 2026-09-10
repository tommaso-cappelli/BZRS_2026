import argparse
import sys
import pandas as pd
import json
import ast
import csv

#HERE, WE ARE NOT DIRECTLY USING THE METADATA THAT DEFINES THE LINEAGES, THE REFERENCE BETWEEN B8 AND H1 (no path), and all the other features.
#We only have to upload the file with the correctly formatted sample_name and its reference genome (B8/H1)

parser = argparse.ArgumentParser()
parser.add_argument('--dataset_path') #what I'm getting from here is the csv file with sample_name, condition (etc) pathway in the original plots as well)
parser.add_argument('--strain_frequency_threshold') #I'll set the minimum frequency that a strain should have in order to be considered for the breseq algorithm
args = parser.parse_args()
breseq_input_folder = '/scicore/home/nimwegen/bojani0000/20260806-dna-rna-deconvolution-pipeline/breseq_strain_assignment_pipeline/OUTPUT_breseq_assignment/fastq/'
ref_folder = '/scicore/home/nimwegen/bojani0000/Gene_clustering_algorithms/pan-genome-analysis/data/E_coli_backup4/input_GenBank/'
metadata = pd.read_csv(args.dataset_path)
master_csv = [['sample', 'strain', 'ref_file', 'condition', 'fastq1', 'fastq2', 'growth_media', 'og_strains','day', 'well']]
for idx in range(len(metadata)):
    sample_name = metadata.iloc[idx]['sample']
    well = sample_name.rstrip('DAYS_1234567890').strip('-')
    day = metadata.iloc[idx]['Day']
    growth_media = metadata.iloc[idx]['Condition']
    strains_iter = ast.literal_eval(metadata.iloc[idx]['strains']) #ast in order to format correctly
    #now let's get the actual strains to be analyzed
    strains = []
    results_folder = "/scicore/home/nimwegen/bojani0000/20260520-strain-deconvolution/real_data/results_first_round/"
    sample_results = results_folder + sample_name +'.json' #.json file with the estimated frequencies by Tamara's alorithm
    with open(sample_results, 'r') as f:
        json_file = json.load(f)
        for strain in strains_iter:
            if json_file['results']['em']['frequencies'][strain]>=float(args.strain_frequency_threshold):
                strains.append(strain) #only significant strains remain, that have at least the frequency threshold of the whole population of the sample
    

    for s in strains:
        ref_file = ref_folder + s + '_pilon_round_4_annotated.gbk'
        for condition in ['strict', 'permissive']:
            in1 = breseq_input_folder + sample_name + '/' + s + '.' + condition + '_R1.fastq.gz'
            in2 = breseq_input_folder + sample_name + '/' + s + '.' + condition + '_R2.fastq.gz'
            tmp_list =[sample_name, s, ref_file, condition, in1, in2, growth_media, strains_iter, day, well]
            master_csv.append(tmp_list)

master_csv_df = pd.DataFrame(data=master_csv[1:], index=list(range(0, len(master_csv)-1)), columns = master_csv[0])
master_csv_df.to_csv(path_or_buf="/scicore/home/nimwegen/cappel0001/BZRS_PROJECT/mixed_samples_breseq/input_files/mixed_df_breseq.csv")


    
            
            


        
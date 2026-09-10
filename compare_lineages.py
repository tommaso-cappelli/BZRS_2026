import subprocess  #Starting from the previous code for a single file, let's modify this one in order to work with a single csv file and work with a single line 
#for each parallel script
import argparse
import sys
import pandas as pd
import os

print("DEBUG: THE SCRIPT HAS SUCCESSFULLY UPDATED!2")

#WE SHOULD RUN A PROGRAM THAT COMPARES EACH LINEAGE: therefore instead of running multiple parallel jobs for this we should probably upload the dict_lineages we've already created for the test_plots, since we've already built all the lines of code to extract the data
parameters = 'score1_freq10'

metadata = pd.read_csv('/scicore/home/nimwegen/bojani0000/20260808-succinate-data/Succinate_samples_AP_202607_metadata.csv') #read the data labelling each well

metadata['Sample_name'] = metadata['Sample_name'].str.replace('_','-') #fix the names to be suitable for your dataset

n_lineages = max(metadata['Lineage'].fillna(0).astype(int)) #set the number

dict_lineages = {}

GDTOOLS_PATH = "/scicore/soft/apps/breseq/0.38.1-foss-2022a/bin/gdtools"

for i in range(1, int(n_lineages+1)):
    dict_lineages.update({i:metadata[metadata['Lineage']==i]})  #divide the metadata through the indexes

#let's start to create the elements to send gd.compare: output files, reference genome, input .gd files

for i in dict_lineages.keys():

    comparison_file = '/scicore/home/nimwegen/cappel0001/BZRS_PROJECT/breseq_test/'+parameters+'/lineages_comp/comp_lineage_'+str(i)+'.html' #output file

    strain_involved = dict_lineages[i]['Strain'].iloc[0] 

    ref_file = '/scicore/home/nimwegen/bojani0000/Gene_clustering_algorithms/pan-genome-analysis/data/E_coli_backup4/input_GenBank/'+strain_involved+'_pilon_round_4_annotated.gbk'
    #we have to select the comparison meter for EACH lineage, not for each sample: it seems pretty useless to force the user to select each time an index to select a sample

    preculture_gd_file = '/scicore/home/nimwegen/cappel0001/BZRS_PROJECT/breseq_test/'+parameters+'/Pre-culture-'+strain_involved+'-breseq/output/output.gd' 

    comp_input = [preculture_gd_file] #let's put the 

    sample_paths = '/scicore/home/nimwegen/cappel0001/BZRS_PROJECT/breseq_test/'+parameters+'/'+dict_lineages[i]['Sample_name']+'-breseq/output/output.gd' #let's get the paths for all the samples of each lineage

    for j in range(len(sample_paths)):

        comp_input.append(sample_paths.iloc[j])

    cmd = ["gdtools", "COMPARE", "-o", comparison_file, "-r", ref_file, *comp_input]

    try:
        # check=True forces Python to raise an error if the command fails
        res = subprocess.run(cmd, capture_output=True, text=True, check=True, env=os.environ)
        print(res.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Breseq failed with error code {e.returncode}")
        print(f"Standard Error output:\n{e.stderr}")
        sys.exit(1)
    except Exception as e:
        # This catches literally any other crash (like breseq not being found)
        print(f"A different Python error occurred: {e}")
        sys.exit(1)    

    

    

    

        

    
     

    


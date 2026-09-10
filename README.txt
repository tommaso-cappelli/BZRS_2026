
recophy_project folder contains the 1st week work that I've done in order to get comfortable with data analysis using python,
NumPy, Matplotlib and Pandas, trying to replicate the results inside the Recophy database for E.Coli through customizable inputs for the plots.

The starting file is a 92 rows x 2.5M+ columns, with each row representing a strain and each column a base of the core genome of E.Coli. The file was filtered, deleting columns with more than 2 unique letters inside them, in order to be binarized (0->no SNP, 1->SNP).

The analysis features both the comparison of 2 strains with 2.5M+ bases per core genome (core_genomic_evolution.ipynb). 
Furthermore, patterns_snps.ipynb tries to compare all the bases of these 2.5 million genes in order to identify common patterns in therms of allele variation frequency (if a certain number of mutations appear more often, and whether if they also involve the same strains. Then, given an extremely low chance that a SNP can happen more than once on the same gene along the evolutionary tree, the 4-gamete-test was implemented to detect clashes and understanding the impact of recombination inside the evolution of E.Coli genome.



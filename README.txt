The files in this repository contain all the coding in python and sh files I have done during my Biozentrum Research Summer in Erik van Nimwegen's lab, whose focus is the analysis, visualization and Mathematical modelling of the dynamics of genome evolution.
I've mainly worked with E.Coli strains, both on short term and long term evolutionary dynamics.
---------------------------------------------------------------------------------------------------------------------------------
recophy_project folder contains the 1st week work that I've done in order to get comfortable with data analysis using python,
NumPy, Matplotlib and Pandas, trying to replicate the results inside the Recophy database for E.Coli through customizable inputs for the plots.

The starting file is a 92 rows x 2.5M+ columns, with each row representing a strain and each column a base of the core genome of E.Coli. The file was filtered, deleting columns with more than 2 unique letters inside them, in order to be binarized (0->no SNP, 1->SNP).

The analysis features both the comparison of 2 strains with 2.5M+ bases per core genome (core_genomic_evolution.ipynb). 
Furthermore, patterns_snps.ipynb tries to compare all the bases of these 2.5 million genes in order to identify common patterns in therms of allele variation frequency (if a certain number of mutations appear more often, and whether if they also involve the same strains. Then, given an extremely low chance that a SNP can happen more than once on the same gene along the evolutionary tree, the 4-gamete-test was implemented to detect clashes and understanding the impact of recombination inside the evolution of E.Coli genome.
-------------------------------------------------------------------------------------------------------------------------------
mixedsamples_growthandcov.ipynb is then focused on a dataset created by Tamara Bojanic from the NGS reads obtained from samples in different growth medias and with mixed strains among them. This algorithm would create through an iterative process, starting from all the unassigned reads and the reference genomes, both a estimation of the frequency of each strain inside the sample and the mean coverage for each 1000bp bin inside the genomes. The plots try to compare the coverage of mixed, multi-strain samples with the coverage of reference samples to look out for artifacts, viral DNA expression; also, the last two notebooks create plots that try to compare the avg expected coverage versus the actual coverage each sample showcases.
--------------------------------------------------------------------------------------------------------------------------------
On these samples, breseq was run in polymorphism mode with the deafult parameters, in order to understand the compatibility of this tool to a multi strain sample and/or adjust the algorithm that assigns each read to certain strains. 
To verify these features, the plots showcased for the CHL samples the frequencies or the e-values on the y-axis, with the coverages on the x-axis, for each mutation. The coverages profiles were built for each strain separately to other input files, and they include the contig, the position of each base and its total coverage in # of strain, since these aren't given automatically by breseq unless BAM2COV is run for all of them. 
To find duplication/deletions, the mean coverage for each 100bp was plotted as well.

For each sample, the issues of running breseq for a single sample with one strain at the time was showcased in the last plot, where on the x-axis it was shown Shannon's entropy of each sample with the strain indicated above 10%, whereas on the y-axis it was shown the number of total variants detected by breseq, that was rising significantly when the sample was more and more mixed
--------------------------------------------------------------------------------------------------------------------------------
In breseq_suc_plots.ipynb, these same plots were showcased for the data with samples coming from a single strain that were mutating while switching media every 10 generations. Here, the plots were run with read aligment as the variation type to be analyzed, in order to confirm the veridicity of mutation by looking at the same comparison listed in the previous paragraph.
The plots were created both with breseq results with default filters and with no filter applied.

The statistics that were analyzed were the consistency of the frequencies of JC and RA found along the pre culture and the 3 samples for each lineage, in order to understand whether these variations cloud be realistically possible or if there could be some high frequency artifact. Then, the coverage plots were plotted, along with the scatterplots frequency-coverage, e-value-coverage, frequency-relative position. Histograms for frequencies were also plotted for samples with no filters.

Whereas for H1 there were some concerning results by looking at the frequency of each mutation, highlighting consistent incoherence among the lineages, the results from B8 were encouraging. A breif summary has been shown in the .pptx file about it.

The last plots  were created through the resultsthe BAM2COV pipeline, included in breseq: the goal was to find a relationship with the H1 variant Issues and the way breseq maps repeated coverage.



Special thanks to Erik van Nimwegen, Tamara Bojanic, Ludovico Calabrese and Alberto Peruzzi.

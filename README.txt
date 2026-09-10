The files in this repository contain all the coding in python and sh files I have done during my Biozentrum Research Summer in Erik van Nimwegen's lab, whose focus is the analysis, visualization and Mathematical modelling of the dynamics of genome evolution.
I've mainly worked with E.Coli strains, both on short term and long term evolutionary dynamics.
---------------------------------------------------------------------------------------------------------------------------------
recophy_project folder contains the 1st week work that I've done in order to get comfortable with data analysis using python,
NumPy, Matplotlib and Pandas, trying to replicate the results inside the Recophy database for E.Coli through customizable inputs for the plots.
-------------------------------------------------------------------------------------------------------------------------------
mixed_samples is then focused on a dataset created by Tamara Bojanic from the NGS reads obtained from samples in different growth medias and with mixed strains among them. On these samples, breseq was run in polymorphism mode with the deafult parameters, in order to understand its compatibility of this tool with a multi strain sample, while adjusting the algorithm that assigns each read to one or more strains. 

For each sample, the issues of running breseq for a single sample with one strain at the time was showcased in the last plot, where on the x-axis it was shown Shannon's entropy of each sample with the strain indicated above 10%.
--------------------------------------------------------------------------------------------------------------------------------
In succinate_samples, these same plots (except for entropy's) were showcased for the data with samples coming from a single strain that were mutating while switching media every 10 generations. Here, the plots were run with read aligment as the variation type to be analyzed, in order to confirm the veridicity of mutation by looking at the same comparison listed in the previous paragraph.

The last plots  were created through the resultsthe BAM2COV pipeline, included in breseq: the goal was to find a relationship with the H1 variant Issues and the way breseq maps repeated coverage.

--------------------------------------------------------------------------------------------------------------------------------------------

Special thanks to Erik van Nimwegen, Tamara Bojanic, Ludovico Calabrese and Alberto Peruzzi.

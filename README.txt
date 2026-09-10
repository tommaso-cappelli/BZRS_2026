In succinate_samples, these same plots used in mixed_samples were showcased for the data with samples coming from a single strain that were mutating while switching media every 10 generations. Here, the plots were run with read aligment as the variation type to be analyzed, in order to confirm the veridicity of mutation by looking at the same comparison listed in the previous paragraph.
The plots were created both with breseq results with default filters and with no filter applied.

The statistics that were analyzed were the consistency of the frequencies of JC and RA found along the pre culture and the 3 samples for each lineage, in order to understand whether these variations cloud be realistically possible or if there could be some high frequency artifact. Then, the coverage plots were plotted, along with the scatterplots frequency-coverage, e-value-coverage, frequency-relative position. Histograms for frequencies were also plotted for samples with no filters.

Whereas for H1 there were some concerning results by looking at the frequency of each mutation, highlighting consistent incoherence among the lineages, the results from B8 were encouraging. A breif summary has been shown in the .pptx file about it.

The last plots  were created through the resultsthe BAM2COV pipeline, included in breseq: the goal was to find a relationship with the H1 variant Issues and the way breseq maps repeated coverage.

# NotchDynamics_SCLC

## Goals
What is the status of genes/proteins in the Notch pathway in different datasets?
1.	Bulk and single cell RNA on human cell lines
    1. 	Do they match up?
    2.	Are there significant drop outs in the single cell data?
    3.	Do mutations in Notch pathway genes correspond to expression levels across subtypes?
2.	Fluidigm data on Hes1-GFP mouse tumor cells (single cell)
    1.	When grouping by Hes1 GFP level, what do the different Notch’s look like? 
    2.	What about other reporters of phenotype, like ASCL1?
3.	RPM time series data
    1.	How do Notch genes change over time in this dataset?
1.	RNA velocity: are there differential kinetics across subtypes for Notch genes in the human and mouse single cell data?
    1.	Are there differential kinetics across the 6 timepoints in the RPM data? i.e. does transcription/degradation rate change between timepoints?
    2.	Are there different kinetics in each of the cell lines? If so, do mutations affect this? (i.e. find mutational info on each cell line and compare mutational status) 
    3.	Can we integrate these fitted parameters into the mechanistic PySB model?
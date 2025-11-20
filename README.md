# Proteosim Course Package

## Package description
This repository provides a simulation framework for mass-spectrometry–based proteomics experiments. It focuses on modeling protein digestion, LCiquid chromatography, realistic MS1/MS2 spectra as well as ion fragmentation of peptides. The code is under active development and is continuously being expanded and improved.

``` mermaid
flowchart LR
    A[proteins sequence] --> B[protein digestion]
    B --> C[fragments]
    C --> D[simulated liquid chromatography]
    E --> F[select peptides]
    F --> G[simulate MS1]
    G --> H[fragmentation]
    H --> I [simulate MS2]
```

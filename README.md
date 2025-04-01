# Breast Cancer Variant Benchmark Dataset

This repository contains the code and processed data for constructing a benchmark dataset of breast cancer-related missense variants, annotated with functional prediction scores and population allele frequencies.

## Project Description
This project aims to support the evaluation and interpretation of pathogenicity prediction models (e.g., MetaRNN, MVP, M-CAP) by providing a standardized, high-confidence dataset.

## Data Sources
- **ClinVar**: GRCh38 VCF release 2024-03-23
- **dbNSFP v5.1a**: Functional scores and conservation metrics

## Tools Used
- [Ensembl VEP](https://www.ensembl.org/info/docs/tools/vep/index.html) with Docker
- dbNSFP plugin for VEP
- Python (Pandas)
- PowerShell (on Windows) / Docker CLI

## How to Reproduce the Dataset
1. Prepare `clinvar_bc_variants_for_vep.vcf` using filtering criteria:
   - SNV only, genes: BRCA1, BRCA2, TP53, ATM, CHEK2
   - Clinical significance: Pathogenic / Benign
   - Breast cancer-related entries only
2. Annotate using VEP (with dbNSFP plugin and specified score fields)
3. Run the Python script to extract selected fields into CSV

## License
MIT License

---
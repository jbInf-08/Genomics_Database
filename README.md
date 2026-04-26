# GenomicsDatabase
[![CI](https://github.com/jbInf-08/Genomics_Database/actions/workflows/ci.yml/badge.svg)](https://github.com/jbInf-08/Genomics_Database/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

## Golden path

```bash
pip install -r requirements-lock.txt
python version_check.py
python genomics_system.py --load-csv data/METABRIC_RNA_Mutation.csv
```

This system is designed to facilitate the storage, retrieval, and analysis of cancer genomic data. Researchers can input genomic sequences, mutation data, and patient metadata for analysis. The system supports querying, visualization, and reporting functionalities to enhance cancer genomics research.

Features

User Management: Add, update, and delete patient records.

Genomic Data Handling: Store and analyze gene sequences and mutations.

Mutation Analysis: Detect and track cancer-related mutations.

Visualization: Generate bar charts and heatmaps for gene expression analysis.

Data Persistence: Save data in a PostgreSQL database or JSON format.

Command-Line Interface: Simple interactive CLI for users.

Data Import: Load datasets from CSV files.

Error Handling & Validation: Ensures data integrity and proper format.

Installation

Prerequisites

Ensure you have the following installed:

Python 3.8+

pip (Python package manager)

PostgreSQL (Optional, for database storage)

Dependencies

Run the following command to install required Python libraries:
pip install -r requirements.txt

Usage

Running the System

Clone the repository:
https://github.com/jbInf-08/Genomics_Database.git

Navigate to the project directory:
cd GenomicsDatabase

Run the main program:
python genomics_system.py

Follow on-screen instructions to add, query, and visualize genomic data.

Data Import from CSV

**Provenance (METABRIC).** The METABRIC cohort is from primary literature, not from Kaggle as the authoritative source. Cite the original studies, for example:

- Curtis C, *et al.* (2012). The genomic and transcriptomic architecture of 2,000 breast tumours. *Nature* **486**:400–407. [doi:10.1038/nature11243](https://doi.org/10.1038/nature11243) — describes the METABRIC design and the combined copy-number / expression resource.
- Pereira B, *et al.* (2016). The somatic mutation profiles of 2,433 breast cancers refine their genomic and transcriptomic landscapes. *Nat. Commun.* **7**:11479. [doi:10.1038/ncomms11479](https://doi.org/10.1038/ncomms11479) — targeted sequencing and mutation–clinical associations on METABRIC tumours (relevant if your table includes somatic calls linked to the same programme).

A **Kaggle mirror** is convenient for download only, e.g. [Breast cancer gene expression profiles (METABRIC)](https://www.kaggle.com/datasets/raghadalharbi/breast-cancer-gene-expression-profiles-metabric?resource=download); always refer to the papers above in manuscripts and supervision.

Download the file you need (e.g. from Kaggle) and save it as `data/METABRIC_RNA_Mutation.csv` in the project directory (the `data/` folder is git-ignored so large datasets are not committed).

Run:
python genomics_system.py --load-csv data/METABRIC_RNA_Mutation.csv

Testing

To verify system functionality, run:
python version_check.py
This script will check Python version, dependencies, and dataset accessibility.

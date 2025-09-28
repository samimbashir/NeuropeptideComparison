# Neuropeptide Comparison

A Python tool to compare neuropeptides against reference databases and output only the matched peptides.

## Features

- Accepts input peptides (FASTA)
- Compares against reference database (FASTA)
- Outputs matched peptides (FASTA)
- Simple CLI interface
- Supports large datasets using efficient pandas operations

## Usage

```
python neuropeptide_compare.py \
  --input data/input_peptides.fasta \
  --reference data/reference_db.fasta \
  --output data/matched_peptides.fasta
```

## Installation

Requires Python 3.7+
```
pip install pandas biopython
```

## Example

Sample data is provided in the `data/` folder.

## License

MIT

## Author

Samim Bashir

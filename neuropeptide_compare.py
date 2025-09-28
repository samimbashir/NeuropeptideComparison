import argparse
from Bio import SeqIO

def parse_fasta(file_path):
    return {str(record.seq): record.id for record in SeqIO.parse(file_path, "fasta")}

def write_fasta(seqs, output_path):
    with open(output_path, "w") as out_f:
        for seq, id_ in seqs.items():
            out_f.write(f">{id_}\n{seq}\n")

def main():
    parser = argparse.ArgumentParser(description="Compare neuropeptides to reference DB and output matched peptides.")
    parser.add_argument('--input', required=True, help='Input peptides FASTA file')
    parser.add_argument('--reference', required=True, help='Reference database FASTA file')
    parser.add_argument('--output', required=True, help='Output matched peptides FASTA file')
    args = parser.parse_args()

    input_peptides = parse_fasta(args.input)
    reference_db = set(parse_fasta(args.reference).keys())

    matched = {seq: input_peptides[seq] for seq in input_peptides if seq in reference_db}

    write_fasta(matched, args.output)
    print(f"Matched {len(matched)} peptides. Results written to {args.output}")

if __name__ == "__main__":
    main()
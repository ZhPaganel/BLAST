import random
import Bio
from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML

'''# intro question
intro = input('Do you want the program to generate a NA sequence or paste your own one? Paste/Generate ')

# defining variables
gen_code_dna = ['a', 't', 'g', 'c']
gen_code_rna = ['a', 'u', 'g', 'c']
seq = []

if intro == 'Generate' or intro == 'generate':
    nc_type = input("Please, enter the type of nucleic acid: ")
    nc_length = int(input("Please, enter the size of the sequence: "))
    if nc_type == "DNA" or nc_type == "dna":
        seq = random.choices(gen_code_dna, k=nc_length)
    elif nc_type == "RNA" or nc_type == "rna":
        seq = random.choices(gen_code_rna, k=nc_length)
    new_seq = ''.join(seq)
else:
    new_seq = input('Please, paste your sequence in FASTA format: ')

print(new_seq)
'''

file = open('seq.fasta', 'w')
fasta = file.write(new_seq)
file.close()

file1 = open('seq.fasta', 'r')
fasta1 = file1.read()
blast = NCBIWWW.qblast('blastn', 'nt', fasta1)
record = NCBIXML.read(blast)
print(len(record.alignments))

e_value_thresh = 0.01
for alignment in record.alignments:
    for hsp in alignment.hsps:
        if hsp.expect < e_value_thresh:
            print('***Alignment***')
            print('sequence: ', alignment.title)
            print('length: ', alignment.length)
            print('e value: ', hsp.expect)
            print(hsp.query)
            print(hsp.match)
            print(hsp.sbjct)


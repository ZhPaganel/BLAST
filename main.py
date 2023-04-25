import random
import Bio
from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML

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


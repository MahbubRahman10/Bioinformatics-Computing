#these are biopython module
from Bio.Seq import Seq     
from Bio import SeqIO    
from Bio.SeqRecord import SeqRecord

def first_fifty_bases(file_path):
    f=open(file_path, 'r')
    records=SeqIO.parse(f,'fasta')
    record=next(records)
    print(record.id)
    print(record.seq[:50])
    print(record.description)
    print(record.seq.reverse_complement()[:50])
    
first_fifty_bases('C:\\Users\\HP\\Desktop\\BIC\\sequence.fasta')
    
#these are biopython module
from Bio.Seq import Seq    
from Bio import SeqIO    
from Bio.SeqRecord import SeqRecord

def first_fifty_bases(file_path):
    f=open(file_path, 'r')
    records=SeqIO.parse(f,'fasta')
    record=next(records)
   
    count={'A':0, 'T':0, 'G':0, 'C':0}
    
    for i in record:
        count[i]+=1
    return count

first_fifty_bases('C:\\Users\\HP\\Desktop\\BIC\\sequence.fasta')
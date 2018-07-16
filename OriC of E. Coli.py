#these are biopython module
from Bio.Seq import Seq
from Bio import SeqIO    
from Bio.SeqRecord import SeqRecord

def file_to_str(file_path):
    f=open(file_path, 'r')
    records=SeqIO.parse(f,'fasta')
    record=next(records)
    rec=record.seq[:50]
    print("Genome Length:",len(record))
    plot(record)
    
import matplotlib.pyplot as plt    

def plot(str):
    count={'A':0, 'T':0, 'G':0, 'C':0}
    g,c=0,0
    data=[]

    for i in str:
        if i=='G':
            g+=1
        elif i=='C':
            c+=1
        
        data.append(g-c)        
    plt.plot(data)
    plt.show()
    
dna=file_to_str('C:\\Users\\HP\\Desktop\\BIC\\sequence.fasta')
def complement(dna):
    count={'A':'T','T':'A', 'G':'C','C':'G'}
    new=[]
    for n in dna:
       new.append(count[n])
       result = ''.join(new)
    return result
        
dna="AATCCGAT"
my=complement(dna)
print(my)
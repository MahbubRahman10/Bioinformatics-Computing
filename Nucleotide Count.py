
def nucleotide_count(dna):
    A,T,C,G=0,0,0,0
    
    for n in dna:
        if n=='A':
            A+=1
        elif n=='T':
            T+=1
        elif n=='C':
            C+=1
        elif n=='G':
            G+=1
            
    return A,T,C,G

dna="ATTCGAACCC"
a,t,c,g=nucleotide_count(dna)

print("A:", a, "T:", t,"C:", c, "G:", g)



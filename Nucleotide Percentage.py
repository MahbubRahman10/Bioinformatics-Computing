def percentage(dna):
    a,t,c,g=0,0,0,0

    for n in dna:
        if n=='A':
            a+=1
        elif n=='T':
            t+=1
        elif n=='G':
            g+=1
        elif n=='C':
            c+=1
            
    return a,t,g,c

dna="AATCATGCCC"

p,q,r,s=percentage(dna)
p*=len(dna)
p/=100
q*=len(dna)
q/=100
r*=len(dna)
r/=100
s*=len(dna)
s/=100

print("A:", p, "T:", q,"C:", r, "G", s)
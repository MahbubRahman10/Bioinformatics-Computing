def revcomplement(dna):
    count={'A':'T','T':'A', 'G':'C','C':'G'}
    data=[]
    for n in dna:
       data.append(count[n])
       result = ''.join(data)
       output = result[::-1]
    return output
        
rev=revcomplement("AATCATGCCC")
print(rev)
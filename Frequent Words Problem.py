def frequent_word(str,k):
    count = {}
    for i in range(0,len(str)-k+1):
        kmer=str[i:i+k]
        if kmer in count:
            count[kmer]+=1
        else:
            count[kmer]=1
        fre=max(count.values())
    for k in count:
        if count[k]==fre:
             print(k)
kmeans=4
dna="ACGTTGCATGTCGCATGATGCATGAGAGCT"
frequent_word(dna,kmeans)
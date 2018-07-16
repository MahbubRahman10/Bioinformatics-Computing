def hamming(str1, str2):
    dist=0;
    for i in range(0, len(str1)):
        if str1[i]!=str2[i]:
            dist+=1
    return dist
        
str1="GGGCCGTTGGT"
str2="GGACCGTTGAC"
hamming(str1, str2)
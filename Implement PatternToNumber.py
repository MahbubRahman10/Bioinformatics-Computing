def pattern_to_number(st):
    st1=[]
	
    for i in range(0, len(st)):
        if st[i]=="A":
            st1.append(0)        
        elif st[i]=="C":
            st1.append(1)
        elif st[i]=="G":
            st1.append(2)
        elif st[i]=="T":
            st1.append(3)
			
    k=len(st1)       
    c=0
    for j in st1[:]:
        k-=1
        print(k)
        c+=j*4**k
    return c

s='AGT'
pattern_to_number(s)
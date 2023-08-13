l=[]
s="are you ready to join with hakunamatata"
k=s.split()[::-1]
print(' '.join(k))
for i in k:
    l.append(' '.join(sorted(i)))
print('   '.join(sorted(l)))

s1="kannan"
s2="kamal"
c=0
for i in range(len(s1)):
    for j in range(len(s2)):
        if(s1[i]==s2[j]):
            c+=1
            s1.replace(s1[i],"#")
            s2.replace(s2[j],"#")
            break;
print(c)
            


f=open('tem.txt','r')

name=f.readlines()
index=0
index_n=1
fw=open('tem-'+str(index_n)+'.txt','w')
for line in name:
    index=index+1
    if index%100==0:
        index_n=index_n+1
        fw=open('tem-'+str(index_n)+'.txt','w')
    fw.write(line)



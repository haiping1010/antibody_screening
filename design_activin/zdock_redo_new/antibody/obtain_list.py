import shutil, random, os
#filenames = random.sample(os.listdir(dirpath), 4000)
import glob
aa=glob.glob("*_antibody.pdb")
##filenames = random.sample(os.listdir(dirpath), 3)
#filenames = random.sample(aa, 3)

fw=open("tem.txt", "w")
print (fw.name)

for pname in aa:
    lname='1nysB_antigen.pdb'
    fw.write(lname+" "+ pname+"\n")

fw.close()

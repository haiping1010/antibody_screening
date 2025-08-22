import shutil, random, os
random.seed(1)
dirpath='/home/zhanghaiping/program/antibody_new_data/zdock_redo_new'
#filenames = random.sample(os.listdir(dirpath), 4000)
import glob
os.chdir(dirpath+'/antigen')
aa=glob.glob("*.pdb")
##filenames = random.sample(os.listdir(dirpath), 3)
#filenames = random.sample(aa, 3)
os.chdir(dirpath+'/antibody')
bb=glob.glob("*.pdb")

os.chdir(dirpath)
fw=open("tem.txt", "w")
print (fw.name)

for pname in aa:
  filenames = random.sample(bb, 6)
  for lname in filenames:
      while pname[:4] == lname[:4]:
          tem=random.sample(bb, 1)
          lname=tem[0]      
      fw.write(pname+"  "+ lname+"\n")
#      fw.write(str(pname))
#      fw.write("1")
   #srcpath = os.path.join(dirpath, fname)
   #disfile=os.path.join(destDirectory, fname)
   #shutil.copyfile(srcpath, disfile)

fw.close()

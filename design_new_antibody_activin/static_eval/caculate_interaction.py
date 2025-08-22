import sys
import numpy as np
from sklearn.cluster import KMeans
import numpy as np
from sklearn.cluster import KMeans

      
visited = {}
HLposition={}
Eposition={}
ResinameHL={}
ResinameE={}
antiface=[]
residuePair=[]
if len(sys.argv) <2 :
   print("python python2.py xxx.pdb")

import glob
filex=sys.argv[1]
#filey=sys.argv[2]

#file1=glob.glob(filex)
#1nysB_6nmrAB
#print (file1[0])
#file='4R2GPQ_antibody.pdb'
##filebase=file.replace("_","")
for line in open(filex):
    tem_B=' '
    if len(line)>16:
       tem_B=line[16]
       line=line[:16]+' '+line[17:]
    #print(line)
    list_n = line.split()
    id = list_n[0]
    if id == 'ATOM' and tem_B !='B'  :
        tem_arr=filex.split('-')
        chain_antibody=tem_arr[0][10:]
        if len(tem_arr[0][10:])==1:
               chain_antibody='H'
        elif len(tem_arr[0][10:])==2:
               chain_antibody='HL'
        type = list_n[2]
        if list_n[3]!= 'UNK' and line[21:22] in list(chain_antibody):
            residue = list_n[3]
            type_of_chain = line[21:22]
            tem1=line[22:26].replace("A", "")
            tem2=tem1.replace("B", "")
            tem2=tem2.replace("C", "")

            atom_count = tem2+line[21:22]
            list_n[6]=line[30:38]
            list_n[7]=line[38:46]
            list_n[8]=line[46:54]
            position = list_n[6:9]
            HLposition[atom_count]=position
            ResinameHL[atom_count]=residue+line[21:26]


##filebase=file2.replace("_","")
for line in open(filex):
    tem_B=' '
    if len(line)>16:
       tem_B=line[16]
       line=line[:16]+' '+line[17:]
    #print(line)
    list_n = line.split()
    id = list_n[0]
    if id == 'ATOM' and tem_B !='B':
        tem_arr=filex.split('-')
        #chain_antigen=tem_arr[0][6:7]
        chain_antigen='A'
        type = list_n[2]
        if    list_n[3]!= 'UNK' and  line[21:22] in list(chain_antigen):
            residue = list_n[3]
            type_of_chain = line[21:22]
            tem1=list_n[5].replace("A", "")
            tem2=tem1.replace("B", "")
            tem2=tem1.replace("C", "")
            atom_count = tem2+line[21:22]
            list_n[6]=line[30:38]
            list_n[7]=line[38:46]
            list_n[8]=line[46:54]
            position = list_n[6:9]
            Eposition[atom_count]=position
            ResinameE[atom_count]=residue+line[21:26]

all_pair=[]
tem_neighbor=[]
HL_res=[]
for key1, value1 in HLposition.items():
   for key2, value2 in Eposition.items():
            a = np.array(value1)
            a1 = a.astype(np.float)
            b = np.array(value2)
            b1 = b.astype(np.float)
            xx=np.subtract(a1,b1) 
            tem=np.square(xx)
            tem1=np.sum(tem)
            #out=np.sqrt(tem1)
            #print out
            if tem1<36 :
                tem_neighbor.append([ResinameHL[key1], ResinameE[key2]])
                HL_res.append(ResinameHL[key1])
                #print out
   #print  (ResinameHL[key1],tem_neighbor)

   #fo = open(filex+'_'+filey+"_summary.txt", "w")

#tem_neighbor=list(set(tem_neighbor))
unique_tuples = set(tuple(item) for item in tem_neighbor)
tem_neighbor = [list(item) for item in unique_tuples]
HL_res=list(set(HL_res))

dict_load=np.load('dict_energy.npy', allow_pickle=True).item()

#print dict_load.keys()
energy=0
for  linex in HL_res:
    
    for liney in tem_neighbor:
        #print (linex, liney[0])
        if  linex==liney[0]:
                #print dict_load[liney[0][0:3]+'_'+liney[1][0:3]]
                energy=energy+dict_load[liney[0][0:3]+'_'+liney[1][0:3]]

print (filex,energy)


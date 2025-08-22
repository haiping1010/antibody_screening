
import sys

input_f=sys.argv[1]

fr=open(input_f,'r')
arr=fr.readlines()

index=0
tem_arr=input_f.split('-')
tem_arr_2=tem_arr[0].split('_')
antig=tem_arr_2[0]
anti=tem_arr_2[1]
chain_E=antig[4:]
chain_HL=anti[4:]

fw=open(input_f.replace('.pdb','_f.pdb'),'w')

for  line  in arr:
   index=index+1
   if index<=len(arr)-647:
         #print (line)
         if len(chain_HL)==1:
             if line.startswith('ATOM'):
                  line=line[:21]+'H'+line[22:]
                  fw.write(line)
             else:
                  fw.write(line)
         if  len(chain_HL)==2:
             if line.startswith('ATOM') and line[21:22]==chain_HL[0]:
                  line=line[:21]+'H'+line[22:]
                  fw.write(line)
             elif line.startswith('ATOM') and line[21:22]==chain_HL[1]:
                  line=line[:21]+'L'+line[22:]
                  fw.write(line)

             else:
                  fw.write(line)
   
   elif index>len(arr)-647:
             if line.startswith('ATOM'):
                  line=line[:21]+'A'+line[22:]
                  fw.write(line)
             else:
                  fw.write(line)

fw.close()
fr.close()



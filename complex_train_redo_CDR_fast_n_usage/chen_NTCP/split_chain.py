
fr=open('fold_2024_12_24_15_31_ntcp_antibody_model_0_cut.pdb','r')

all_arr=fr.readlines()
fw1=open('xxxx_antibody.pdb','w')
fw2=open('xxxx_antigen.pdb','w')

for line in all_arr:
      if line.startswith('ATOM'):
          if  line[21:22]=='A' or line[21:22]=='B':
              fw1.write(line)
          elif line[21:22]=='C':
              fw2.write(line)
      elif line.startswith('TER'):
          fw1.write(line)


fw1.close()
fw2.close()

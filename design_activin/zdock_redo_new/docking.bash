for i in antibody/*_antibody.pdb
    do
    for j in antigen/*_antigen.pdb
           do
           base1=${i%.pdb}
           base2=${j%.pdb}
           baseA=${base1:9}
           baseB=${base2:8}
           baseAA=${baseA%_antibody}
           baseBB=${baseB%_antigen}
           if [ "$baseAA" != "$baseBB" ];then
               mkdir -p  Docking/$baseA'_'$baseB 
               cd  Docking/$baseA'_'$baseB
               cp -r ../../antibody/$baseA'.pdb'   ../../antigen/$baseB'.pdb' ../../uniCHARMM  ../../create_lig  .
               mark_sur $baseA'.pdb'  receptor_m.pdb
               mark_sur $baseB'.pdb' ligand_m.pdb
               zdock -R receptor_m.pdb -L ligand_m.pdb -o zdock.out  -N  1
               create.pl zdock.out
               cd ../../
             fi
              done
        done

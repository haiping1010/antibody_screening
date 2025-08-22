cat  rerun_tem1.txt  | while read line
 do
IFS='_' read -r -a array <<< $line

i=${array[0]}
j=${array[1]}
           base1=${i%.pdb}
           base2=${j%.pdb}
           baseA=${base1%_antigen}
           echo $baseA
           baseB=${base2%_antibody}
           #baseAA=${baseA%_antibody}
           #baseBB=${baseB%_antigen}
           #if [ "$baseAA" != "$baseBB" ];then
               mkdir -p  Docking_all/$baseA'_'$baseB 
               cd  Docking_all/$baseA'_'$baseB
               cp -r ../../../antigen/$baseA'_antigen.pdb'   ../../../antibody/$baseB'_antibody.pdb'  ../../adding_block.py   ../../uniCHARMM  ../../create_lig  .
               mark_sur $baseA'_antigen.pdb'   ligand_m.pdb
               mark_sur $baseB'_antibody.pdb' receptor_m.pdb
               python adding_block.py  $baseA'_antigen.pdb'  ligand_m.pdb 
               python adding_block.py   $baseB'_antibody.pdb'   receptor_m.pdb
               zdock -R receptor_mm.pdb -L ligand_mm.pdb -o zdock.out  -N  1
               create.pl zdock.out
               cd ../../
            # fi
        
done

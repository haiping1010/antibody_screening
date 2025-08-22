
export path=/home/zhang/work/zdock3.0.2_linux_x64




cat tem-17.txt | while read line
 do
IFS=' ' read -r -a array <<< $line

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
               cp -r ../../antigen/$baseA'_antigen.pdb'   ../../antibody/$baseB'_antibody.pdb'  ../../adding_block.py   ../../uniCHARMM  ../../create_lig  .
               $path/mark_sur_static $baseA'_antigen.pdb'   ligand_m.pdb
               $path/mark_sur_static $baseB'_antibody.pdb' receptor_m.pdb
               python adding_block.py  $baseA'_antigen.pdb'  ligand_m.pdb 
               python adding_block.py   $baseB'_antibody.pdb'   receptor_m.pdb
               #nohup $path/zdock -R receptor_mm.pdb -L ligand_mm.pdb -o zdock.out  -N  1 &
	       $path/zdock -R receptor_mm.pdb -L ligand_mm.pdb -o zdock.out  -N  5 
               #sleep  40s
               #python $path/create.pl zdock.out
               cd ../../
            # fi
done

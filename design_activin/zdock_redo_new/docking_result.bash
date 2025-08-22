
export path=/home/zhang/work/zdock3.0.2_linux_x64




cat tem.txt | while read line
 do
IFS=' ' read -r -a array <<< $line

i=${array[0]}
j=${array[1]}
           base1=${i%.pdb}
           base2=${j%.pdb}
           baseA=${base1%_antigen}
           echo $baseA
           baseB=${base2%_antibody}
	   echo $baseB
           #baseAA=${baseA%_antibody}
           #baseBB=${baseB%_antigen}
           #if [ "$baseAA" != "$baseBB" ];then
               cd  Docking_all/$baseA'_'$baseB
               perl $path/create.pl zdock.out
               cd ../../
            # fi
done

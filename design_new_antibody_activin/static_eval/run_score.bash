rm summary.txt
for name in   *-complex.?.pdb 
do

python caculate_interaction.py $name >>summary.txt

done


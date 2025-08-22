cat    problem_file.txt  | while read line

do

grep  " "$line  tem.txt | grep "_antibody.pdb"  


done



for name in *_antibody.pdb

do

base=${name%.pdb}

echo $base
python pdb2fasta.py  $name   > $base'.fasta'



done

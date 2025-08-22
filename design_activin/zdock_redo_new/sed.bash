for i in tem-*.txt
do
index=${i%.txt}
cp -r docking_x.bash 'docking_'$index'.bash'

sed -i "s/XXXXX/$i/g"  'docking_'$index'.bash'


done

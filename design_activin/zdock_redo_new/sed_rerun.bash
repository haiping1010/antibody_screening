for i in rerun_tem-*.txt
do
index=${i%.txt}
cp -r rerun_docking_x.bash 'rerun_docking_'$index'.bash'

sed -i "s/XXXXX/$i/g"  'rerun_docking_'$index'.bash'


done

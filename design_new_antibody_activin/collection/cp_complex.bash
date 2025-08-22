
cd  ../Docking_all

for name in *_*
do

for i in {1..5}
do
cp -r  $name/'complex.'$i'.pdb'   ../collection/$name"-complex."$i".pdb"


done


done

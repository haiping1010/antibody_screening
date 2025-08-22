for name in  1nysB_*-complex.?.pdb
do

echo $name
nohup python    extract_A_HL.py   $name &

sleep 0.02s

done

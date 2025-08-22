
for name in temT_{20..60}.txt
do

	nohup python  python_2_pp_complex_d.py  $name  &
sleep 200s

done

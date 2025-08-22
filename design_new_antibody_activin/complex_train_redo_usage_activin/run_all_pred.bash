#conda activate py3
for name in   temT_*.txt
#for name in   all_data/temT_42.txt
#for name in   all_data/temT_100.txt  all_data/temT_101.txt
do

	id=${name:5:-4}
	echo $id
python  training_nn3_load_name.py   $id
#nohup python  training_nn3_load_name.py   $id  > 'out_Pred_'$id'.log' 2>&1&
#sleep  20s
done

#conda activate py3
for name in   all_screen/*_extracted_combined_sequences.txt
#for name in   all_data/temT_42.txt
#for name in   all_data/temT_100.txt  all_data/temT_101.txt
do

	id=${name:11:-4}
	echo $id
nohup python  read_smi_protein_nnn.py  $id  > 'outT_'$id'.log' 2>&1&
sleep  100s
done

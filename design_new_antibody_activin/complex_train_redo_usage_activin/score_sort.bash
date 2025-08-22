
cat  sorted_output_*.txt  > all_out.list

sort -g -rk 1,1 all_out.list  > all_out.sort

awk -F ',' ' $1 >= 0.9 ' all_out.sort  >  all_out_select.sort


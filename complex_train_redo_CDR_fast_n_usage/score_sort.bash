cat   L_P_*_paired_sorted_output.txt  > all_out.list

sort -g -rk 1,1 all_out.list  > all_out.sort

awk -F ',' ' $1 >= 0.99 ' all_out.sort  >  all_out_select.sort


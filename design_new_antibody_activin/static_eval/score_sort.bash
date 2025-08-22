
cat  summary.txt  > all_out.list

sort -g -k 2,2 all_out.list  > all_out.sort

awk -F ' ' ' $2 <=-5 ' all_out.sort  >  all_out_select.sort


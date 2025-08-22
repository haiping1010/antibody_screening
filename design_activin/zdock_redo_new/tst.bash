cat tem.txt | while read line
 do
IFS=' ' read -r -a array <<< $line

echo ${array[0]}
j=${arrray[1]}
##echo $line
echo $j    
done

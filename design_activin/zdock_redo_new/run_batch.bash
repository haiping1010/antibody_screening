for name in docking_tem-{1..30}.bash

do
bash={name%.bash}
echo $name
nohup bash $name> $base'.log' 2>&1 &


done

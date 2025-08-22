for name in docking_tem-{61..170}.bash

do
bash={name%.bash}
echo $name

qsub $name


done

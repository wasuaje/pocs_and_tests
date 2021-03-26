#!bin/bash
#
# Apagado rapido de maquinas qa y desarrollo
#

MAQ="10.3.1.2 10.3.1.3 10.2.60.60 10.3.1.10 10.3.1.13 10.3.1.14 10.3.1.59 "

for m in $MAQ
do
echo ssh root@$m shutdown -h now
ssh root@$m ls -la
done

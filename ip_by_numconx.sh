#!/bin/bash
#
# Me devuelva las 20 ips que mas se estan conectado a los equipos
#

IPS="204.228.236.6 204.228.236.13 204.228.236.17"
#" 204.228.236.17 204.228.236.10 204.228.236.2 204.228.236.7"
CMD="netstat -ntu | awk '{print \$5}' | awk -F: '{print \$1}' |sort|uniq -c|sort -rn| head -10"

for i in $IPS
do
 echo  ssh root@$i eval $CMD
 ssh root@$i $CMD
done

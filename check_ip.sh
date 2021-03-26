#!/bin/bash
# script que revisa ips disponibles en el red
# W.A. - 10-03-2010
#if [ "$A" ~= "Destination.*Unreachable" ]
echo "Ip'S disponibles en el rango entre 1 y 200 para ip's  Sistemas Internet"
for i in  {2..60}
do
A=`ping -c1 10.3.1.$i`
#echo "$A"
if [[ "$A" =~ "Destination Host Unreachable" ]]
then	
echo 10.3.1.$i
fi
done

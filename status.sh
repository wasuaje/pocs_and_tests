#!/bin/bash


FILE=/root/scripts/status/status_$(/bin/date +'%G%m%d_%H%M%S')

echo "*************************Resultados de TOP *********************************" > $FILE
top -b -n1 >> $FILE
echo "*************************Resultados de SAR *********************************" >> $FILE
sar -A >> $FILE
echo "*************************Resultados de PS -AUX *****************************" >> $FILE
ps -aux >> $FILE
echo "*************************Resultados de LSOF    *****************************" >> $FILE
lsof >> $FILE
echo "*************************Resultados de NETSTAT -a **************************" >> $FILE
netstat -a >> $FILE


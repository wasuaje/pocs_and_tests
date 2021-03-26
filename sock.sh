#!/bin/bash

echo ""> web01.txt
echo ""> web02.txt
echo ""> web03.txt
echo ""> mand10.txt


i=0
while  [  $i -eq 0 ]
do

date >> web01.txt; ssh root@m6 cat /proc/net/sockstat >> web01.txt
date >> web02.txt; ssh root@m13 cat /proc/net/sockstat >> web02.txt
date >> web03.txt; ssh root@m17 cat /proc/net/sockstat >> web03.txt
date >> mand10.txt; ssh root@m10 cat /proc/net/sockstat >> mand10.txt
sleep 50
done

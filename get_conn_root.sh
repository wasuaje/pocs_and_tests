

VAR=`ssh root@m6 netstat -na | grep ".179:8080" | wc -l`; echo  Static web01 el universal=  $VAR


VAR1=`ssh root@m13 netstat -na | grep ".177:8080" | wc -l`; echo  Static web02 el universal=  $VAR1


VAR2=`ssh root@m17 netstat -na | grep ".178:8080" | wc -l`; echo Static web03 el universal=  $VAR2


VAR3=`ssh root@m6 netstat -na | grep "207.70.52.179:8090" | wc -l`; echo Dinamic el universal Web01=  $VAR3

VAR4=`ssh root@m13 netstat -na | grep "207.70.52.177:8090" | wc -l`; echo Dinamic el universal Web02=  $VAR4

VAR5=`ssh root@m17 netstat -na | grep "207.70.52.178:8090" | wc -l`; echo Dinamic el universal Web03=  $VAR5



VAR6=`ssh root@m7 netstat -na | grep "204.228.236.8.80 " | wc -l`; echo Empleos=  $VAR6


VAR7=`ssh root@m13 netstat -na | grep ".11:80" | wc -l `;echo Clasificados=  $VAR7


VAR8=`ssh root@m10 netstat -na | grep ".10:80" | wc -l `;echo open Adstream=  $VAR8

let TOTAL=$VAR+$VAR1+$VAR2+$VAR3+$VAR4+$VAR5+$VAR6+$VAR7+$VAR8

echo "*** Total General = " $TOTAL



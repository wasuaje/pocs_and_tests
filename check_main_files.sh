#!/bin/sh
cd /tmp

#Descargo todos los archivos que necesito, los diferencio en nombre al llegar para compararlos
scp root@m6:/usr/local/apacheTest-statics/conf/httpd.conf ./httpd6.conf
scp root@m13:/usr/local/apacheTest-statics/conf/httpd.conf ./httpd13.conf
scp root@m17:/usr/local/apacheTest-statics/conf/httpd.conf ./httpd17.conf

scp root@m6:/usr/local/apacheTest-statics/conf/logrotate.conf ./logrotate6.conf
scp root@m13:/usr/local/apacheTest-statics/conf/logrotate.conf ./logrotate13.conf
scp root@m17:/usr/local/apacheTest-statics/conf/logrotate.conf ./logrotate17.conf

scp root@m6:/etc/hosts ./hosts6
scp root@m13:/etc/hosts ./hosts13
scp root@m17:/etc/hosts ./hosts17

ssh root@m6 crontab -l > ./crontab6
ssh root@m13 crontab -l > ./crontab13
ssh root@m17 crontab -l > ./crontab17

#la letra son el numero de lineas con Diferencias y la letre con numero el texto con la diferencia para arreglarlo
#Diferencias para httpd
A=`diff httpd6.conf  httpd13.conf | wc -l`
A1=`diff httpd6.conf  httpd13.conf`
B=`diff httpd6.conf  httpd17.conf | wc -l`
B1=`diff httpd6.conf  httpd17.conf `
C=`diff httpd13.conf httpd17.conf | wc -l`
C1=`diff httpd13.conf httpd17.conf `

#Diferencias para logrotate
D=`diff logrotate6.conf logrotate6.conf | wc -l`
D1=`diff logrotate6.conf logrotate6.conf `
E=`diff logrotate6.conf logrotate13.conf | wc -l`
E1=`diff logrotate6.conf logrotate13.conf `
F=`diff logrotate13.conf logrotate17.conf | wc -l`
F1=`diff logrotate13.conf logrotate17.conf `

#Diferencias para /etc/hosts
G=`diff hosts6 hosts13 | wc -l`
G1=`diff hosts6 hosts13 `
H=`diff hosts6 hosts17 | wc -l`
H1=`diff hosts6 hosts17 `
I=`diff hosts13 hosts17 | wc -l`
I1=`diff hosts13 hosts17 `

#Diferencias para crontab
J=`diff crontab6 crontab13 | wc -l`
J1=`diff crontab6 crontab13`
K=`diff crontab6 crontab17 | wc -l`
K1=`diff crontab6 crontab17`
L=`diff crontab13 crontab17 | wc -l`
L1=`diff crontab13 crontab17`


if [ $A -gt "0" ] ; then
echo "Hay diferencias en httpd.conf entre web01 y web02 \n" > msg.txt
echo $A1  >> msg.txt
mail -s "Diferencias en archivo httpd.conf" wasuaje@eluniversal.com < msg.txt
fi

if [ $B -gt "0" ] ; then
echo "Hay diferencias en httpd.conf entre web01 y web03 \n" > msg.txt
echo $B1  >> msg.txt
mail -s "Diferencias en archivo httpd.conf" wasuaje@eluniversal.com < msg.txt
fi

if [ $C -gt "0" ] ; then
echo "Hay diferencias en httpd.conf entre web02 y web03 \n" > msg.txt
echo $C1  >> msg.txt
mail -s "Diferencias en archivo httpd.conf" wasuaje@eluniversal.com < msg.txt
fi

if [ $D -gt "0" ] ; then
echo "Hay diferencias en logrotate.conf entre web01 y web02 \n" > msg.txt
echo $D1  >> msg.txt
mail -s "Diferencias en archivo logrotate.conf" wasuaje@eluniversal.com < msg.txt
fi

if [ $E -gt "0" ] ; then
echo "Hay diferencias en logrotate.conf entre web01 y web03 \n" > msg.txt
echo $E1  >> msg.txt
mail -s "Diferencias en archivo logrotate.conf" wasuaje@eluniversal.com < msg.txt
fi

if [ $F -gt "0" ] ; then
echo "Hay diferencias en logrotate.conf entre web02 y web03 \n" > msg.txt
echo $F1  >> msg.txt
mail -s "Diferencias en archivo logrotate.conf" wasuaje@eluniversal.com < msg.txt
fi

if [ $G -gt "0" ] ; then
echo "Hay diferencias en /etc/hosts entre web01 y web02 \n" > msg.txt
echo $G1  >> msg.txt
mail -s "Diferencias en archivo /etc/hosts" wasuaje@eluniversal.com < msg.txt
fi

if [ $H -gt "0" ] ; then
echo "Hay diferencias en /etc/hosts entre web01 y web03 \n" > msg.txt
echo $H1  >> msg.txt
mail -s "Diferencias en archivo /etc/hosts" wasuaje@eluniversal.com < msg.txt
fi

if [ $I -gt "0" ] ; then
echo "Hay diferencias en /etc/hosts entre web02 y web03 \n" > msg.txt
echo $I1  >> msg.txt
mail -s "Diferencias en archivo /etc/hosts" wasuaje@eluniversal.com < msg.txt
fi

if [ $J -gt "0" ] ; then
echo "Hay diferencias en crontab entre web01 y web02 \n" > msg.txt
echo $J1  >> msg.txt
mail -s "Diferencias en archivo crontab" wasuaje@eluniversal.com < msg.txt
fi

if [ $K -gt "0" ] ; then
echo "Hay diferencias en crontab entre web01 y web03 \n" > msg.txt
echo $K1  >> msg.txt
mail -s "Diferencias en archivo crontab" wasuaje@eluniversal.com < msg.txt
fi

if [ $L -gt "0" ] ; then
echo "Hay diferencias en crontab entre web02 y web03 \n" > msg.txt
echo $L1  >> msg.txt
mail -s "Diferencias en archivo crontab" wasuaje@eluniversal.com < msg.txt
fi



#Se borran los archivos descargados y los generados
rm -rf *.conf
rm -rf *.txt
rm -rf hosts*
rm -rf cront*

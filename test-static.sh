#con 20 conexiones
echo "***************************************"
echo "*prueba con 20 conexiones 500 request *"
echo "*144 bytes                            *"
echo "***************************************"
ab -q -c 20 -n 750 198.60.236.4/images/eu3/icons-btns/destacadas-nums-on.gif

echo "************"
echo "* 30kbytes *"
echo "************"
ab -q -c 20 -n 750 198.60.236.4/2010/01/29/protestasblair290110.jpg.393.288.thumb

echo "************"
echo "* 109kbytes*"
echo "************"
ab -q -c 20 -n 750 198.60.236.4/flash/relatoEuro2008.swf


echo "***************************************"
echo "*prueba con 40 conexiones 500 request *"
echo "*144 bytes                            *"
echo "***************************************"
ab -q -c 40 -n 750 198.60.236.4/images/eu3/icons-btns/destacadas-nums-on.gif

echo "************"
echo "* 30kbytes *"
echo "************"
ab -q -c 40 -n 750 198.60.236.4/2010/01/29/protestasblair290110.jpg.393.288.thumb

echo "************"
echo "* 109kbytes*"
echo "************"
ab -q -c 40 -n 750 198.60.236.4/flash/relatoEuro2008.swf



echo "***************************************"
echo "*prueba con 60 conexiones 500 request *"
echo "*144 bytes                            *"
echo "***************************************"
ab -q -c 60 -n 750 198.60.236.4/images/eu3/icons-btns/destacadas-nums-on.gif

echo "************"
echo "* 30kbytes *"
echo "************"
ab -q -c 60 -n 750 198.60.236.4/2010/01/29/protestasblair290110.jpg.393.288.thumb


echo "************"
echo "* 109kbytes*"
echo "************"
ab -q -c 60 -n 750 198.60.236.4/flash/relatoEuro2008.swf






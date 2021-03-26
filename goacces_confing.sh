goaccess --log-format "%h %^[%d:%t %^] \"%r\" %s %b \"%R\" \"%u\""  --date-format %d/%b/%Y  --time-format %H:%M:%S -f www-estampas-access.log  | mail -a "Content-type: text/html" -s "prueba"  wasuaje@eluniversal.com
(
  echo To: wasuaje@eluniversal.com
  echo From: wasuaje@involta.com
  echo "Content-Type: text/html; "
  echo Subject: a logfile
  echo
  cat reporte_estampas.html
) | sendmail -t

(
echo "From: wasuaje@involta.com";
echo "To: wasuaje@involta.com";
echo "Subject: prueba";
echo "Content-Type: text/html";
echo "MIME-Version: 1.0";
echo "";
cat reporte_estampas.html;
) | sendmail -t



goaccess --log-format "%h %^[%d:%t %^] \"%r\" %s %b \"%R\" \"%u\""  --date-format %d/%b/%Y  --time-format %H:%M:%S -f www-estampas-access.log > reporte_estampas.html

(echo To: wasuaje@eluniversal.com;   echo From: wasuaje@prueba.com;   echo "Content-Type: text/html; ";   echo Subject: a logfile;   echo;   cat reporte_estampas.html;) | sendmail -t
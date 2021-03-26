#su - oraeup -c ./oracle/load/prueba.sh 
#############
#REDUCIDO
#############

su - oraeud -c /oracle/EUD/pruebaresp.sh 

LOG_FILE="/home/backup_bd_sap_desa.log"

echo "****" > $LOG_FILE
echo "comenzando el respaldo" >> $LOG_FILE
date >> $LOG_FILE


rman target / log=$LOG_FILE <<EOF

run {
allocate channel c1 type disk;
backup current controlfile format '/home/pruebarespaldo01.bak';
}

exit;
exit;
EOF

echo "Finalizado el respaldo" >> $LOG_FILE
date >> $LOG_FILE


############
### Funciona 
############

LOG_FILE="/oracle/load/backup_bd_sap_desa.log"

echo "****" > $LOG_FILE
echo "comenzando el respaldo" >> $LOG_FILE
date >> $LOG_FILE


rman target / log=$LOG_FILE <<EOF

run {
crosscheck archivelog all;
allocate channel C1 device type DISK format '/backup2/back_prod_%U_%d_%D_%M_%Y.bak';
backup database include current controlfile plus archivelog delete all input;
delete obsolete;
}

exit;
exit;
EOF

echo "Finalizado el respaldo" >> $LOG_FILE
date >> $LOG_FILE



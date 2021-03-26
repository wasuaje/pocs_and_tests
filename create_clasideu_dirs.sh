#!/bin/bash
# 
# Creado por Wasuaje para Clasideu
# 28/02/2011
# Modificado el 02/03/2011 para que use mes del año + 1
# y tome en cuenta que en el mes 12 usara mes 13 entonces lo convierte en 01
# de la misma manera le suma 1 al año en curso
# No acepta parametros
# Toma el mesaño de la fecha actual, crea el directorio FROMDIR+BASEDIR+mesaño
# Luego hace un link simbólico desde lo anteriormente creado hacia TODIR+BASEDIR+mesaño
# Hay que asegurarse que el cronjob esta asi 59 23 28 * * /root/scripts/create_clasideu_dirs.sh
# Y que el archivo tiene permisos de ejecucion

A=`/bin/date +'%m'`
MONTH=`expr $A + 1`
YEAR=`/bin/date +'%G'`
if [ $MONTH = 13 ]; then
	MONTH=1
	OLDYEAR=`/bin/date +'%G'`
	YEAR=`expr $OLDYEAR + 1`
fi	
NEWDIR=`printf "%02d" $MONTH`$YEAR
SUBDIRS="INMUEBLE CARRO ARTICULO SERVICIO NEGOCIO EMPLEO"

#para desarrollo habilitar las 3 lineas siguientes y modificarlas segun su sistema
#cd /home/wasuaje/Documentos/desarrollo/pruebaclasi
#FROMDIR="./manduca13"
#TODIR="./manduca10"

#PARA PRODUCCION habilitar las siguientes 3 lineas
BASEDIR="/netapp/clasificados/fotos/galeria/fotos/clasificados"
FROMDIR="/manduca13"
TODIR="/manduca10"

#Loop principal crea el directorio y a la vez desde alli el symlink hasta m10 

for D in $SUBDIRS
do
	mkdir -p $FROMDIR$BASEDIR/$D/$NEWDIR
	ln -s 	$FROMDIR$BASEDIR/$D/$NEWDIR $TODIR$BASEDIR/$D/$NEWDIR
done

	



#!/bin/bash
# 
# Creado por Wasuaje para Clasideu
# 28/02/2011
# No acepta parametros
# Toma el mesaño de la fecha actual, crea el directorio FROMDIR+BASEDIR+mesaño
# Luego hace un link simbólico desde lo anteriormente creado hacia TODIR+BASEDIR+mesaño
# Hay que asegurarse que el cronjob esta asi 59 23 28 * * /root/scripts/create_clasideu_dirs.sh
# Y que el archivo tiene permisos de ejecucion

A=`/bin/date +'%m'`
MONTH=`expr $A + 10`
YEAR=`/bin/date +'%G'`
if [ $MONTH = 13 ]; then
	MONTH=1
	OLDYEAR=`/bin/date +'%G'`
	YEAR=`expr $OLDYEAR + 1`
fi	
NEWDIR=`printf "%02d" $MONTH`$YEAR

echo $NEWDIR

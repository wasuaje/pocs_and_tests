IMG=/usr/local/ImageMagick-671/bin
IR="cd /home/manduca/wuelf"
comando="$IR; $IMG/convert -debug 'All' -colorspace RGB -resize 200X200 evil1.jpg evil2.jpg"

ssh root@m2 $comando 

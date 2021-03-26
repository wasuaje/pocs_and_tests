#!bin/bash
for i in {1..2}
do
mail -s prueba wasuaje@hotmail.com,wasuaje@eluniversal.com < test.txt
done

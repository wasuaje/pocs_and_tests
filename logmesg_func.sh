logmsg()
{
echo
echo "### `date` ###################"
for msg in "$@"
do
echo "# $msg"
done
echo "####################################################"
}

logmsg cualqueircosa


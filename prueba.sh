set password [lrange $argv 0 0]
set ipaddr [lrange $argv 1 1]
set scriptname [lrange $argv 2 2]
set arg1 [lrange $argv 3 3]
set timeout -1
# now connect to remote UNIX box (ipaddr) with given script to execute

spawn ssh root@$ipaddr $scriptname $arg1 match_max 100000
# Look for passwod prompt
expect "Password:"
# Send password aka $password
send -- "$password1\r"
expect "#"
send --$password1\r
# send blank line (\r) to make sure we get back to gui
send -- "\r"
expect eof

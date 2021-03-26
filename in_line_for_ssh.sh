for i in $string ; do ssh  root@204.228.236."$i" "netstat -ln|grep 80

#!/bin/bash

pass="B4rc3l0n4!"
user="root"
LOCALBOXES="10.3.1.2 10.3.0.130 10.3.0.239 10.3.1.10 10.3.1.12 10.3.1.13 10.3.1.14 10.3.1.61 10.3.1.77 10.3.1.59"

for ips in $LOCALBOXES;
do
ssh root@$ips passwd root
done

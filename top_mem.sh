#!/bin/bash
clear
ps gxu | head -n1 
ps gxu | sort -k 4nr  | head -n30 | grep -v PID

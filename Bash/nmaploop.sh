#!/bin/bash
#script to do quick scans of all ports with Nmap, then deep scans of open ports on a target
#$1 is the first command line argument, $2 would be the second, ect
echo "NOTE: this does not scan UDP ports, and is probably very noisy!!!"
echo "_  _ ____ _   _ ___  ____    ____ _  _ _ ____ _  _ ____ ____ "
echo "|\/| |__|  \_/  |__] |___    |  | |  | | |    |_/  |___ |__/ "
echo "|  | |  |   |   |__] |___    |_\| |__| | |___ | \_ |___ |  \ "
echo "                                                             "
echo Targeting $1
echo
echo this may take a moment
echo
translated_scan=$(grep -o -E [0-9]+\/ <(nmap -p- $1) | tr '/ ' ',' | tr -d [:space:])
echo "scanning ports found open: ${translated_scan::-1}"
ports="${translated_scan::-1}"
echo
read -p "filename base:  " filename
echo
echo "beginning deep scan"
(nmap $1 -A -p $ports -oA $filename)

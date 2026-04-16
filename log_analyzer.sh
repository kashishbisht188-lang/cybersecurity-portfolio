#!/bin/bash
# Log Analyzer - finds failed login attempts
# Author: Kashish
# Description: Extracts failed login attempts from Linux system logs

echo "=== FAILED LOGIN ATTEMPTS ==="
grep "unix_chkpwd" failed.txt | awk '{print $1,$2,$3,$11}' | sed 's/failed/ALERT/g'

echo "=== TOTAL COUNT ==="
grep "unix_chkpwd" failed.txt | wc -l

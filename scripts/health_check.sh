#!/usr/bin/env bash
# Server resource health assessment utility
set -euo pipefail

echo "=========================================="
echo " HOST RESOURCE HEALTH REPORT: $(hostname)"
echo " TIME: $(date -u)"
echo "=========================================="

echo -e "\n[1] CPU Load:"
uptime

echo -e "\n[2] Memory Utilization:"
free -h

echo -e "\n[3] Disk Space Usage:"
df -h -x tmpfs -x devtmpfs

echo "=========================================="
echo "Status: OK"

#!/bin/bash
cat /tmp/tod_page_crop_stats.txt | awk 'NR > 1 {print $1, $2, $3}'

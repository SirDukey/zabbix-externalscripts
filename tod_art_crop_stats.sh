#!/bin/bash
cat /tmp/tod_art_crop_stats.txt | awk 'NR > 1 {print $1, $2, $3}'

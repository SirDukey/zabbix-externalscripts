#!/bin/bash

ssh root@192.168.1.13 du -hs /var/lib/mysql/* | grep noviny | awk '{ print $1 }'
